#!/usr/bin/env python3
"""
veilleur — Index an article into ChromaDB.

Usage:
    python3 scripts/index_article.py 2026-03-07
    python3 scripts/index_article.py  # defaults to today's date

Output: JSON on stdout confirming the indexing.
"""

import json
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from load_sources import detect_theme

DEFAULT_PERSIST_DIR = Path(__file__).parent.parent / 'data' / 'chromadb'
COLLECTION_NAME = 'articles'


def parse_article(filepath):
    """Parse a markdown article file into structured data."""
    text = filepath.read_text(encoding='utf-8')
    lines = text.strip().split('\n')

    # Title: first line starting with #
    title = 'Sans titre'
    for line in lines:
        if line.startswith('# '):
            title = line.lstrip('# ').strip()
            break

    # Body: all text before "## Sources"
    body = text
    sources_idx = text.find('\n## Sources')
    if sources_idx != -1:
        body = text[:sources_idx].strip()

    # Themes: detect on each section (separated by **bold**)
    sections = re.split(r'\n\*\*[^*]+\*\*\n', body)
    themes = set()
    for section in sections:
        theme = detect_theme(title, section)
        if theme != 'Autre':
            themes.add(theme)
    if not themes:
        themes.add(detect_theme(title, body))

    # Source count: count references [[N](url)]
    source_count = len(set(re.findall(r'\[\[\d+\]', text)))

    # Word count
    word_count = len(body.split())

    return {
        'title': title,
        'body': body,
        'themes': ','.join(sorted(themes)),
        'source_count': source_count,
        'word_count': word_count,
    }


def get_collection(persist_directory=None):
    """Return the ChromaDB 'articles' collection."""
    import chromadb

    persist_dir = str(persist_directory or DEFAULT_PERSIST_DIR)
    client = chromadb.PersistentClient(path=persist_dir)
    return client.get_or_create_collection(name=COLLECTION_NAME)


def index_article(target_date, persist_directory=None, output_directory=None):
    """Index an article by date. Idempotent via upsert on ID = date."""
    output_dir = output_directory or Path(__file__).parent.parent / 'data' / 'output'
    filepath = output_dir / f"{target_date}-article.md"

    if not filepath.exists():
        return {"error": f"Fichier non trouvé: {filepath.name}", "date": target_date}

    parsed = parse_article(filepath)

    collection = get_collection(persist_directory)
    collection.upsert(
        ids=[target_date],
        documents=[parsed['body']],
        metadatas=[{
            'date': target_date,
            'title': parsed['title'],
            'themes': parsed['themes'],
            'source_count': parsed['source_count'],
            'word_count': parsed['word_count'],
        }],
    )

    return {
        "status": "indexed",
        "date": target_date,
        "title": parsed['title'],
        "themes": parsed['themes'],
        "word_count": parsed['word_count'],
        "source_count": parsed['source_count'],
    }


if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else date.today().isoformat()
    result = index_article(target)
    print(json.dumps(result, indent=2, ensure_ascii=False))
