#!/usr/bin/env python3
"""Autopublish: if article not reviewed by 23h, publish anyway.

Usage:
    python3 scripts/autopublish.py              # today's date
    python3 scripts/autopublish.py --date DATE  # specific date
    python3 scripts/autopublish.py --dry-run    # check guards only
"""

import argparse
import logging
import subprocess
import sys
from datetime import date
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def setup_logging(target_date: str) -> logging.Logger:
    log_dir = PROJECT_ROOT / "data" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / f"{target_date}-autopublish.log"

    logger = logging.getLogger("autopublish")
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
    logger.info(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd or PROJECT_ROOT)
    if result.stdout:
        logger.info(f"stdout: {result.stdout[:2000]}")
    if result.stderr:
        logger.warning(f"stderr: {result.stderr[:2000]}")
    return result


def collect_files(target_date: str) -> list[str]:
    """Collect all files to commit for the given date."""
    patterns = [
        f"site/src/content/articles/{target_date}.md",
        f"site/src/content/fiches/{target_date}-*",
        f"site/public/images/{target_date}.png",
        "site/src/data/metrics.json",
        "site/src/data/themes-over-time.json",
        "site/src/data/articles-meta.json",
    ]
    files = []
    for pattern in patterns:
        found = sorted(PROJECT_ROOT.glob(pattern))
        files.extend(str(f.relative_to(PROJECT_ROOT)) for f in found)
    return files


def main():
    parser = argparse.ArgumentParser(description="Autopublish: automatic article publication")
    parser.add_argument("--date", default=date.today().isoformat(), help="Target date (YYYY-MM-DD)")
    parser.add_argument("--dry-run", action="store_true", help="Check guards only")
    args = parser.parse_args()

    target_date = args.date
    logger = setup_logging(target_date)
    logger.info(f"=== Autopublish starting for {target_date} ===")

    # Guard: article must exist
    article = PROJECT_ROOT / "data" / "output" / f"{target_date}-article.md"
    if not article.exists():
        logger.info(f"No article for {target_date} — nothing to publish")
        return

    # Guard: check if already published (site article exists and is committed)
    result = run_command(
        ["git", "log", "--oneline", "-1", "--", f"site/src/content/articles/{target_date}.md"],
        logger,
    )
    if result.stdout.strip():
        logger.info(f"Article {target_date} already committed — skipping")
        return

    # Collect files to commit
    files = collect_files(target_date)
    if not files:
        logger.info("No files to commit")
        return

    logger.info(f"Files to publish: {files}")

    if args.dry_run:
        logger.info("Dry run — guards passed, would commit and push")
        print(f"Dry run OK: {len(files)} files to publish for {target_date}")
        return

    # Stage files
    result = run_command(["git", "add"] + files, logger)
    if result.returncode != 0:
        logger.error("Failed to stage files")
        notify("Veilleur — Erreur", f"Échec du staging pour {target_date}")
        sys.exit(1)

    # Commit
    message = f"feat: add {target_date} article and fiches"
    result = run_command(["git", "commit", "-m", message], logger)
    if result.returncode != 0:
        logger.error("Failed to commit")
        notify("Veilleur — Erreur", f"Échec du commit pour {target_date}")
        sys.exit(1)

    # Push to main
    result = run_command(["git", "push"], logger)
    if result.returncode != 0:
        logger.error("Failed to push")
        notify("Veilleur — Erreur", f"Échec du push pour {target_date}")
        sys.exit(1)

    notify("Veilleur — Publié", f"Article du {target_date} publié sur le site")
    logger.info(f"=== Autopublish completed for {target_date} ===")


if __name__ == "__main__":
    main()
