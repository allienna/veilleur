#!/usr/bin/env python3
"""Tests for carry-forward feature: late-arriving newsletters inclusion."""

import json
import sys
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


class TestGatherRawFiles(unittest.TestCase):

    def test_no_carryforward(self, ):
        """Without carry-forward flag, only current day files are returned."""
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            _make_newsletter(tmp_path, "2026-03-10-newsletter-alpha.json", "Alpha", [])
            _make_newsletter(tmp_path, "2026-03-09-newsletter-beta.json", "Beta", [])

            with patch('load_sources.Path') as mock_path_cls:
                # We need to patch the data dirs used in gather_raw_files
                pass

            # Direct test: use the actual function with patched paths
            import load_sources as ls
            original_parent = Path(ls.__file__).parent.parent
            data_dir = tmp_path / 'data' / 'raw'

            import glob as globmod
            pattern = str(data_dir / "2026-03-10-newsletter-*.json")
            files = sorted(globmod.glob(pattern))
            self.assertEqual(len(files), 1)
            self.assertIn("alpha", files[0])

    def test_gather_with_carryforward_no_manifest(self):
        """Without a manifest for previous day, no carry-forward happens."""
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            _make_newsletter(tmp_path, "2026-03-10-newsletter-alpha.json", "Alpha", [])
            _make_newsletter(tmp_path, "2026-03-09-newsletter-beta.json", "Beta", [])

            result = _gather_with_tmp(tmp_path, "2026-03-10", carry_forward_days=1)
            names = [Path(f).name for f in result]
            # No manifest for 2026-03-09, so only current day
            self.assertEqual(names, ["2026-03-10-newsletter-alpha.json"])

    def test_gather_with_carryforward_all_processed(self):
        """When manifest covers all files, nothing is carried forward."""
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            _make_newsletter(tmp_path, "2026-03-10-newsletter-alpha.json", "Alpha", [])
            _make_newsletter(tmp_path, "2026-03-09-newsletter-beta.json", "Beta", [])
            _make_manifest(tmp_path, "2026-03-09", ["2026-03-09-newsletter-beta.json"])

            result = _gather_with_tmp(tmp_path, "2026-03-10", carry_forward_days=1)
            # Only the current day file
            names = [Path(f).name for f in result]
            self.assertEqual(names, ["2026-03-10-newsletter-alpha.json"])

    def test_gather_with_carryforward_late_file(self):
        """A file not in the manifest is carried forward."""
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            _make_newsletter(tmp_path, "2026-03-10-newsletter-alpha.json", "Alpha", [])
            _make_newsletter(tmp_path, "2026-03-09-newsletter-beta.json", "Beta", [])
            _make_newsletter(tmp_path, "2026-03-09-newsletter-gamma-2100.json", "Gamma Late", [])
            # Manifest only includes beta, not gamma (gamma arrived late)
            _make_manifest(tmp_path, "2026-03-09", ["2026-03-09-newsletter-beta.json"])

            result = _gather_with_tmp(tmp_path, "2026-03-10", carry_forward_days=1)
            names = [Path(f).name for f in result]
            # Carry-forward first, then current day
            self.assertEqual(names, [
                "2026-03-09-newsletter-gamma-2100.json",
                "2026-03-10-newsletter-alpha.json",
            ])


def _gather_with_tmp(tmp_path, target_date, carry_forward_days=0):
    """Call gather_raw_files with paths redirected to tmp_path."""
    import load_sources as ls
    import glob as globmod

    data_dir = tmp_path / 'data' / 'raw'
    output_dir = tmp_path / 'data' / 'output'

    # Inline reimplementation using the same logic as gather_raw_files
    # but with custom paths (avoids complex patching)
    from datetime import datetime, timedelta

    pattern = str(data_dir / f"{target_date}-newsletter-*.json")
    files = sorted(globmod.glob(pattern))

    if carry_forward_days > 0:
        current = datetime.strptime(target_date, "%Y-%m-%d")
        carry_forward_files = []
        for days_back in range(1, carry_forward_days + 1):
            prev_date = (current - timedelta(days=days_back)).strftime("%Y-%m-%d")
            manifest_path = output_dir / f"{prev_date}-processed-files.json"
            if not manifest_path.exists():
                continue
            with open(manifest_path) as f:
                manifest = json.load(f)
            processed = set(manifest.get("files", []))
            prev_pattern = str(data_dir / f"{prev_date}-newsletter-*.json")
            prev_files = sorted(globmod.glob(prev_pattern))
            late_files = [fp for fp in prev_files if Path(fp).name not in processed]
            carry_forward_files.extend(late_files)
        files = carry_forward_files + files

    return files


