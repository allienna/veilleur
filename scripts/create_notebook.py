#!/usr/bin/env python3
"""
veilleur — Create a NotebookLM notebook from daily sources.

Usage:
    python3 scripts/create_notebook.py 2026-03-16
    python3 scripts/create_notebook.py 2026-03-16 --audio
    python3 scripts/create_notebook.py 2026-03-16 --dry-run

Loads kept sources, deduplicates, filters tracking URLs,
creates a NotebookLM notebook named YYYY-MM-DD,
adds each source URL, and optionally generates a podcast.
"""

import json
import subprocess
import sys
import time
from datetime import date
from urllib.parse import urlparse

# Tracking/redirect domains to skip — these aren't real article URLs
SKIP_URL_PATTERNS = [
    'upmynt.com',
    'substack.com/redirect',
    'substack.com/app-link',
    'substack.com/signup',
    'substack.com/@',
    'elinkc20.the-nbs.fr',
    'email.beehiivstatus.com',
    'tldr.tech/signup',
    'tldr.tech/data/manage',
    'tldr.tech/dev/manage',
    'tldr.tech/tech/manage',
    'open.substack.com',
    '/feedback/',
    '/manage?email=',
    '/unsubscribe',
    '/disable_email',
]

# Title patterns indicating non-article pages
SKIP_TITLE_PATTERNS = [
    '502 bad gateway',
    'sign up',
    'introducing the substack app',
    'substack | signup',
    'message important',
    'whoa! this isn\'t the page',
]


def load_kept_sources(target_date: str) -> list[dict]:
    """Load sources via load_sources.py and return kept entries."""
    result = subprocess.run(
        ['uv', 'run', 'python3', 'scripts/load_sources.py', target_date],
        capture_output=True, text=True, cwd='.'
    )
    if result.returncode != 0:
        print(f"Error loading sources: {result.stderr}", file=sys.stderr)
        sys.exit(1)

    data = json.loads(result.stdout)
    return data.get('sources', [])


def is_tracking_url(url: str) -> bool:
    """Check if URL is a tracking/redirect link."""
    return any(pattern in url for pattern in SKIP_URL_PATTERNS)


def is_skippable_title(title: str) -> bool:
    """Check if title indicates a non-article page."""
    title_lower = title.lower()
    return any(pattern in title_lower for pattern in SKIP_TITLE_PATTERNS)


def deduplicate_by_title(sources: list[dict]) -> list[dict]:
    """Remove duplicate sources that share the same title."""
    seen_titles = set()
    unique = []
    for s in sources:
        # Normalize title for comparison
        norm_title = s['title'].strip().lower()[:80]
        if norm_title in seen_titles:
            continue
        seen_titles.add(norm_title)
        unique.append(s)
    return unique


def filter_sources(sources: list[dict]) -> list[dict]:
    """Filter sources to only real article URLs suitable for NotebookLM."""
    filtered = []
    for s in sources:
        url = s['url']
        title = s['title']

        if is_tracking_url(url):
            continue
        if is_skippable_title(title):
            continue

        filtered.append(s)

    return deduplicate_by_title(filtered)


def nlm_run(args: list[str], check: bool = True) -> subprocess.CompletedProcess:
    """Run an nlm CLI command."""
    cmd = ['nlm'] + args
    result = subprocess.run(cmd, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"nlm error: {' '.join(cmd)}", file=sys.stderr)
        print(result.stderr, file=sys.stderr)
    return result


def create_notebook(target_date: str) -> str | None:
    """Create a NotebookLM notebook and return its ID."""
    result = nlm_run(['notebook', 'create', target_date])
    if result.returncode != 0:
        return None

    # Parse notebook ID from output
    try:
        data = json.loads(result.stdout)
        notebook_id = data.get('id') or data.get('notebook_id')
        if notebook_id:
            return notebook_id
    except (json.JSONDecodeError, TypeError):
        pass

    # Fallback: search by title in notebook list
    list_result = nlm_run(['notebook', 'list'])
    if list_result.returncode == 0:
        notebooks = json.loads(list_result.stdout)
        for nb in notebooks:
            if nb.get('title') == target_date:
                return nb['id']

    return None


