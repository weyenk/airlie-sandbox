import itertools
import re
import unittest

import sandbox.roman
from sandbox.roman import from_roman, to_roman


class RomanTest(unittest.TestCase):
    def test_roman_module_is_importable_and_exposes_callable_to_roman_and_from_roman(self) -> None:
        self.assertTrue(callable(sandbox.roman.to_roman))
        self.assertTrue(callable(sandbox.roman.from_roman))

    def test_to_roman_returns_only_roman_characters_for_every_n_in_1_to_3999(self) -> None:
        for n in range(1, 4000):
            result = to_roman(n)
            self.assertIsInstance(result, str)
            self.assertIsNotNone(re.fullmatch(r"[IVXLCDM]+", result))

    def test_to_roman_raises_value_error_for_every_out_of_range_integer(self) -> None:
        for n in (0, -1, -100, 4000, 4001, 10000, -10000):
            with self.assertRaises(ValueError):
                to_roman(n)
        for n in range(1, 4000):
            self.assertIsInstance(to_roman(n), str)

    def test_from_roman_round_trips_to_roman_for_every_n_in_1_to_3999(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)

    def test_from_roman_raises_value_error_for_every_invalid_string_of_at_most_four_characters(self) -> None:
        valid = {to_roman(n) for n in range(1, 4000)}
        inverse = {to_roman(n): n for n in range(1, 4000)}
        alphabet = "IVXLCDM"
        for length in range(0, 5):
            for s in ("".join(chars) for chars in itertools.product(alphabet, repeat=length)):
                if s in valid:
                    self.assertEqual(from_roman(s), inverse[s])
                else:
                    with self.assertRaises(ValueError):
                        from_roman(s)
        for s in ("iv", " I", "I I"):
            with self.assertRaises(ValueError):
                from_roman(s)

    def test_from_roman_raises_value_error_for_every_string_longer_than_fifteen_characters(self) -> None:
        for s in ("I" * 16, "M" * 16, to_roman(3888) + "I", "M" * 17):
            with self.assertRaises(ValueError):
                from_roman(s)
        self.assertEqual(from_roman(to_roman(3888)), 3888)

    def test_from_roman_returns_the_correct_n_for_every_valid_string_of_length_5_to_15(self) -> None:
        inverse = {to_roman(n): n for n in range(1, 4000)}
        for s, n in inverse.items():
            if 5 <= len(s) <= 15:
                self.assertEqual(from_roman(s), n)
        self.assertEqual(from_roman(to_roman(3900)), 3900)
        self.assertEqual(from_roman("MCMXCIV"), 1994)

    def test_from_roman_raises_value_error_for_invalid_strings_of_length_5_to_15(self) -> None:
        valid = {to_roman(n) for n in range(1, 4000)}
        inverse = {to_roman(n): n for n in range(1, 4000)}
        for s in ("MMMMM", "MCMCM", "IIIIII", "IM", "XLX"):
            self.assertNotIn(s, valid)
            with self.assertRaises(ValueError):
                from_roman(s)
        for s, n in inverse.items():
            if 5 <= len(s) <= 15:
                self.assertEqual(from_roman(s), n)


if __name__ == "__main__":
    unittest.main()
