#!/usr/bin/env python3
"""
veilleur — Recherche sémantique dans l'historique des articles.

Usage:
    python3 scripts/search_history.py "query" [--limit N]

Output: JSON sur stdout avec les résultats de recherche.
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from index_article import get_collection


def search_articles(query, limit=5, persist_directory=None):
    """Recherche sémantique dans les articles indexés."""
    collection = get_collection(persist_directory)
    total = collection.count()

    if total == 0 or limit <= 0:
        return {"query": query, "results": [], "total_indexed": total}

    results = collection.query(
        query_texts=[query],
        n_results=min(limit, total),
        include=['documents', 'metadatas', 'distances'],
    )

    formatted = []
    for i in range(len(results['ids'][0])):
        metadata = results['metadatas'][0][i]
        distance = results['distances'][0][i]
        document = results['documents'][0][i]

        formatted.append({
            "date": metadata['date'],
            "title": metadata['title'],
            "relevance": round(1 / (1 + distance), 3),
            "themes": metadata['themes'],
            "excerpt": document[:200] + "..." if len(document) > 200 else document,
        })

    return {
        "query": query,
        "results": formatted,
        "total_indexed": total,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Recherche dans les articles')
    parser.add_argument('query', help='Requête de recherche')
    parser.add_argument('--limit', type=int, default=5, help='Nombre max de résultats')
    args = parser.parse_args()

    result = search_articles(args.query, limit=args.limit)
    print(json.dumps(result, indent=2, ensure_ascii=False))
