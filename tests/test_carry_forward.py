#!/usr/bin/env python3
"""Tests for carry-forward feature: late-arriving newsletters inclusion."""

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from load_sources import gather_raw_files, load_sources
from detect_trends import extract_publisher
from save_processed_files import save_manifest


def _make_newsletter(tmp_path, filename, newsletter_name, links):
    """Helper to create a newsletter JSON file."""
    raw_dir = tmp_path / 'data' / 'raw'
    raw_dir.mkdir(parents=True, exist_ok=True)
    data = {
        "newsletter": newsletter_name,
        "received_at": "2026-03-09T08:00:00Z",
        "links": links,
    }
    path = raw_dir / filename
    path.write_text(json.dumps(data))
    return str(path)


def _make_manifest(tmp_path, date, files):
    """Helper to create a processed files manifest."""
    output_dir = tmp_path / 'data' / 'output'
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest = {"date": date, "generated_at": "2026-03-09T20:00:00Z", "files": files}
    path = output_dir / f"{date}-processed-files.json"
    path.write_text(json.dumps(manifest))
    return path


def _make_link(url, title="Test Article", content_length=600):
    """Helper to create a link dict with enough content to pass filtering."""
    return {
        "url": url,
        "title": title,
        "content": f"This is a test article about {title}. " * (content_length // 40),
    }


def _patch_paths(tmp_path):
    """Context manager to redirect gather_raw_files paths to tmp_path."""
    return patch.multiple(
        'load_sources',
        __file__=str(tmp_path / 'scripts' / 'load_sources.py'),
    )


class TestGatherRawFiles(unittest.TestCase):
    """Tests for gather_raw_files using actual function with patched paths."""

    def test_no_carryforward_uses_only_target_date(self):
        """gather_raw_files(date, 0) only returns files for that date."""
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            _make_newsletter(tmp_path, "2026-03-10-newsletter-a.json", "A", [])
            _make_newsletter(tmp_path, "2026-03-09-newsletter-b.json", "B", [])

            with _patch_paths(tmp_path):
                result = gather_raw_files("2026-03-10", carry_forward_days=0)

            names = [Path(f).name for f in result]
            self.assertEqual(names, ["2026-03-10-newsletter-a.json"])

    def test_carryforward_includes_late_files(self):
        """Unprocessed files from previous day are carried forward."""
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            _make_newsletter(tmp_path, "2026-03-10-newsletter-a.json", "A", [])
            _make_newsletter(tmp_path, "2026-03-09-newsletter-b.json", "B", [])
            _make_newsletter(tmp_path, "2026-03-09-newsletter-c-2100.json", "C", [])
            _make_manifest(tmp_path, "2026-03-09", ["2026-03-09-newsletter-b.json"])

            with _patch_paths(tmp_path):
                result = gather_raw_files("2026-03-10", carry_forward_days=1)

            names = [Path(f).name for f in result]
            # Carry-forward comes first, then current day
            self.assertEqual(names[0], "2026-03-09-newsletter-c-2100.json")
            self.assertIn("2026-03-10-newsletter-a.json", names)

    def test_carryforward_no_manifest_skips(self):
        """Without manifest, previous day files are not carried forward."""
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            _make_newsletter(tmp_path, "2026-03-10-newsletter-a.json", "A", [])
            _make_newsletter(tmp_path, "2026-03-09-newsletter-b.json", "B", [])

            with _patch_paths(tmp_path):
                result = gather_raw_files("2026-03-10", carry_forward_days=1)

            names = [Path(f).name for f in result]
            self.assertEqual(names, ["2026-03-10-newsletter-a.json"])

    def test_carryforward_all_processed_skips(self):
        """When all previous files are in the manifest, nothing is carried forward."""
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            _make_newsletter(tmp_path, "2026-03-10-newsletter-a.json", "A", [])
            _make_newsletter(tmp_path, "2026-03-09-newsletter-b.json", "B", [])
            _make_manifest(tmp_path, "2026-03-09", ["2026-03-09-newsletter-b.json"])

            with _patch_paths(tmp_path):
                result = gather_raw_files("2026-03-10", carry_forward_days=1)

            names = [Path(f).name for f in result]
            self.assertEqual(names, ["2026-03-10-newsletter-a.json"])

    def test_carryforward_multiple_days(self):
        """Carry-forward looks back multiple days."""
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            _make_newsletter(tmp_path, "2026-03-10-newsletter-a.json", "A", [])
            _make_newsletter(tmp_path, "2026-03-08-newsletter-old.json", "Old", [])
            _make_manifest(tmp_path, "2026-03-08", [])  # Empty manifest = all files are late

            with _patch_paths(tmp_path):
                result = gather_raw_files("2026-03-10", carry_forward_days=3)

            names = [Path(f).name for f in result]
            self.assertIn("2026-03-08-newsletter-old.json", names)

    def test_carryforward_already_processed_by_later_day(self):
        """A file carried forward and processed by day X should not be carried again on day X+1."""
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            _make_newsletter(tmp_path, "2026-03-11-newsletter-a.json", "A", [])
            _make_newsletter(tmp_path, "2026-03-09-newsletter-b.json", "B", [])
            _make_newsletter(tmp_path, "2026-03-09-newsletter-late.json", "Late", [])
            # Day 09 manifest: only b was processed
            _make_manifest(tmp_path, "2026-03-09", ["2026-03-09-newsletter-b.json"])
            # Day 10 manifest: late was carried forward and processed
            _make_manifest(tmp_path, "2026-03-10", [
                "2026-03-10-newsletter-x.json",
                "2026-03-09-newsletter-late.json",
            ])

            with _patch_paths(tmp_path):
                result = gather_raw_files("2026-03-11", carry_forward_days=3)

            names = [Path(f).name for f in result]
            # late.json should NOT appear — it was already processed on day 10
            self.assertNotIn("2026-03-09-newsletter-late.json", names)


class TestLoadSourcesCarryForward(unittest.TestCase):
    """Test that load_sources properly tags carry-forward sources."""

    def test_carryforward_sources_are_tagged(self):
        """Sources from carry-forward files get carry_forward=True and original_date."""
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            link_a = _make_link("https://example.com/a", "AI Article A")
            link_b = _make_link("https://example.com/b", "AI Article B")
            _make_newsletter(tmp_path, "2026-03-10-newsletter-alpha.json", "Alpha", [link_a])
            _make_newsletter(tmp_path, "2026-03-09-newsletter-beta.json", "Beta", [link_b])
            _make_manifest(tmp_path, "2026-03-09", [])  # Empty = beta is "late"

            with _patch_paths(tmp_path):
                result = load_sources("2026-03-10", carry_forward_days=1)

            self.assertEqual(result['carryforward_count'], 1)
            cf_sources = [s for s in result['sources'] if s.get('carry_forward')]
            self.assertEqual(len(cf_sources), 1)
            self.assertEqual(cf_sources[0]['original_date'], '2026-03-09')

    def test_carryforward_count_excludes_filtered(self):
        """carryforward_count only counts kept (non-filtered) sources."""
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            # A link too short to pass filtering
            short_link = {"url": "https://example.com/short", "title": "Short", "content": "tiny"}
            good_link = _make_link("https://example.com/good", "Good AI Article")
            _make_newsletter(tmp_path, "2026-03-10-newsletter-a.json", "A", [])
            _make_newsletter(tmp_path, "2026-03-09-newsletter-b.json", "B", [short_link, good_link])
            _make_manifest(tmp_path, "2026-03-09", [])

            with _patch_paths(tmp_path):
                result = load_sources("2026-03-10", carry_forward_days=1)

            # Only 1 kept carry-forward (the short one is filtered)
            self.assertEqual(result['carryforward_count'], 1)

    def test_no_carryforward_no_tags(self):
        """Without carry-forward, no sources have carry_forward tag."""
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            link_a = _make_link("https://example.com/a", "AI Article A")
            _make_newsletter(tmp_path, "2026-03-10-newsletter-alpha.json", "Alpha", [link_a])

            with _patch_paths(tmp_path):
                result = load_sources("2026-03-10", carry_forward_days=0)

            self.assertEqual(result['carryforward_count'], 0)
            for s in result['sources']:
                self.assertNotIn('carry_forward', s)

    def test_files_loaded_paths_in_output(self):
        """Output includes files_loaded_paths with basenames."""
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            link_a = _make_link("https://example.com/a", "Article")
            _make_newsletter(tmp_path, "2026-03-10-newsletter-alpha.json", "Alpha", [link_a])

            with _patch_paths(tmp_path):
                result = load_sources("2026-03-10")

            self.assertIn('files_loaded_paths', result)
            self.assertEqual(result['files_loaded_paths'], ["2026-03-10-newsletter-alpha.json"])


class TestSaveManifest(unittest.TestCase):

    def test_writes_manifest(self):
        """save_manifest writes a valid JSON manifest."""
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            output_dir = tmp_path / 'data' / 'output'
            output_dir.mkdir(parents=True, exist_ok=True)

            import save_processed_files as spf
            original = spf.__file__
            spf.__file__ = str(tmp_path / 'scripts' / 'save_processed_files.py')
            try:
                save_manifest("2026-03-09", ["file1.json", "file2.json"])
            finally:
                spf.__file__ = original

            manifest_path = output_dir / "2026-03-09-processed-files.json"
            self.assertTrue(manifest_path.exists())

            with open(manifest_path) as f:
                data = json.load(f)
            self.assertEqual(data['date'], '2026-03-09')
            self.assertEqual(data['files'], ['file1.json', 'file2.json'])
            self.assertIn('generated_at', data)


class TestExtractPublisherRegex(unittest.TestCase):
    """Test the improved regex-based extract_publisher."""

    def test_standard_name(self):
        self.assertEqual(
            extract_publisher("2026-03-09-newsletter-tldrnewsletter.json"),
            "tldrnewsletter",
        )

    def test_name_with_4digit_time_suffix(self):
        self.assertEqual(
            extract_publisher("2026-03-09-newsletter-tldrnewsletter-1009.json"),
            "tldrnewsletter",
        )

    def test_name_with_6digit_time_suffix(self):
        """n8n generates HHMMSS timestamps (e.g. 100923 for 10:09:23)."""
        self.assertEqual(
            extract_publisher("2026-03-09-newsletter-tldrnewsletter-100923.json"),
            "tldrnewsletter",
        )

    def test_manual_name(self):
        self.assertEqual(
            extract_publisher("2026-03-09-newsletter-manual.json"),
            "manual",
        )

    def test_hyphenated_publisher(self):
        self.assertEqual(
            extract_publisher("2026-03-09-newsletter-my-newsletter.json"),
            "my-newsletter",
        )

    def test_hyphenated_publisher_with_time(self):
        self.assertEqual(
            extract_publisher("2026-03-09-newsletter-my-newsletter-0830.json"),
            "my-newsletter",
        )

    def test_different_date_still_works(self):
        """Carry-forward files have a different date — regex handles this."""
        self.assertEqual(
            extract_publisher("2026-03-08-newsletter-lateone-2100.json", target_date="2026-03-09"),
            "lateone",
        )

    def test_no_target_date_needed(self):
        """target_date parameter is optional and ignored."""
        self.assertEqual(
            extract_publisher("2026-03-09-newsletter-alpha.json"),
            extract_publisher("2026-03-09-newsletter-alpha.json", "2026-03-09"),
        )


if __name__ == '__main__':
    unittest.main()
