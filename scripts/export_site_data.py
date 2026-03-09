#!/usr/bin/env python3
"""
veilleur — Export ChromaDB + SQLite data to JSON for the Astro site.

Outputs:
  site/src/data/articles-meta.json   — article metadata from ChromaDB
  site/src/data/metrics.json         — engagement metrics from SQLite
  site/src/data/themes-over-time.json — theme aggregation by month

Usage:
    python3 scripts/export_site_data.py
"""

import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent.parent
OUTPUT_DIR = ROOT / 'site' / 'src' / 'data'
CHROMADB_DIR = ROOT / 'data' / 'chromadb'
METRICS_DB = ROOT / 'data' / 'metrics.db'


def export_articles_meta():
    """Export article metadata from ChromaDB."""
    try:
        import chromadb
    except ImportError:
        print("chromadb not installed, skipping articles-meta export", file=sys.stderr)
        return []

    if not CHROMADB_DIR.exists():
        print("ChromaDB directory not found, skipping articles-meta export", file=sys.stderr)
        return []

    client = chromadb.PersistentClient(path=str(CHROMADB_DIR))
    try:
        collection = client.get_collection('articles')
    except Exception:
        print("ChromaDB collection 'articles' not found", file=sys.stderr)
        return []

    if collection.count() == 0:
        return []

    result = collection.get(include=['metadatas'])
    articles = []
    for meta in result['metadatas']:
        articles.append({
            'date': meta.get('date', ''),
            'title': meta.get('title', ''),
            'themes': [t.strip() for t in meta.get('themes', '').split(',') if t.strip()],
            'word_count': meta.get('word_count', 0),
            'source_count': meta.get('source_count', 0),
        })

    articles.sort(key=lambda a: a['date'], reverse=True)
    return articles


def export_metrics():
    """Export engagement metrics from SQLite."""
    if not METRICS_DB.exists():
        print("metrics.db not found, skipping metrics export", file=sys.stderr)
        return []

    import sqlite3
    conn = sqlite3.connect(str(METRICS_DB))
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "SELECT date, title, themes, likes, comments, reposts, impressions FROM metrics ORDER BY date DESC"
    ).fetchall()
    conn.close()

    metrics = []
    for row in rows:
        d = dict(row)
        d['themes'] = [t.strip() for t in d.get('themes', '').split(',') if t.strip()]
        d['score'] = d['likes'] + d['comments'] * 3 + d['reposts'] * 2
        metrics.append(d)

    return metrics


def export_themes_over_time(articles_meta):
    """Aggregate theme occurrences by month.

    Returns a dict keyed by theme, where each value is a dict of month → count.
    Format: { "IA": { "2026-03": 5, "2026-04": 3 }, "Leadership": { ... } }
    """
    by_theme: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))

    for article in articles_meta:
        date = article.get('date', '')
        if len(date) >= 7:
            month = date[:7]  # YYYY-MM
            for theme in article.get('themes', []):
                by_theme[theme][month] += 1

    return {theme: dict(sorted(months.items())) for theme, months in by_theme.items()}


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Exporting articles metadata from ChromaDB...")
    articles = export_articles_meta()
    (OUTPUT_DIR / 'articles-meta.json').write_text(
        json.dumps(articles, indent=2, ensure_ascii=False), encoding='utf-8'
    )
    print(f"  → {len(articles)} articles exported")

    print("Exporting metrics from SQLite...")
    metrics = export_metrics()
    (OUTPUT_DIR / 'metrics.json').write_text(
        json.dumps(metrics, indent=2, ensure_ascii=False), encoding='utf-8'
    )
    print(f"  → {len(metrics)} metrics entries exported")

    print("Aggregating themes over time...")
    themes = export_themes_over_time(articles)
    (OUTPUT_DIR / 'themes-over-time.json').write_text(
        json.dumps(themes, indent=2, ensure_ascii=False), encoding='utf-8'
    )
    print(f"  → {len(themes)} themes exported")

    print(f"\nDone. Data written to {OUTPUT_DIR}/")


if __name__ == '__main__':
    main()
