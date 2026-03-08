#!/usr/bin/env python3
"""Integration tests for detect_trends.py with synthetic multi-newsletter data."""

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from detect_trends import detect_trends


def make_newsletter(name, links):
    """Build a newsletter JSON structure."""
    return {
        "newsletter": name,
        "from": "test@example.com",
        "received_at": "2099-01-01T08:00:00Z",
        "links": links,
    }


def make_link(url, title, content=""):
    """Build a link entry with enough content to pass the MIN_CONTENT_LENGTH filter."""
    if not content:
        content = f"Article about {title}. " * 60  # ~600+ chars
    return {"url": url, "title": title, "content": content, "scraped": True}


class TestDetectTrendsIntegration(unittest.TestCase):
    """End-to-end tests using temporary newsletter files on disk."""

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        self.test_date = "2099-01-01"

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmpdir)

    def _write_newsletter(self, number, newsletter):
        filename = f"{self.test_date}-newsletter-{number:02d}.json"
        filepath = os.path.join(self.tmpdir, filename)
        with open(filepath, 'w') as f:
            json.dump(newsletter, f)
        return filepath

    def _run(self):
        """Run detect_trends with glob patched to read from our temp directory."""
        import glob as real_glob
        original_glob = real_glob.glob

        def patched_glob(pattern, **kwargs):
            filename_pattern = os.path.basename(pattern)
            return sorted(original_glob(os.path.join(self.tmpdir, filename_pattern), **kwargs))

        with patch('detect_trends.globmod.glob', side_effect=patched_glob):
            return detect_trends(self.test_date)

    def test_single_newsletter_no_trends(self):
        """Single newsletter should produce no trends."""
        self._write_newsletter(1, make_newsletter("Newsletter A", [
            make_link("https://example.com/article1", "Introduction to Kubernetes"),
            make_link("https://example.com/article2", "GPT-5 launched today"),
            make_link("https://example.com/article3", "React Server Components guide"),
        ]))

        result = self._run()
        self.assertEqual(result['trends'], [])
        self.assertEqual(result['newsletters_count'], 1)
        self.assertGreater(len(result['unclustered']), 0)

    def test_url_match_creates_trend(self):
        """Same URL in two newsletters should create a trend with high score."""
        shared_url = "https://openai.com/blog/gpt5-launch"

        self._write_newsletter(1, make_newsletter("TLDR AI", [
            make_link(shared_url, "OpenAI launches GPT-5"),
            make_link("https://example.com/unrelated1", "Rust async patterns"),
        ]))
        self._write_newsletter(2, make_newsletter("The Batch", [
            make_link(shared_url, "GPT-5 is here"),
            make_link("https://example.com/unrelated2", "PostgreSQL 17 features"),
        ]))

        result = self._run()
        self.assertEqual(len(result['trends']), 1)
        trend = result['trends'][0]
        self.assertGreaterEqual(trend['score'], 0.5)
        self.assertEqual(len(trend['newsletters']), 2)
        self.assertIn('TLDR AI', trend['newsletters'])
        self.assertIn('The Batch', trend['newsletters'])

    def test_url_match_with_utm_params(self):
        """Same URL with different UTM params should still match."""
        self._write_newsletter(1, make_newsletter("NL-A", [
            make_link("https://example.com/ai-article?utm_source=nla&utm_medium=email", "AI breakthrough"),
        ]))
        self._write_newsletter(2, make_newsletter("NL-B", [
            make_link("https://example.com/ai-article?utm_source=nlb&utm_campaign=weekly", "AI breakthrough"),
        ]))

        result = self._run()
        self.assertEqual(len(result['trends']), 1)
        self.assertGreaterEqual(result['trends'][0]['score'], 0.5)

    def test_title_similarity_creates_trend(self):
        """Similar titles across newsletters should create a trend."""
        self._write_newsletter(1, make_newsletter("NL-A", [
            make_link("https://site-a.com/post1", "GPT-5 launched with new capabilities today"),
        ]))
        self._write_newsletter(2, make_newsletter("NL-B", [
            make_link("https://site-b.com/post2", "GPT-5 new capabilities launched by OpenAI"),
        ]))

        result = self._run()
        self.assertEqual(len(result['trends']), 1)
        self.assertGreater(result['trends'][0]['score'], 0.0)

    def test_different_topics_no_trend(self):
        """Completely different topics should not cluster."""
        self._write_newsletter(1, make_newsletter("NL-A", [
            make_link("https://a.com/kubernetes", "Kubernetes scaling best practices for production"),
        ]))
        self._write_newsletter(2, make_newsletter("NL-B", [
            make_link("https://b.com/cooking", "French pastry techniques and recipes masterclass"),
        ]))

        result = self._run()
        self.assertEqual(len(result['trends']), 0)
        self.assertEqual(len(result['unclustered']), 2)

    def test_multiple_clusters(self):
        """Multiple distinct topics shared across newsletters should form separate clusters."""
        self._write_newsletter(1, make_newsletter("NL-A", [
            make_link("https://shared.com/gpt5", "GPT-5 launch announcement details"),
            make_link("https://shared.com/rust2", "Rust 2.0 release announcement today"),
            make_link("https://a.com/only-a", "French pastry baking techniques",
                       "Learn how to bake croissants and pain au chocolat. " * 60),
        ]))
        self._write_newsletter(2, make_newsletter("NL-B", [
            make_link("https://shared.com/gpt5", "GPT-5 launch announcement details"),
            make_link("https://shared.com/rust2", "Rust 2.0 release announcement today"),
            make_link("https://b.com/only-b", "Marine biology coral reef study",
                       "Scientists discovered new coral species in the Pacific Ocean. " * 60),
        ]))

        result = self._run()
        # shared URLs create trends
        self.assertGreaterEqual(len(result['trends']), 1)
        # Verify total sources accounted for (trends + unclustered)
        trend_source_count = sum(len(t['sources']) for t in result['trends'])
        total = trend_source_count + len(result['unclustered'])
        self.assertEqual(total, result['sources_analyzed'])

    def test_no_sources_returns_empty(self):
        """No files for the date should return empty structure."""
        result = self._run()
        self.assertEqual(result['sources_analyzed'], 0)
        self.assertEqual(result['trends'], [])
        self.assertEqual(result['unclustered'], [])

    def test_output_structure(self):
        """Verify all expected fields are present in output."""
        self._write_newsletter(1, make_newsletter("NL-A", [
            make_link("https://shared.com/article", "Shared article about AI models"),
        ]))
        self._write_newsletter(2, make_newsletter("NL-B", [
            make_link("https://shared.com/article", "Shared article about AI models"),
        ]))

        result = self._run()

        # Top-level fields
        self.assertIn('date', result)
        self.assertIn('sources_analyzed', result)
        self.assertIn('newsletters_count', result)
        self.assertIn('trends', result)
        self.assertIn('unclustered', result)
        self.assertEqual(result['date'], self.test_date)

        # Trend fields
        if result['trends']:
            trend = result['trends'][0]
            self.assertIn('id', trend)
            self.assertIn('label', trend)
            self.assertIn('theme', trend)
            self.assertIn('score', trend)
            self.assertIn('newsletters', trend)
            self.assertIn('sources', trend)

            # Trend source fields
            src = trend['sources'][0]
            self.assertIn('index', src)
            self.assertIn('title', src)
            self.assertIn('newsletter', src)
            self.assertIn('trend_score', src)

    def test_trend_scores_sorted_descending(self):
        """Trends should be sorted by score, highest first."""
        # Create a strong URL match and a weaker title-only match
        self._write_newsletter(1, make_newsletter("NL-A", [
            make_link("https://shared.com/exact", "Exact URL match article about testing"),
            make_link("https://a.com/similar1", "GPT-5 launched with amazing capabilities"),
        ]))
        self._write_newsletter(2, make_newsletter("NL-B", [
            make_link("https://shared.com/exact", "Exact URL match article about testing"),
            make_link("https://b.com/similar2", "GPT-5 amazing capabilities launched today"),
        ]))

        result = self._run()
        if len(result['trends']) >= 2:
            scores = [t['score'] for t in result['trends']]
            self.assertEqual(scores, sorted(scores, reverse=True))

    def test_three_newsletters(self):
        """Trend spanning 3 newsletters should work correctly."""
        shared_url = "https://example.com/big-news"

        self._write_newsletter(1, make_newsletter("NL-A", [
            make_link(shared_url, "Big news article"),
        ]))
        self._write_newsletter(2, make_newsletter("NL-B", [
            make_link(shared_url, "Big news article"),
        ]))
        self._write_newsletter(3, make_newsletter("NL-C", [
            make_link(shared_url, "Big news article"),
        ]))

        result = self._run()
        self.assertEqual(result['newsletters_count'], 3)
        self.assertEqual(len(result['trends']), 1)
        self.assertEqual(len(result['trends'][0]['newsletters']), 3)
        self.assertEqual(len(result['trends'][0]['sources']), 3)


if __name__ == '__main__':
    unittest.main()
