#!/usr/bin/env python3
"""Unit tests for scripts/generate_image.py"""

import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from generate_image import main


class TestGenerateImageCLI(unittest.TestCase):

    def test_missing_date_exits_with_error(self):
        with patch("sys.argv", ["generate_image.py"]):
            with self.assertRaises(SystemExit) as ctx:
                main()
            self.assertEqual(ctx.exception.code, 1)

    def test_missing_prompt_file_exits_with_error(self, ):
        with patch("sys.argv", ["generate_image.py", "1999-01-01"]):
            with self.assertRaises(SystemExit) as ctx:
                main()
            self.assertEqual(ctx.exception.code, 1)

    def test_skip_when_image_already_exists(self, tmp_path=None):
        import tempfile

        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir = Path(tmpdir)
            prompt_file = tmpdir / "2099-01-01-image-prompt.md"
            prompt_file.write_text("A test prompt")
            image_file = tmpdir / "2099-01-01-image.png"
            image_file.write_text("fake image")

            with patch("generate_image.DATA_OUTPUT", tmpdir), \
                 patch("sys.argv", ["generate_image.py", "2099-01-01"]), \
                 patch("builtins.print") as mock_print:
                main()
                output = json.loads(mock_print.call_args[0][0])
                self.assertEqual(output["status"], "skipped")


class TestGeminiBackendSafetyHandling(unittest.TestCase):

    def test_empty_candidates_raises(self):
        from image_backends import gemini_backend

        mock_response = type("Response", (), {"candidates": []})()

        with patch.dict("os.environ", {"GOOGLE_API_KEY": "fake"}), \
             patch("google.genai.Client") as mock_client_cls:
            mock_client_cls.return_value.models.generate_content.return_value = mock_response

            with self.assertRaises(RuntimeError) as ctx:
                gemini_backend.generate("test prompt", "/tmp/test.png")
            self.assertIn("No candidates", str(ctx.exception))

    def test_none_candidates_raises(self):
        from image_backends import gemini_backend

        mock_response = type("Response", (), {"candidates": None})()

        with patch.dict("os.environ", {"GOOGLE_API_KEY": "fake"}), \
             patch("google.genai.Client") as mock_client_cls:
            mock_client_cls.return_value.models.generate_content.return_value = mock_response

            with self.assertRaises(RuntimeError) as ctx:
                gemini_backend.generate("test prompt", "/tmp/test.png")
            self.assertIn("No candidates", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
