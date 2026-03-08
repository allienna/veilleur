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
                likes=int(row.get('likes', 0)),
                comments=int(row.get('comments', 0)),
                reposts=int(row.get('reposts', 0)),
                impressions=int(row.get('impressions', 0)),
            )
            results.append(result)
    return {"imported": len(results), "results": results}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Saisie des métriques LinkedIn')
    parser.add_argument('date', nargs='?', help='Date de l\'article (YYYY-MM-DD)')
    parser.add_argument('--likes', type=int, default=0)
    parser.add_argument('--comments', type=int, default=0)
    parser.add_argument('--reposts', type=int, default=0)
    parser.add_argument('--impressions', type=int, default=0)
    parser.add_argument('--show', action='store_true', help='Afficher les métriques existantes')
    parser.add_argument('--list', action='store_true', help='Lister les métriques récentes')
    parser.add_argument('--import-csv', type=str, help='Importer depuis un CSV')
    args = parser.parse_args()

    if args.import_csv:
        result = import_csv(args.import_csv)
    elif args.list:
        result = get_all_metrics()
    elif args.date and args.show:
        result = get_metrics(args.date)
        if result is None:
            result = {"error": f"Aucune métrique pour {args.date}"}
    elif args.date:
        title, themes = resolve_article_metadata(args.date)
        result = upsert_metrics(
            date=args.date,
            title=title,
            themes=themes,
            likes=args.likes,
            comments=args.comments,
            reposts=args.reposts,
            impressions=args.impressions,
        )
    else:
        parser.print_help()
        sys.exit(1)

    print(json.dumps(result, indent=2, ensure_ascii=False))
