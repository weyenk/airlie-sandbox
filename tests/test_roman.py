import os
import re
import subprocess
import sys
import unittest

from sandbox.roman import to_roman


class RomanTest(unittest.TestCase):
    def test_to_roman_canonical_examples(self) -> None:
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(9), "IX")
        self.assertEqual(to_roman(40), "XL")
        self.assertEqual(to_roman(90), "XC")
        self.assertEqual(to_roman(400), "CD")
        self.assertEqual(to_roman(900), "CM")
        self.assertEqual(to_roman(1994), "MCMXCIV")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")
        self.assertEqual(to_roman(8), "VIII")
        self.assertEqual(to_roman(58), "LVIII")
        self.assertIsInstance(to_roman(1994), str)

    def test_unittest_discovery_and_version_still_passes(self) -> None:
        # Recursion guard: the gate re-runs this very test file, so a nested
        # run skips itself instead of spawning another gate forever.
        if os.environ.get("ROMAN_GATE_INNER") == "1":
            self.skipTest("already inside the gate; avoid recursive gate runs")
        repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        env = dict(os.environ, ROMAN_GATE_INNER="1")
        result = subprocess.run(
            [sys.executable, "-m", "unittest", "-q"],
            cwd=repo_root,
            env=env,
            capture_output=True,
            text=True,
            timeout=120,
        )
        output = result.stdout + result.stderr
        self.assertEqual(result.returncode, 0, output)
        self.assertIn("OK", output)
        # -q prints no passing test names, so the run count is the discovery
        # proof: 1 version test + 2 roman tests = 3 after this layer.
        ran = re.search(r"Ran (\d+) tests?", output)
        self.assertIsNotNone(ran, output)
        self.assertGreaterEqual(int(ran.group(1)), 3, output)


if __name__ == "__main__":
    unittest.main()
