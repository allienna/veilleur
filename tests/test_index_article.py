#!/usr/bin/env python3
"""Unit and integration tests for index_article.py."""

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from index_article import parse_article, index_article, get_collection

SAMPLE_ARTICLE = """\
# L'IA ne remplace pas les bons fondamentaux

Et si le vrai avantage compétitif n'était pas de maîtriser l'IA ?

**L'IA comme amplificateur**

Sean Goedecke a publié un retour d'expérience sur les LLM [[1](https://example.com/llm)].

**Travailler ensemble, autrement**

PostHog a partagé sa recette du travail asynchrone [[2](https://example.com/async)].

**Mesurer ce qui compte**

LinkedIn a open-sourcé son Developer Productivity Framework [[3](https://example.com/dph)].

---

## Sources

1. [How I use LLMs](https://example.com/llm)
2. [Async work](https://example.com/async)
3. [DPH Framework](https://example.com/dph)

## Pour aller plus loin

- [Extra resource](https://example.com/extra)

---

*Disclaimer text.*
"""

MINIMAL_ARTICLE = """\
# Un titre simple

Un seul paragraphe sans section ni source.
"""

LEADERSHIP_ARTICLE = """\
# Leadership et management en remote

Comment gérer une équipe distribuée efficacement.

**Le rôle du engineering manager**

Le leadership moderne nécessite de repenser le management [[1](https://example.com/lead)].

---

## Sources

1. [Remote leadership](https://example.com/lead)
"""


class TestParseArticle(unittest.TestCase):
    """Tests for parse_article()."""

    def setUp(self):
        self.tmpdir = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def _write(self, content, name="test-article.md"):
        filepath = self.tmpdir / name
        filepath.write_text(content, encoding='utf-8')
        return filepath

    def test_extracts_title(self):
        parsed = parse_article(self._write(SAMPLE_ARTICLE))
        self.assertEqual(parsed['title'], "L'IA ne remplace pas les bons fondamentaux")

    def test_extracts_themes_ia(self):
        parsed = parse_article(self._write(SAMPLE_ARTICLE))
        self.assertIn('IA', parsed['themes'])

    def test_extracts_themes_leadership(self):
        parsed = parse_article(self._write(LEADERSHIP_ARTICLE))
        self.assertIn('Leadership', parsed['themes'])

    def test_counts_sources(self):
        parsed = parse_article(self._write(SAMPLE_ARTICLE))
        self.assertEqual(parsed['source_count'], 3)

    def test_word_count_positive(self):
        parsed = parse_article(self._write(SAMPLE_ARTICLE))
        self.assertGreater(parsed['word_count'], 0)

    def test_body_excludes_sources_section(self):
        parsed = parse_article(self._write(SAMPLE_ARTICLE))
        self.assertNotIn('## Sources', parsed['body'])

    def test_minimal_article(self):
        parsed = parse_article(self._write(MINIMAL_ARTICLE))
        self.assertEqual(parsed['title'], 'Un titre simple')
        self.assertGreater(parsed['word_count'], 0)

    def test_empty_file(self):
        parsed = parse_article(self._write(''))
        self.assertEqual(parsed['title'], 'Sans titre')
        self.assertEqual(parsed['source_count'], 0)

    def test_no_heading_uses_default_title(self):
        parsed = parse_article(self._write('Just some text without heading.'))
        self.assertEqual(parsed['title'], 'Sans titre')


class TestIndexArticle(unittest.TestCase):
    """Integration tests for index_article() with ChromaDB."""

    def setUp(self):
        self.tmpdir = Path(tempfile.mkdtemp())
        self.chromadir = Path(tempfile.mkdtemp())
        self.test_date = "2099-01-01"
        # Create data/output structure
        self.output_dir = self.tmpdir / 'data' / 'output'
        self.output_dir.mkdir(parents=True)

    def tearDown(self):
        shutil.rmtree(self.tmpdir)
        shutil.rmtree(self.chromadir)

    def _write_article(self, content, target_date=None):
        target_date = target_date or self.test_date
        filepath = self.output_dir / f"{target_date}-article.md"
        filepath.write_text(content, encoding='utf-8')

    def _index(self, target_date=None):
        """Run index_article with patched paths."""
        from unittest.mock import patch
        target_date = target_date or self.test_date
        with patch('index_article.Path') as mock_path:
            # Make Path(__file__).parent.parent resolve to our tmpdir
            mock_path.return_value = mock_path
            mock_path.__truediv__ = Path.__truediv__
            # Simpler: just patch the output dir lookup
        # Actually, let's patch at a higher level
        import index_article as mod
        original_parent = Path(mod.__file__).parent.parent
        output_path = self.output_dir / f"{target_date}-article.md"

        # Patch the output dir construction
        with patch.object(Path, '__truediv__', wraps=Path.__truediv__):
            # Direct approach: write file where the script expects it
            pass

        # Simplest approach: use the real function but copy file to expected location
        # and use persist_directory for ChromaDB isolation
        expected_dir = original_parent / 'data' / 'output'
        expected_file = expected_dir / f"{target_date}-article.md"

        expected_dir.mkdir(parents=True, exist_ok=True)
        expected_file.write_text(
            (self.output_dir / f"{target_date}-article.md").read_text(),
            encoding='utf-8'
        )

        try:
            return mod.index_article(target_date, persist_directory=self.chromadir)
        finally:
            expected_file.unlink(missing_ok=True)

    def test_index_creates_entry(self):
        self._write_article(SAMPLE_ARTICLE)
        result = self._index()
        self.assertEqual(result['status'], 'indexed')
        self.assertEqual(result['date'], self.test_date)

        collection = get_collection(self.chromadir)
        self.assertEqual(collection.count(), 1)

    def test_index_idempotent(self):
        self._write_article(SAMPLE_ARTICLE)
        self._index()
        self._index()

        collection = get_collection(self.chromadir)
        self.assertEqual(collection.count(), 1)

    def test_index_missing_file(self):
        import index_article as mod
        result = mod.index_article("2099-12-31", persist_directory=self.chromadir)
        self.assertIn('error', result)

    def test_index_metadata(self):
        self._write_article(SAMPLE_ARTICLE)
        self._index()

        collection = get_collection(self.chromadir)
        result = collection.get(ids=[self.test_date], include=['metadatas'])
        metadata = result['metadatas'][0]

        self.assertEqual(metadata['date'], self.test_date)
        self.assertIn('title', metadata)
        self.assertIn('themes', metadata)
        self.assertGreater(metadata['source_count'], 0)
        self.assertGreater(metadata['word_count'], 0)

    def test_index_updates_on_change(self):
        self._write_article(SAMPLE_ARTICLE)
        self._index()

        self._write_article(LEADERSHIP_ARTICLE)
        self._index()

        collection = get_collection(self.chromadir)
        self.assertEqual(collection.count(), 1)
        result = collection.get(ids=[self.test_date], include=['metadatas'])
        self.assertIn('Leadership', result['metadatas'][0]['themes'])


if __name__ == '__main__':
    unittest.main()
