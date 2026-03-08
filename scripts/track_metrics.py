#!/usr/bin/env python3
"""
veilleur — Saisie et import des métriques LinkedIn.

Usage:
    python3 scripts/track_metrics.py 2026-03-07 --likes 42 --comments 8 --reposts 3
    python3 scripts/track_metrics.py 2026-03-07 --show
    python3 scripts/track_metrics.py --import-csv metrics.csv
    python3 scripts/track_metrics.py --list

Output: JSON sur stdout.
"""

import argparse
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from metrics_db import upsert_metrics, get_metrics, get_all_metrics
from index_article import parse_article


def resolve_article_metadata(date):
    """Résout le titre et les thèmes depuis le fichier article."""
    output_dir = Path(__file__).parent.parent / 'data' / 'output'
    filepath = output_dir / f"{date}-article.md"

    if filepath.exists():
        parsed = parse_article(filepath)
        return parsed['title'], parsed['themes']

    return 'Sans titre', 'Autre'


def get_latest_untracked_info(db_path=None, collection=None):
    """Retourne les infos du dernier article sans métriques, ou None."""
    from metrics_db import get_latest_without_metrics
    date = get_latest_without_metrics(db_path=db_path, collection=collection)
    if date:
        title, themes = resolve_article_metadata(date)
        return {"date": date, "title": title, "themes": themes}
    return {"date": None, "message": "Tous les articles ont des métriques"}


def import_csv(filepath):
    """Importe les métriques depuis un fichier CSV."""
    results = []
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = row['date']
            title, themes = resolve_article_metadata(date)
            result = upsert_metrics(
                date=date,
                title=title,
                themes=themes,
                likes=int(row.get('likes') or 0),
                comments=int(row.get('comments') or 0),
                reposts=int(row.get('reposts') or 0),
                impressions=int(row.get('impressions') or 0),
            )
            results.append(result)
    return {"imported": len(results), "results": results}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Saisie des métriques LinkedIn')
    parser.add_argument('date', nargs='?', help='Date de l\'article (YYYY-MM-DD)')
    parser.add_argument('--likes', type=int, default=None)
    parser.add_argument('--comments', type=int, default=None)
    parser.add_argument('--reposts', type=int, default=None)
    parser.add_argument('--impressions', type=int, default=None)
    parser.add_argument('--show', action='store_true', help='Afficher les métriques existantes')
    parser.add_argument('--list', action='store_true', help='Lister les métriques récentes')
    parser.add_argument('--import-csv', type=str, help='Importer depuis un CSV')
    parser.add_argument('--latest-untracked', action='store_true',
                        help='JSON du dernier article sans métriques (date, title, themes)')
    args = parser.parse_args()

    if args.latest_untracked:
        result = get_latest_untracked_info()
    elif args.import_csv:
        result = import_csv(args.import_csv)
    elif args.list:
        result = get_all_metrics()
    elif args.date and args.show:
        result = get_metrics(args.date)
        if result is None:
            result = {"error": f"Aucune métrique pour {args.date}"}
    elif args.date:
        title, themes = resolve_article_metadata(args.date)
        # Merge with existing values to avoid overwriting with 0
        existing = get_metrics(args.date)
        result = upsert_metrics(
            date=args.date,
            title=title,
            themes=themes,
            likes=args.likes if args.likes is not None else (existing or {}).get('likes', 0),
            comments=args.comments if args.comments is not None else (existing or {}).get('comments', 0),
            reposts=args.reposts if args.reposts is not None else (existing or {}).get('reposts', 0),
            impressions=args.impressions if args.impressions is not None else (existing or {}).get('impressions', 0),
        )
    else:
        parser.print_help()
        sys.exit(1)

    print(json.dumps(result, indent=2, ensure_ascii=False))
