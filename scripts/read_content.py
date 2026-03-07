#!/usr/bin/env python3
"""
veilleur — Lecture du contenu complet de sources sélectionnées.

Usage:
    python3 scripts/read_content.py 2026-03-07 0 2 5 8
    # Lit le contenu des sources aux indices 0, 2, 5, 8 (0-indexed)

Output: Contenu markdown de chaque source sur stdout.
"""

import json
import glob
import sys
from pathlib import Path


def read_content(target_date: str, indices: list[int]) -> None:
    """Affiche le contenu des sources aux indices donnés."""
    data_dir = Path(__file__).parent.parent / 'data' / 'raw'
    pattern = str(data_dir / f"{target_date}-newsletter-*.json")
    files = sorted(glob.glob(pattern))

    if not files:
        print(f"Aucun fichier trouvé pour {target_date}", file=sys.stderr)
        sys.exit(1)

    # Charger tous les liens (même logique que load_sources, sans filtrage)
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
            print(f"\n... [tronqué, {len(content)} chars au total]")
        print()


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python3 read_content.py DATE INDEX [INDEX ...]", file=sys.stderr)
        sys.exit(1)

    target = sys.argv[1]
    indices = [int(x) for x in sys.argv[2:]]
    read_content(target, indices)
