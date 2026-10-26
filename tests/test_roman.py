import os
import re
import subprocess
import sys
import unittest

import sandbox.roman
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

    def test_to_roman_rejects_less_than_one(self) -> None:
        with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
            to_roman(0)
        with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
            to_roman(-5)

    def test_to_roman_rejects_greater_than_3999(self) -> None:
        with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
            to_roman(4000)

    def test_to_roman_rejects_non_int(self) -> None:
        with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
            to_roman(4.5)
        with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
            to_roman("IV")
        with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
            to_roman(None)
        with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
            to_roman([])
        # bool is an int subclass but has no canonical numeral; reject it explicitly.
        with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
            to_roman(True)
        with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
            to_roman(False)

    def test_from_roman_canonical_examples(self) -> None:
        self.assertEqual(sandbox.roman.from_roman("I"), 1)
        self.assertEqual(sandbox.roman.from_roman("IV"), 4)
        self.assertEqual(sandbox.roman.from_roman("XL"), 40)
        self.assertEqual(sandbox.roman.from_roman("CD"), 400)
        self.assertEqual(sandbox.roman.from_roman("CM"), 900)
        self.assertEqual(sandbox.roman.from_roman("MCMXCIV"), 1994)
        self.assertEqual(sandbox.roman.from_roman("MMMCMXCIX"), 3999)
        self.assertIsInstance(sandbox.roman.from_roman("MCMXCIV"), int)

    def test_from_roman_rejects_bad_chars_and_lowercase(self) -> None:
        with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
            sandbox.roman.from_roman("A")
        with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
            sandbox.roman.from_roman("iv")

    def test_from_roman_rejects_non_canonical(self) -> None:
        with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
            sandbox.roman.from_roman("IIII")
        with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
            sandbox.roman.from_roman("VV")
        with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
            sandbox.roman.from_roman("IL")
        with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
            sandbox.roman.from_roman("MCMC")

    def test_from_roman_rejects_empty_string(self) -> None:
        with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
            sandbox.roman.from_roman("")

    def test_from_roman_rejects_non_string(self) -> None:
        with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
            sandbox.roman.from_roman(1994)
        with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
            sandbox.roman.from_roman(None)
        with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
            sandbox.roman.from_roman([])

    def test_round_trip_from_to_for_all_range(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(sandbox.roman.from_roman(to_roman(n)), n)

    def test_round_trip_to_from_identity_for_canonical_samples(self) -> None:
        samples = [
            "I", "IV", "IX", "X", "XL", "XC",
            "C", "CD", "CM", "D", "M",
            "MCMXCIV", "MMMCMXCIX",
        ]
        for s in samples:
            self.assertEqual(to_roman(sandbox.roman.from_roman(s)), s)

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
        # proof: 1 version test + 8 roman tests = 9 after this layer.
        ran = re.search(r"Ran (\d+) tests?", output)
        self.assertIsNotNone(ran, output)
        self.assertGreaterEqual(int(ran.group(1)), 3, output)


if __name__ == "__main__":
    unittest.main()
