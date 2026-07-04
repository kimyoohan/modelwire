#!/usr/bin/env python3
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.build_site import markdown_to_html, sanitize_filename  # noqa: E402


class BuildSiteTests(unittest.TestCase):
    def test_markdown_renderer(self):
        markdown = """# Heading

This is **bold** and a [link](https://example.com).

- one
- two

Plain paragraph
wrapped line."""
        html = markdown_to_html(markdown)
        self.assertIn("<h1>Heading</h1>", html)
        self.assertIn("<strong>bold</strong>", html)
        self.assertIn('<a href="https://example.com">link</a>', html)
        self.assertIn("<ul>", html)
        self.assertIn("<li>one</li>", html)
        self.assertIn("<li>two</li>", html)
        self.assertIn("<p>Plain paragraph wrapped line.</p>", html)

    def test_filename_sanitizer(self):
        self.assertEqual(sanitize_filename("provider/model:latest 2026"), "provider_model_latest_2026")
        self.assertEqual(sanitize_filename("abc-XYZ_123"), "abc-XYZ_123")

    def test_validate_script_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