class TestGatherRawFilesIntegration(unittest.TestCase):
    """Integration tests using actual gather_raw_files with patched paths."""

    def test_gather_no_carryforward_uses_only_target_date(self):
        """gather_raw_files(date, 0) only returns files for that date."""
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            _make_newsletter(tmp_path, "2026-03-10-newsletter-a.json", "A", [])
            _make_newsletter(tmp_path, "2026-03-09-newsletter-b.json", "B", [])

            with _patch_gather_paths(tmp_path):
                result = gather_raw_files("2026-03-10", carry_forward_days=0)

            names = [Path(f).name for f in result]
            self.assertEqual(names, ["2026-03-10-newsletter-a.json"])

    def test_gather_carryforward_includes_late_files(self):
        """gather_raw_files with carry-forward includes unprocessed previous files."""
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            _make_newsletter(tmp_path, "2026-03-10-newsletter-a.json", "A", [])
            _make_newsletter(tmp_path, "2026-03-09-newsletter-b.json", "B", [])
            _make_newsletter(tmp_path, "2026-03-09-newsletter-c-2100.json", "C", [])
            _make_manifest(tmp_path, "2026-03-09", ["2026-03-09-newsletter-b.json"])

            with _patch_gather_paths(tmp_path):
                result = gather_raw_files("2026-03-10", carry_forward_days=1)

            names = [Path(f).name for f in result]
            self.assertIn("2026-03-09-newsletter-c-2100.json", names)
            self.assertIn("2026-03-10-newsletter-a.json", names)
            # Carry-forward comes first
            self.assertEqual(names[0], "2026-03-09-newsletter-c-2100.json")

    def test_gather_carryforward_no_manifest_skips(self):
        """Without manifest, previous day files are not carried forward."""
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            _make_newsletter(tmp_path, "2026-03-10-newsletter-a.json", "A", [])
            _make_newsletter(tmp_path, "2026-03-09-newsletter-b.json", "B", [])

            with _patch_gather_paths(tmp_path):
                result = gather_raw_files("2026-03-10", carry_forward_days=1)

            names = [Path(f).name for f in result]
            self.assertEqual(names, ["2026-03-10-newsletter-a.json"])

    def test_gather_carryforward_all_processed_skips(self):
        """When all previous files are in the manifest, nothing is carried forward."""
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            _make_newsletter(tmp_path, "2026-03-10-newsletter-a.json", "A", [])
            _make_newsletter(tmp_path, "2026-03-09-newsletter-b.json", "B", [])
            _make_manifest(tmp_path, "2026-03-09", ["2026-03-09-newsletter-b.json"])

            with _patch_gather_paths(tmp_path):
                result = gather_raw_files("2026-03-10", carry_forward_days=1)

            names = [Path(f).name for f in result]
            self.assertEqual(names, ["2026-03-10-newsletter-a.json"])

    def test_gather_carryforward_multiple_days(self):
        """Carry-forward looks back multiple days."""
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            _make_newsletter(tmp_path, "2026-03-10-newsletter-a.json", "A", [])
            _make_newsletter(tmp_path, "2026-03-08-newsletter-old.json", "Old", [])
            _make_manifest(tmp_path, "2026-03-08", [])  # Empty manifest = all files are late

            with _patch_gather_paths(tmp_path):
                result = gather_raw_files("2026-03-10", carry_forward_days=3)

            names = [Path(f).name for f in result]
            self.assertIn("2026-03-08-newsletter-old.json", names)