def add_sources(notebook_id: str, sources: list[dict], delay: float = 1.0) -> tuple[int, int]:
    """Add URL sources to the notebook. Returns (success_count, fail_count)."""
    success = 0
    fail = 0

    for i, s in enumerate(sources):
        url = s['url']
        title = s['title'][:60]
        print(f"  [{i+1}/{len(sources)}] {title}...")

        result = nlm_run(['source', 'add', notebook_id, '--url', url], check=False)
        if result.returncode == 0:
            success += 1
        else:
            fail += 1
            print(f"    FAILED: {result.stderr.strip()[:100]}", file=sys.stderr)

        # Small delay to avoid rate limiting
        if i < len(sources) - 1:
            time.sleep(delay)

    return success, fail


def generate_audio(notebook_id: str, language: str = 'fr') -> bool:
    """Trigger audio podcast generation."""
    result = nlm_run(['audio', 'create', notebook_id, '--language', language, '--confirm'], check=False)
    return result.returncode == 0


def generate_video(notebook_id: str, language: str = 'fr', fmt: str = 'cinematic') -> bool:
    """Trigger video generation."""
    result = nlm_run(['video', 'create', notebook_id, '--format', fmt, '--language', language, '--confirm'], check=False)
    return result.returncode == 0


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else date.today().isoformat()
    dry_run = '--dry-run' in sys.argv
    with_audio = '--audio' in sys.argv
    with_video = '--video' in sys.argv

    print(f"Loading sources for {target}...")
    raw_sources = load_kept_sources(target)
    print(f"  Kept sources: {len(raw_sources)}")

    sources = filter_sources(raw_sources)
    print(f"  After filtering: {len(sources)}")

    # Group by theme for display
    by_theme = {}
    for s in sources:
        by_theme.setdefault(s['theme'], []).append(s)

    print("\nSources to add:")
    for theme, items in by_theme.items():
        print(f"\n  [{theme}] ({len(items)})")
        for s in items:
            print(f"    - {s['title'][:70]}")
            print(f"      {s['url']}")

    print(f"\nTotal: {len(sources)} sources")

    if dry_run:
        print("\n(dry run — no notebook created)")
        # Output JSON for inspection
        print(json.dumps({
            "date": target,
            "source_count": len(sources),
            "sources": [{"title": s["title"], "url": s["url"], "theme": s["theme"]} for s in sources],
        }, indent=2, ensure_ascii=False))
        return

    # Create notebook
    print(f"\nCreating notebook '{target}'...")
    notebook_id = create_notebook(target)
    if not notebook_id:
        print("Failed to create notebook.", file=sys.stderr)
        sys.exit(1)
    print(f"  Notebook ID: {notebook_id}")

    # Add sources
    print(f"\nAdding {len(sources)} sources...")
    success, fail = add_sources(notebook_id, sources)
    print(f"\n  Added: {success}, Failed: {fail}")

    # Generate audio
    if with_audio:
        print("\nGenerating podcast audio (fr)...")
        if generate_audio(notebook_id):
            print("  Audio generation started.")
        else:
            print("  Audio generation failed.", file=sys.stderr)

    # Generate video
    if with_video:
        print("\nGenerating cinematic video (fr)...")
        if generate_video(notebook_id):
            print("  Video generation started.")
        else:
            print("  Video generation failed.", file=sys.stderr)

    # Summary
    print(f"\nDone! Notebook '{target}' ({notebook_id})")
    print(f"  Sources: {success}/{len(sources)}")
    if with_audio:
        print("  Audio: generation in progress")
    if with_video:
        print("  Video: generation in progress")


if __name__ == '__main__':
    main()
