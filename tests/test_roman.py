"""Tests for sandbox.roman.to_roman."""

import unittest

from sandbox.roman import to_roman


class ToRomanTest(unittest.TestCase):
    def test_to_roman_returns_canonical_subtractive_forms(self) -> None:
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(9), "IX")
        self.assertEqual(to_roman(40), "XL")
        self.assertEqual(to_roman(90), "XC")
        self.assertEqual(to_roman(400), "CD")
        self.assertEqual(to_roman(900), "CM")
        self.assertEqual(to_roman(1994), "MCMXCIV")
        self.assertEqual(to_roman(888), "DCCCLXXXVIII")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_to_roman_matches_reference_for_every_value_in_range(self) -> None:
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thousands = ["", "M", "MM", "MMM"]
        for n in range(1, 4000):
            expected = (
                thousands[n // 1000]
                + hundreds[(n // 100) % 10]
                + tens[(n // 10) % 10]
                + ones[n % 10]
            )
            self.assertEqual(to_roman(n), expected)

    def test_to_roman_returns_a_string_for_every_value_in_range(self) -> None:
        for n in range(1, 4000):
            self.assertIsInstance(to_roman(n), str)

    def test_to_roman_rejects_out_of_range_and_non_integer(self) -> None:
        for bad in (0, 4000, -1, 1.5, "x", True):
            with self.assertRaisesRegex(ValueError, r"must be an integer from 1 to 3999"):
                to_roman(bad)


if __name__ == "__main__":
    unittest.main()
