#!/usr/bin/env python3
"""Sentinel: autonomous article generation at 20h.

Usage:
    python3 scripts/sentinel.py              # today's date
    python3 scripts/sentinel.py --date DATE  # specific date
    python3 scripts/sentinel.py --dry-run    # check guards only
"""

import argparse
import json
import logging
import subprocess
import sys
import time
from datetime import date
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MIN_SOURCES = 3
TRANSIENT_API_STATUSES = {429, 500, 502, 503, 504}
GENERATION_MAX_RETRIES = 2
GENERATION_RETRY_DELAY_SECONDS = 60


def is_transient_error(stdout: str) -> bool:
    """Return True if the claude -p JSON output reports a transient API error."""
    try:
        data = json.loads(stdout)
    except (json.JSONDecodeError, TypeError):
        return False
    return data.get("api_error_status") in TRANSIENT_API_STATUSES


def setup_logging(target_date: str) -> logging.Logger:
    log_dir = PROJECT_ROOT / "data" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / f"{target_date}-sentinel.log"

    logger = logging.getLogger("sentinel")
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(log_file, mode="a")
    file_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
    logger.addHandler(console_handler)

    return logger


def notify(title: str, message: str):
    """Send macOS notification."""
    try:
        subprocess.run(
            ["osascript", "-e", f'display notification "{message}" with title "{title}"'],
            check=False,
            capture_output=True,
        )
    except FileNotFoundError:
        pass


def run_command(cmd: list[str], logger: logging.Logger, cwd: Path | None = None) -> subprocess.CompletedProcess:
    """Run a command, log output, return result."""
    logger.info(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd or PROJECT_ROOT)
    if result.stdout:
        logger.info(f"stdout: {result.stdout[:2000]}")
    if result.stderr:
        logger.warning(f"stderr: {result.stderr[:2000]}")
    return result


def check_idempotence(target_date: str) -> bool:
    """Return True if article already exists."""
    return (PROJECT_ROOT / "data" / "output" / f"{target_date}-article.md").exists()


def preflight_sources(target_date: str, logger: logging.Logger) -> bool:
    """Check if enough sources are available. Return True if OK."""
    result = run_command(
        ["uv", "run", "python3", "scripts/load_sources.py", target_date, "--carry-forward", "3"],
        logger,
    )
    if result.returncode != 0:
        logger.error(f"Sources script failed with exit code {result.returncode}")
        return False

    try:
        data = json.loads(result.stdout)
        source_count = len(data.get("sources", []))
        logger.info(f"Found {source_count} sources")
        return source_count >= MIN_SOURCES
    except (json.JSONDecodeError, KeyError) as e:
        logger.error(f"Failed to parse sources output: {e}")
        return False


def run_generation(target_date: str, logger: logging.Logger) -> bool:
    """Run Claude in headless mode for article generation."""
    prompt = f"""Run /generate {target_date} in autonomous mode.
Skip step 0.5 (metrics).
Accept all filtered sources without confirmation.
Note trends but continue without asking.
Select narrative autonomously: prioritize trend clusters, then theme priority (IA > Leadership > Data > Tech).
Skip step 6 (Notion push).
Skip step 7 (Notion review wait).
Skip step 8 (Notion fetch).
In step 9: copy files to site but do NOT propose /ship."""

    allowed_tools = "Bash,Read,Write,Edit,MultiEdit,Glob,Grep,WebFetch"

    cmd = [
        "claude", "-p", prompt,
        "--model", "opus",
        "--allowedTools", allowed_tools,
        "--output-format", "json",
        "--permission-mode", "bypassPermissions",
        "--max-budget-usd", "5",
    ]

    attempt = 1
    while True:
        result = run_command(cmd, logger)
        if result.returncode == 0:
            break
        if attempt <= GENERATION_MAX_RETRIES and is_transient_error(result.stdout):
            logger.warning(
                f"Transient API error on attempt {attempt}/{GENERATION_MAX_RETRIES + 1}, "
                f"retrying in {GENERATION_RETRY_DELAY_SECONDS}s..."
            )
            time.sleep(GENERATION_RETRY_DELAY_SECONDS)
            attempt += 1
            continue
        logger.error(f"Claude generation failed with exit code {result.returncode}")
        return False

    # Verify output files were created
    article = PROJECT_ROOT / "data" / "output" / f"{target_date}-article.md"
    if not article.exists():
        logger.error("Article file was not created by Claude")
        return False

    logger.info("Article generation completed successfully")
    return True


def run_image_generation(target_date: str, logger: logging.Logger) -> bool:
    """Generate the article image via Gemini API."""
    prompt_file = PROJECT_ROOT / "data" / "output" / f"{target_date}-image-prompt.md"
    if not prompt_file.exists():
        logger.warning(f"Image prompt file not found: {prompt_file}")
        return False

    result = run_command(
        ["uv", "run", "python3", "scripts/generate_image.py", target_date],
        logger,
    )
    if result.returncode != 0:
        logger.warning("Image generation failed — continuing without image")
        return False

    logger.info("Image generation completed")
    return True


def main():
    parser = argparse.ArgumentParser(description="Sentinel: autonomous article generation")
    parser.add_argument("--date", default=date.today().isoformat(), help="Target date (YYYY-MM-DD)")
    parser.add_argument("--dry-run", action="store_true", help="Check guards only, don't generate")
    args = parser.parse_args()

    target_date = args.date
    logger = setup_logging(target_date)
    logger.info(f"=== Sentinel starting for {target_date} ===")

    # Guard: idempotence
    if check_idempotence(target_date):
        logger.info(f"Article already exists for {target_date} — skipping")
        return

    # Pre-flight: check sources
    if not preflight_sources(target_date, logger):
        msg = f"Not enough sources for {target_date} (minimum {MIN_SOURCES})"
        logger.warning(msg)
        notify("Veilleur — Pas assez de sources", msg)
        return

    if args.dry_run:
        logger.info("Dry run — guards passed, would proceed with generation")
        print(f"Dry run OK: {target_date} has enough sources, article not yet generated")
        return

    # Step 1: Generate article via Claude
    if not run_generation(target_date, logger):
        notify("Veilleur — Erreur", f"Échec de la génération pour {target_date}")
        sys.exit(1)

    # Step 2: Create NotebookLM notebook + podcast (fr)
    result = run_command(["just", "notebook", target_date, "--audio"], logger)
    if result.returncode != 0:
        logger.warning("NotebookLM creation failed — continuing")

    # Step 3: Generate image via Gemini
    run_image_generation(target_date, logger)

    # Step 4: Generate Instagram carousel + reel
    result = run_command(["uv", "run", "python3", "scripts/generate_instagram.py", target_date], logger)
    if result.returncode != 0:
        logger.warning("Instagram generation failed — continuing")

    # Step 3: Notify
    article_file = PROJECT_ROOT / "data" / "output" / f"{target_date}-article.md"
    title = "Article généré"
    for line in article_file.read_text().splitlines():
        if line.startswith("title:"):
            title = line.split(":", 1)[1].strip().strip('"')
            break

    notify("Veilleur — Article prêt", f"{target_date}: {title}")

    # Step 5: Autopublish (chained, not separate cron)
    logger.info("Running autopublish...")
    result = run_command(
        ["uv", "run", "python3", "scripts/autopublish.py", "--date", target_date],
        logger,
    )
    if result.returncode != 0:
        logger.warning("Autopublish failed")
        notify("Veilleur — Erreur", f"Échec de l'autopublish pour {target_date}")

    logger.info(f"=== Sentinel completed for {target_date} ===")


if __name__ == "__main__":
    main()
