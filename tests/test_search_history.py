#!/usr/bin/env python3
"""Unit and integration tests for search_history.py."""

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from index_article import get_collection, parse_article
from search_history import search_articles

SAMPLE_ARTICLE = """\
# L'IA transforme le développement logiciel

L'intelligence artificielle change la façon dont nous codons.

**Les assistants de code**

GitHub Copilot et les LLM accélèrent le développement [[1](https://example.com/copilot)].

---

## Sources

1. [GitHub Copilot](https://example.com/copilot)
"""

SECOND_ARTICLE = """\
# Le leadership en entreprise tech

Comment diriger une équipe technique efficacement.

**Management moderne**

Le servant leadership gagne en popularité [[1](https://example.com/lead)].

---

## Sources

1. [Servant Leadership](https://example.com/lead)
"""


class TestSearchHistory(unittest.TestCase):
    """Integration tests for search_articles() with ChromaDB."""

    def setUp(self):
        self.tmpdir = Path(tempfile.mkdtemp())
        self.chromadir = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.tmpdir)
        shutil.rmtree(self.chromadir)

    def _index_article(self, content, date_str):
        """Index a sample article into ChromaDB for testing."""
        filepath = self.tmpdir / f"{date_str}-article.md"
        filepath.write_text(content, encoding='utf-8')
        parsed = parse_article(filepath)
        collection = get_collection(self.chromadir)
        collection.upsert(
            ids=[date_str],
            documents=[parsed['body']],
            metadatas=[{
                'date': date_str,
                'title': parsed['title'],
                'themes': parsed['themes'],
                'source_count': parsed['source_count'],
                'word_count': parsed['word_count'],
            }],
        )

    def test_search_empty_collection(self):
        result = search_articles("intelligence artificielle", persist_directory=self.chromadir)
        self.assertEqual(result['results'], [])
        self.assertEqual(result['total_indexed'], 0)
        self.assertEqual(result['query'], "intelligence artificielle")

    def test_search_returns_results(self):
        self._index_article(SAMPLE_ARTICLE, "2099-01-01")
        result = search_articles("intelligence artificielle", persist_directory=self.chromadir)
        self.assertGreater(len(result['results']), 0)
        first = result['results'][0]
        self.assertIn('date', first)
        self.assertIn('title', first)
        self.assertIn('relevance', first)
        self.assertIn('themes', first)
        self.assertIn('excerpt', first)

    def test_search_relevance_score(self):
        self._index_article(SAMPLE_ARTICLE, "2099-01-01")
        result = search_articles("GitHub Copilot", persist_directory=self.chromadir)
        for r in result['results']:
            self.assertGreaterEqual(r['relevance'], 0)
            self.assertLessEqual(r['relevance'], 1)

    def test_search_limit(self):
        self._index_article(SAMPLE_ARTICLE, "2099-01-01")
        self._index_article(SECOND_ARTICLE, "2099-01-02")
        result = search_articles("développement", limit=1, persist_directory=self.chromadir)
        self.assertEqual(len(result['results']), 1)
        self.assertEqual(result['total_indexed'], 2)

    def test_search_result_structure(self):
        self._index_article(SAMPLE_ARTICLE, "2099-01-01")
        result = search_articles("IA", persist_directory=self.chromadir)
        expected_keys = {'date', 'title', 'relevance', 'themes', 'excerpt'}
        for r in result['results']:
            self.assertEqual(set(r.keys()), expected_keys)


if __name__ == '__main__':
    unittest.main()
