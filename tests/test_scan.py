import tempfile
import unittest
from pathlib import Path

from iac_secret_scanner import run, scan_file


class ScanTests(unittest.TestCase):
    def test_detects_access_key_and_password_assignment(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "main.tf"
            path.write_text(
                'access_key = "AKIA1234567890ABCDEF"\n'
                'password = "example-secret-value"\n',
                encoding="utf-8",
            )

            self.assertEqual(scan_file(path), ["aws_key", "password"])

    def test_ignores_unsupported_extensions(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "notes.txt").write_text(
                'password = "example-secret-value"', encoding="utf-8"
            )

            self.assertEqual(run(root), {})

    def test_skips_symbolic_links(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "workspace"
            root.mkdir()
            outside = Path(tmp) / "outside.env"
            outside.write_text('password = "example-secret-value"', encoding="utf-8")
            link = root / ".env"
            try:
                link.symlink_to(outside)
            except (OSError, NotImplementedError):
                self.skipTest("Symbolic links are not available in this environment")

            self.assertEqual(run(root), {})
            self.assertEqual(scan_file(link), [])

    def test_skips_dependency_directories(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            dependency_dir = root / "node_modules"
            dependency_dir.mkdir()
            (dependency_dir / "config.json").write_text(
                'password = "example-secret-value"', encoding="utf-8"
            )

            self.assertEqual(run(root), {})

    def test_detects_github_google_and_slack_tokens(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "secrets.env"
            path.write_text(
                "GITHUB_TOKEN=ghp_" + "A" * 36 + "\\n"
                "GOOGLE_API_KEY=AIza" + "A" * 35 + "\\n"
                "SLACK_TOKEN=xoxb-" + "A" * 20,
                encoding="utf-8",
            )
            self.assertEqual(
                scan_file(path),
                ["github_token", "google_api_key", "slack_token"],
            )

    def test_skips_files_over_the_configured_size_limit(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "large.env"
            path.write_bytes(b"A" * (5 * 1024 * 1024 + 1))
            self.assertEqual(scan_file(path), [])


if __name__ == "__main__":
    unittest.main()
