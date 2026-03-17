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


def check_pr_exists(target_date: str, logger: logging.Logger) -> bool:
    """Check if a PR already exists for this date."""
    branch = f"feat/article-{target_date}"
    result = run_command(["gh", "pr", "list", "--head", branch, "--json", "number"], logger)
    if result.returncode != 0:
        logger.warning("Failed to check PRs via gh")
        return False
    try:
        prs = __import__("json").loads(result.stdout)
        return len(prs) > 0
    except Exception:
        return False


def run_ship(target_date: str, logger: logging.Logger) -> bool:
    """Run /ship via Claude CLI."""
    prompt = f"""Run /ship for article {target_date}. Branch: feat/article-{target_date}.
Commit all files in data/output/{target_date}-*, data/fiches/{target_date}-*,
site/src/content/articles/{target_date}.md, site/src/content/fiches/{target_date}-*,
site/public/images/{target_date}.png (if exists).
Open PR with title 'feat: add {target_date} article and fiches'."""

    cmd = [
        "claude", "-p", prompt,
        "--model", "sonnet",
        "--allowedTools", "Bash,Read,Write,Edit,Glob,Grep",
        "--permission-mode", "bypassPermissions",
        "--max-budget-usd", "2",
    ]
    result = run_command(cmd, logger)
    if result.returncode != 0:
        logger.error("Ship step failed")
        return False
    logger.info("Ship completed")
    return True


def run_merge(target_date: str, logger: logging.Logger) -> bool:
    """Run /merge via Claude CLI."""
    branch = f"feat/article-{target_date}"
    prompt = f"""Run /merge for the PR on branch {branch}.
Handle any Copilot review comments, then squash merge."""

    cmd = [
        "claude", "-p", prompt,
        "--model", "sonnet",
        "--allowedTools", "Bash,Read,Write,Edit,Glob,Grep",
        "--permission-mode", "bypassPermissions",
        "--max-budget-usd", "2",
    ]
    result = run_command(cmd, logger)
    if result.returncode != 0:
        logger.error("Merge step failed")
        return False
    logger.info("Merge completed")
    return True


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

    # Guard: PR must not already exist
    if check_pr_exists(target_date, logger):
        logger.info(f"PR already exists for {target_date} — skipping")
        return

    if args.dry_run:
        logger.info("Dry run — guards passed, would proceed with ship + merge")
        print(f"Dry run OK: article exists for {target_date}, no PR yet")
        return

    # Step 1: Ship (create branch, commit, push, open PR)
    if not run_ship(target_date, logger):
        notify("Veilleur — Erreur", f"Échec du ship pour {target_date}")
        sys.exit(1)

    # Step 2: Merge
    if not run_merge(target_date, logger):
        notify("Veilleur — Erreur", f"Échec du merge pour {target_date}")
        sys.exit(1)

    # Step 3: Notify
    notify("Veilleur — Publié", f"Article du {target_date} publié sur le site")
    logger.info(f"=== Autopublish completed for {target_date} ===")


if __name__ == "__main__":
    main()
