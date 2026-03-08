#!/usr/bin/env python3
"""
veilleur — Read the full content of selected sources.

Usage:
    python3 scripts/read_content.py 2026-03-07 0 2 5 8
    # Reads the content of sources at indices 0, 2, 5, 8 (0-indexed)

Output: Markdown content of each source on stdout.
"""

import json
import glob
import sys
from pathlib import Path


def read_content(target_date: str, indices: list[int]) -> None:
    """Print the content of sources at the given indices."""
    data_dir = Path(__file__).parent.parent / 'data' / 'raw'
    pattern = str(data_dir / f"{target_date}-newsletter-*.json")
    files = sorted(glob.glob(pattern))

    if not files:
        print(f"Aucun fichier trouvé pour {target_date}", file=sys.stderr)
        sys.exit(1)

    # Load all links (same logic as load_sources, without filtering)
    all_links = []
    seen_urls = set()

    for filepath in files:
        with open(filepath, 'r') as f:
            data = json.load(f)

        for link in data.get('links', []):
            url = link.get('url', '')
            if url in seen_urls:
                continue
            seen_urls.add(url)
            all_links.append(link)

    for idx in indices:
        if idx < 0 or idx >= len(all_links):
            print(f"=== SOURCE {idx} === [INDEX INVALIDE]")
            continue

        link = all_links[idx]
        url = link.get('url', 'N/A')
        title = link.get('title', 'Sans titre')
        content = link.get('content', '[Pas de contenu scrapé]')

        print(f"=== SOURCE {idx} ===")
        print(f"URL: {url}")
        print(f"Title: {title}")
        print(f"Content length: {len(content)} chars")
        print()
        print(content[:3000])
        if len(content) > 3000:
            print(f"\n... [truncated, {len(content)} chars total]")
        print()


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python3 read_content.py DATE INDEX [INDEX ...]", file=sys.stderr)
        sys.exit(1)

    target = sys.argv[1]
    indices = [int(x) for x in sys.argv[2:]]
    read_content(target, indices)
