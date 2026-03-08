#!/usr/bin/env python3
"""
veilleur — Index all existing articles into ChromaDB.

Usage:
    python3 scripts/index_all.py

Output: JSON on stdout with an indexing summary.
"""

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from index_article import index_article


def index_all():
    """Index all existing articles in data/output/."""
    output_dir = Path(__file__).parent.parent / 'data' / 'output'

    if not output_dir.exists():
        return {"error": "Dossier data/output/ introuvable", "indexed": [], "errors": []}

    files = sorted(output_dir.glob('*-article.md'))
    indexed = []
    errors = []

    for filepath in files:
        match = re.match(r'(\d{4}-\d{2}-\d{2})-article\.md', filepath.name)
        if not match:
            continue

        target_date = match.group(1)
        result = index_article(target_date)

        if 'error' in result:
            errors.append(result)
        else:
            indexed.append(result)

    return {
        "total": len(indexed) + len(errors),
        "indexed": indexed,
        "errors": errors,
    }


if __name__ == '__main__':
    result = index_all()
    print(json.dumps(result, indent=2, ensure_ascii=False))