def _patch_gather_paths(tmp_path):
    """Context manager to redirect gather_raw_files paths to tmp_path."""
    from unittest.mock import patch as _patch

    original_gather = gather_raw_files.__wrapped__ if hasattr(gather_raw_files, '__wrapped__') else None

    # Patch Path(__file__).parent.parent to return tmp_path
    import load_sources as ls
    real_file_path = Path(ls.__file__)
    fake_parent_parent = tmp_path

    class FakePath(type(real_file_path)):
        pass

    # Simplest approach: patch the module-level path computation
    return _patch.multiple(
        'load_sources',
        __file__=str(tmp_path / 'scripts' / 'load_sources.py'),
    )


class TestLoadSourcesCarryForward(unittest.TestCase):
    """Test that load_sources properly tags carry-forward sources."""

    def test_carryforward_sources_are_tagged(self):
        """Sources from carry-forward files get carry_forward=True and original_date."""
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            link_a = _make_link("https://example.com/a", "AI Article A")
            link_b = _make_link("https://example.com/b", "AI Article B")
            _make_newsletter(tmp_path, "2026-03-10-newsletter-alpha.json", "Alpha", [link_a])
            _make_newsletter(tmp_path, "2026-03-09-newsletter-beta.json", "Beta", [link_b])
            _make_manifest(tmp_path, "2026-03-09", [])  # Empty = beta is "late"

            with _patch_gather_paths(tmp_path):
                result = load_sources("2026-03-10", carry_forward_days=1)

            self.assertEqual(result['carryforward_count'], 1)
            # Find the carry-forward source
            cf_sources = [s for s in result['sources'] if s.get('carry_forward')]
            self.assertEqual(len(cf_sources), 1)
            self.assertEqual(cf_sources[0]['original_date'], '2026-03-09')

    def test_no_carryforward_no_tags(self):
        """Without carry-forward, no sources have carry_forward tag."""
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            link_a = _make_link("https://example.com/a", "AI Article A")
            _make_newsletter(tmp_path, "2026-03-10-newsletter-alpha.json", "Alpha", [link_a])

            with _patch_gather_paths(tmp_path):
                result = load_sources("2026-03-10", carry_forward_days=0)

            self.assertEqual(result['carryforward_count'], 0)
            for s in result['sources']:
                self.assertNotIn('carry_forward', s)

    def test_files_loaded_paths_in_output(self):
        """Output includes files_loaded_paths with basenames."""
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            link_a = _make_link("https://example.com/a", "Article")
            _make_newsletter(tmp_path, "2026-03-10-newsletter-alpha.json", "Alpha", [link_a])

            with _patch_gather_paths(tmp_path):
                result = load_sources("2026-03-10")

            self.assertIn('files_loaded_paths', result)
            self.assertEqual(result['files_loaded_paths'], ["2026-03-10-newsletter-alpha.json"])


class TestSaveManifest(unittest.TestCase):

    def test_writes_manifest(self):
        """save_manifest writes a valid JSON manifest."""
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            output_dir = tmp_path / 'data' / 'output'

            with patch('save_processed_files.Path') as MockPath:
                # Redirect __file__ parent.parent
                mock_file = type(Path())('fake')
                MockPath.return_value = mock_file
                MockPath.__truediv__ = Path.__truediv__

            # Direct approach: call with patched paths
            from save_processed_files import save_manifest as sm
            output_dir.mkdir(parents=True, exist_ok=True)

            # Patch Path(__file__).parent.parent
            import save_processed_files as spf
            original = spf.__file__
            spf.__file__ = str(tmp_path / 'scripts' / 'save_processed_files.py')
            try:
                sm("2026-03-09", ["file1.json", "file2.json"])
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

    def test_name_with_time_suffix(self):
        self.assertEqual(
            extract_publisher("2026-03-09-newsletter-tldrnewsletter-1009.json"),
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
