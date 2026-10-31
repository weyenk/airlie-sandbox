"""Tests for sandbox.roman: canonical Roman numerals for 1..3999 and back."""

import itertools
import unittest

from sandbox.roman import from_roman, to_roman

# Independent positional reference: digit decomposition, not a greedy table.
_ONES = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
_TENS = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
_HUNDREDS = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
_THOUSANDS = ["", "M", "MM", "MMM"]


def _expected_roman(n: int) -> str:
    """Canonical numeral for n in 1..3999, built from its decimal digits."""
    thousands, rest = divmod(n, 1000)
    hundreds, rest = divmod(rest, 100)
    tens, ones = divmod(rest, 10)
    return _THOUSANDS[thousands] + _HUNDREDS[hundreds] + _TENS[tens] + _ONES[ones]


class RomanTest(unittest.TestCase):
    def test_to_roman_returns_canonical_and_round_trips_for_every_n_in_1_to_3999(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(to_roman(n), _expected_roman(n))
            self.assertEqual(from_roman(to_roman(n)), n)
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(9), "IX")
        self.assertEqual(to_roman(40), "XL")
        self.assertEqual(to_roman(90), "XC")
        self.assertEqual(to_roman(400), "CD")
        self.assertEqual(to_roman(900), "CM")
        self.assertEqual(to_roman(1994), "MCMXCIV")
        self.assertEqual(to_roman(3888), "MMMDCCCLXXXVIII")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_to_roman_raises_valueerror_with_phrase_for_out_of_range_and_non_int(self) -> None:
        for bad in (0, 4000, -1, 1.5, "V", None, True):
            with self.assertRaises(ValueError) as ctx:
                to_roman(bad)
            self.assertIn("to_roman expects an int in 1..3999", str(ctx.exception))

    def test_from_roman_returns_n_for_every_canonical_output(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)
        self.assertEqual(from_roman("IV"), 4)
        self.assertEqual(from_roman("IX"), 9)
        self.assertEqual(from_roman("XL"), 40)
        self.assertEqual(from_roman("XC"), 90)
        self.assertEqual(from_roman("CD"), 400)
        self.assertEqual(from_roman("CM"), 900)
        self.assertEqual(from_roman("MCMXCIV"), 1994)
        self.assertEqual(from_roman("MMMDCCCLXXXVIII"), 3888)
        self.assertEqual(from_roman("MMMCMXCIX"), 3999)

    def test_from_roman_raises_malformed_phrase_for_every_non_canonical_1_to_4_char_string(self) -> None:
        valid = {to_roman(n): n for n in range(1, 4000)}
        for length in (1, 2, 3, 4):
            for letters in itertools.product("IVXLCDM", repeat=length):
                numeral = "".join(letters)
                if numeral in valid:
                    self.assertEqual(from_roman(numeral), valid[numeral])
                else:
                    with self.assertRaises(ValueError) as ctx:
                        from_roman(numeral)
                    self.assertIn("from_roman got a malformed numeral", str(ctx.exception))

    def test_from_roman_raises_1_to_15_phrase_for_empty_string(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("")
        self.assertIn("from_roman expected a numeral of 1 to 15 characters", str(ctx.exception))

    def test_from_roman_raises_for_overlong_and_invalid_character_strings(self) -> None:
        with self.assertRaises(ValueError):
            from_roman("M" * 16)
        with self.assertRaises(ValueError):
            from_roman("mcmxciv")

    def test_from_roman_raises_malformed_phrase_for_non_str_argument(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman(123)
        self.assertIn("from_roman got a malformed numeral", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
