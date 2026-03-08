#!/usr/bin/env python3
"""Unit tests for metrics_insights.py."""

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from metrics_db import upsert_metrics
from metrics_insights import (
    compute_engagement_score,
    format_insights_for_generate,
    generate_insights,
    theme_performance,
    top_performing_articles,
)


class TestEngagementScore(unittest.TestCase):
    """Tests for compute_engagement_score."""

    def test_engagement_score_formula(self):
        # likes + comments*3 + reposts*5
        self.assertEqual(compute_engagement_score(likes=10, comments=2, reposts=1), 10 + 6 + 5)

    def test_engagement_score_defaults(self):
        self.assertEqual(compute_engagement_score(), 0)


class TestThemePerformance(unittest.TestCase):
    """Tests for theme_performance."""

    def setUp(self):
        self.tmpdir = Path(tempfile.mkdtemp())
        self.db_path = self.tmpdir / 'test_metrics.db'

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def _seed(self, date, title, themes, likes=10, comments=2, reposts=1):
        upsert_metrics(date, title, themes, likes=likes, comments=comments, reposts=reposts, db_path=self.db_path)

    def test_theme_performance_empty_db(self):
        result = theme_performance(db_path=self.db_path)
        self.assertEqual(result, [])

    def test_theme_performance_single_theme(self):
        self._seed('2099-01-01', 'Art 1', 'IA', likes=10, comments=2, reposts=1)
        self._seed('2099-01-02', 'Art 2', 'IA', likes=20, comments=4, reposts=2)

        result = theme_performance(db_path=self.db_path)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['theme'], 'IA')
        self.assertEqual(result[0]['total_articles'], 2)
        # Art1: 10+6+5=21, Art2: 20+12+10=42, avg=31.5
        self.assertEqual(result[0]['avg_engagement'], 31.5)

    def test_theme_performance_splits_multi_theme(self):
        self._seed('2099-01-01', 'Art 1', 'IA,Leadership', likes=10, comments=2, reposts=1)

        result = theme_performance(db_path=self.db_path)
        themes = [r['theme'] for r in result]
        self.assertIn('IA', themes)
        self.assertIn('Leadership', themes)

    def test_theme_performance_ordered_by_engagement(self):
        self._seed('2099-01-01', 'Low', 'Data', likes=1, comments=0, reposts=0)
        self._seed('2099-01-02', 'High', 'IA', likes=50, comments=10, reposts=5)

        result = theme_performance(db_path=self.db_path)
        self.assertEqual(result[0]['theme'], 'IA')
        self.assertEqual(result[1]['theme'], 'Data')


class TestTopPerformingArticles(unittest.TestCase):
    """Tests for top_performing_articles."""

    def setUp(self):
        self.tmpdir = Path(tempfile.mkdtemp())
        self.db_path = self.tmpdir / 'test_metrics.db'

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def _seed(self, date, title, themes, likes=10, comments=2, reposts=1):
        upsert_metrics(date, title, themes, likes=likes, comments=comments, reposts=reposts, db_path=self.db_path)

    def test_top_performing_articles(self):
        self._seed('2099-01-01', 'Low', 'IA', likes=1, comments=0, reposts=0)
        self._seed('2099-01-02', 'Mid', 'Data', likes=10, comments=2, reposts=1)
        self._seed('2099-01-03', 'High', 'Leadership', likes=50, comments=10, reposts=5)

        result = top_performing_articles(limit=2, db_path=self.db_path)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['title'], 'High')
        self.assertEqual(result[1]['title'], 'Mid')


class TestGenerateInsights(unittest.TestCase):
    """Tests for generate_insights."""

    def setUp(self):
        self.tmpdir = Path(tempfile.mkdtemp())
        self.db_path = self.tmpdir / 'test_metrics.db'

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def _seed(self, date, title, themes, likes=10, comments=2, reposts=1):
        upsert_metrics(date, title, themes, likes=likes, comments=comments, reposts=reposts, db_path=self.db_path)

    def test_generate_insights_empty_db(self):
        result = generate_insights(db_path=self.db_path)
        self.assertEqual(result['total_articles_tracked'], 0)
        self.assertEqual(result['theme_ranking'], [])
        self.assertEqual(result['recommendations'], [])

    def test_generate_insights_with_data(self):
        self._seed('2099-01-01', 'A1', 'IA', likes=10, comments=2, reposts=1)
        self._seed('2099-01-02', 'A2', 'IA', likes=20, comments=4, reposts=2)
        self._seed('2099-01-03', 'A3', 'Data', likes=5, comments=1, reposts=0)
        self._seed('2099-01-04', 'A4', 'Leadership', likes=30, comments=5, reposts=3)
        self._seed('2099-01-05', 'A5', 'IA', likes=15, comments=3, reposts=1)
        self._seed('2099-01-06', 'A6', 'Data', likes=8, comments=1, reposts=1)

        result = generate_insights(db_path=self.db_path)
        self.assertEqual(result['total_articles_tracked'], 6)
        self.assertGreater(len(result['theme_ranking']), 0)
        # Verify multipliers are present
        for t in result['theme_ranking']:
            self.assertIn('multiplier_vs_avg', t)

    def test_generate_insights_recommendations(self):
        # IA has high engagement, Data has very low
        self._seed('2099-01-01', 'A1', 'IA', likes=50, comments=10, reposts=5)
        self._seed('2099-01-02', 'A2', 'IA', likes=60, comments=12, reposts=6)
        self._seed('2099-01-03', 'A3', 'Data', likes=1, comments=0, reposts=0)
        self._seed('2099-01-04', 'A4', 'Data', likes=2, comments=0, reposts=0)

        result = generate_insights(db_path=self.db_path)
        # IA avg: (50+30+25=105, 60+36+30=126) -> 115.5
        # Data avg: (1, 2) -> 1.5
        # Overall avg: (105+126+1+2)/4 = 58.5
        # IA multiplier: 115.5/58.5 ≈ 2.0 -> should generate recommendation
        self.assertGreater(len(result['recommendations']), 0)
        has_ia_rec = any('IA' in r for r in result['recommendations'])
        self.assertTrue(has_ia_rec)

    def test_generate_insights_trend(self):
        # Seed 8 articles with recent ones having higher engagement
        for i in range(8):
            likes = 10 + i * 5 if i >= 4 else 5
            self._seed(f'2099-01-{i+1:02d}', f'Art {i}', 'IA', likes=likes, comments=1, reposts=0)

        result = generate_insights(db_path=self.db_path)
        self.assertIn('trend', result)
        self.assertIn(result['trend']['direction'], ['up', 'down', 'stable'])


class TestFormatInsightsForGenerate(unittest.TestCase):
    """Tests for format_insights_for_generate."""

    def setUp(self):
        self.tmpdir = Path(tempfile.mkdtemp())
        self.db_path = self.tmpdir / 'test_metrics.db'

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def _seed(self, date, title, themes, likes=10, comments=2, reposts=1):
        upsert_metrics(date, title, themes, likes=likes, comments=comments, reposts=reposts, db_path=self.db_path)

    def test_format_for_generate_empty(self):
        result = format_insights_for_generate(db_path=self.db_path)
        self.assertEqual(result, "")

    def test_format_for_generate_with_data(self):
        self._seed('2099-01-01', 'A1', 'IA', likes=10, comments=2, reposts=1)
        self._seed('2099-01-02', 'A2', 'Data', likes=20, comments=4, reposts=2)

        result = format_insights_for_generate(db_path=self.db_path)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertIn('Insights', result)
        self.assertIn('IA', result)


if __name__ == '__main__':
    unittest.main()
