import itertools
import unittest

import sandbox.roman


class RomanTest(unittest.TestCase):
    def test_to_roman_returns_the_standard_numeral_for_named_values(self) -> None:
        expected = {
            1994: "MCMXCIV",
            3999: "MMMCMXCIX",
            3: "III",
            14: "XIV",
            49: "XLIX",
            99: "XCIX",
            444: "CDXLIV",
            999: "CMXCIX",
            2024: "MMXXIV",
        }
        for n, numeral in expected.items():
            self.assertEqual(sandbox.roman.to_roman(n), numeral)

    def test_round_trip_holds_for_every_integer_in_1_to_3999(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(sandbox.roman.from_roman(sandbox.roman.to_roman(n)), n)

    def test_to_roman_raises_value_error_out_of_range(self) -> None:
        for n in (0, -1, 4000):
            with self.assertRaises(ValueError):
                sandbox.roman.to_roman(n)

    def test_from_roman_returns_the_integer_for_valid_numerals(self) -> None:
        self.assertEqual(sandbox.roman.from_roman("MCMXCIV"), 1994)
        self.assertEqual(sandbox.roman.from_roman("MMMCMXCIX"), 3999)

    def test_from_roman_accepts_exactly_the_canonical_1_to_4_char_numerals(self) -> None:
        canonical = {
            sandbox.roman.to_roman(n): n
            for n in range(1, 4000)
            if len(sandbox.roman.to_roman(n)) <= 4
        }
        self.assertEqual(len(canonical), 346)
        for length in range(1, 5):
            for chars in itertools.product("IVXLCDM", repeat=length):
                numeral = "".join(chars)
                if numeral in canonical:
                    self.assertEqual(sandbox.roman.from_roman(numeral), canonical[numeral])
                else:
                    with self.assertRaises(ValueError):
                        sandbox.roman.from_roman(numeral)

    def test_from_roman_raises_value_error_on_empty_string(self) -> None:
        with self.assertRaises(ValueError):
            sandbox.roman.from_roman("")


if __name__ == "__main__":
    unittest.main()
