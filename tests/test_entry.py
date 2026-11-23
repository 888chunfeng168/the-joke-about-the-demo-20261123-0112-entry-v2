"""Tests for main.py: the written joke is one line, in range, exact, deterministic."""

import hashlib
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from main import JOKE  # noqa: E402

EXPECTED = "My AI agent crashed the demo, apologized, fixed it live \u2014 and the audience thinks I'm its assistant."


def run_main(out_path: Path) -> subprocess.CompletedProcess:
    env = dict(os.environ, JOKE_OUTPUT_PATH=str(out_path))
    return subprocess.run(
        [sys.executable, str(ROOT / "main.py")],
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )


class TestEntry(unittest.TestCase):
    def test_joke_is_the_fixed_line(self):
        self.assertEqual(JOKE, EXPECTED)

    def test_single_line_and_length(self):
        self.assertEqual(JOKE.count("\n"), 0)
        self.assertEqual(JOKE.count("\r"), 0)
        self.assertTrue(JOKE.strip())
        self.assertGreaterEqual(len(JOKE), 1)
        self.assertLessEqual(len(JOKE), 280)

    def test_writes_exact_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "entry.txt"
            result = run_main(out)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(out.read_text(encoding="utf-8"), EXPECTED)

    def test_two_runs_are_byte_identical(self):
        with tempfile.TemporaryDirectory() as tmp:
            first = Path(tmp) / "first.txt"
            second = Path(tmp) / "second.txt"
            self.assertEqual(run_main(first).returncode, 0)
            self.assertEqual(run_main(second).returncode, 0)
            digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
            self.assertEqual(digest(first), digest(second))


if __name__ == "__main__":
    unittest.main()
