#!/usr/bin/env python3
"""Unit tests for metrics_db.py."""

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from metrics_db import get_db, upsert_metrics, get_metrics, get_all_metrics


class TestMetricsDb(unittest.TestCase):
    """Tests for metrics database layer."""

    def setUp(self):
        self.tmpdir = Path(tempfile.mkdtemp())
        self.db_path = self.tmpdir / 'test_metrics.db'

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def test_create_table_idempotent(self):
        conn1 = get_db(self.db_path)
        conn1.close()
        conn2 = get_db(self.db_path)
        conn2.close()
        # No error means idempotent

    def test_upsert_creates_row(self):
        result = upsert_metrics(
            '2099-01-01', 'Test Article', 'IA',
            likes=10, comments=2, reposts=1,
            db_path=self.db_path,
        )
        self.assertEqual(result['status'], 'created')
        self.assertEqual(result['likes'], 10)

    def test_upsert_updates_existing(self):
        upsert_metrics('2099-01-01', 'Test', 'IA', likes=10, db_path=self.db_path)
        result = upsert_metrics('2099-01-01', 'Test', 'IA', likes=20, db_path=self.db_path)
        self.assertEqual(result['status'], 'updated')
        self.assertEqual(result['likes'], 20)

        stored = get_metrics('2099-01-01', db_path=self.db_path)
        self.assertEqual(stored['likes'], 20)

    def test_get_metrics_returns_none_for_missing(self):
        result = get_metrics('2099-12-31', db_path=self.db_path)
        self.assertIsNone(result)

    def test_get_all_metrics_ordered_by_date(self):
        upsert_metrics('2099-01-01', 'A', 'IA', likes=5, db_path=self.db_path)
        upsert_metrics('2099-01-03', 'C', 'Data', likes=15, db_path=self.db_path)
        upsert_metrics('2099-01-02', 'B', 'Leadership', likes=10, db_path=self.db_path)

        results = get_all_metrics(db_path=self.db_path)
        dates = [r['date'] for r in results]
        self.assertEqual(dates, ['2099-01-03', '2099-01-02', '2099-01-01'])

    def test_get_all_metrics_respects_limit(self):
        for i in range(5):
            upsert_metrics(f'2099-01-0{i+1}', f'Art {i}', 'IA', db_path=self.db_path)

        results = get_all_metrics(limit=3, db_path=self.db_path)
        self.assertEqual(len(results), 3)

    def test_upsert_sets_recorded_at(self):
        upsert_metrics('2099-01-01', 'Test', 'IA', db_path=self.db_path)
        stored = get_metrics('2099-01-01', db_path=self.db_path)
        self.assertIsNotNone(stored['recorded_at'])

    def test_upsert_update_sets_updated_at(self):
        upsert_metrics('2099-01-01', 'Test', 'IA', likes=1, db_path=self.db_path)
        upsert_metrics('2099-01-01', 'Test', 'IA', likes=2, db_path=self.db_path)
        stored = get_metrics('2099-01-01', db_path=self.db_path)
        self.assertIsNotNone(stored['updated_at'])


class TestTrackMetricsCsv(unittest.TestCase):
    """Tests for CSV import functionality."""

    def setUp(self):
        self.tmpdir = Path(tempfile.mkdtemp())
        self.db_path = self.tmpdir / 'test_metrics.db'

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def test_csv_import(self):
        csv_path = self.tmpdir / 'test.csv'
        csv_path.write_text(
            'date,likes,comments,reposts,impressions\n'
            '2099-01-01,10,2,1,500\n'
            '2099-01-02,20,5,3,1000\n',
            encoding='utf-8',
        )

        # Import CSV using track_metrics import function
        # We need to patch db_path since import_csv uses default
        from unittest.mock import patch
        import metrics_db

        with patch.object(metrics_db, 'DEFAULT_DB_PATH', self.db_path):
            from track_metrics import import_csv
            result = import_csv(str(csv_path))

        self.assertEqual(result['imported'], 2)


if __name__ == '__main__':
    unittest.main()
