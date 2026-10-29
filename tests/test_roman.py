import unittest

import sandbox.roman


class RomanTest(unittest.TestCase):
    def test_importing_sandbox_roman_exposes_both_callables(self) -> None:
        self.assertTrue(hasattr(sandbox.roman, "to_roman"))
        self.assertTrue(callable(sandbox.roman.to_roman))
        self.assertTrue(hasattr(sandbox.roman, "from_roman"))
        self.assertTrue(callable(sandbox.roman.from_roman))

    def test_to_roman_round_trips_every_integer_in_range(self) -> None:
        allowed = {"M", "D", "C", "L", "X", "V", "I"}
        for n in range(1, 4000):
            numeral = sandbox.roman.to_roman(n)
            self.assertIsInstance(numeral, str)
            self.assertLessEqual(set(numeral), allowed)
            self.assertEqual(sandbox.roman.from_roman(numeral), n)

    def test_to_roman_and_from_roman_agree_on_fixed_pairs(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(1994), "MCMXCIV")
        self.assertEqual(sandbox.roman.from_roman("IX"), 9)

    def test_to_roman_is_canonical_for_every_integer_in_range(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(
                sandbox.roman.to_roman(sandbox.roman.from_roman(sandbox.roman.to_roman(n))),
                sandbox.roman.to_roman(n),
            )


if __name__ == "__main__":
    unittest.main()
