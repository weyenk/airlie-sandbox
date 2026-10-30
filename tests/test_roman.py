import itertools
import unittest

from sandbox.roman import from_roman, to_roman


class RomanTest(unittest.TestCase):
    def test_to_roman_uses_only_uppercase_roman_characters_for_every_value_in_range(self) -> None:
        allowed = {"I", "V", "X", "L", "C", "D", "M"}
        for n in range(1, 4000):
            s = to_roman(n)
            self.assertIsInstance(s, str)
            self.assertGreater(len(s), 0)
            self.assertLessEqual(set(s), allowed)
            self.assertEqual(s, s.upper())

    def test_every_integer_in_range_round_trips_through_to_roman_and_from_roman(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)

    def test_no_valid_numeral_exceeds_fifteen_characters(self) -> None:
        for n in range(1, 4000):
            self.assertGreaterEqual(len(to_roman(n)), 1)
            self.assertLessEqual(len(to_roman(n)), 15)
        self.assertEqual(to_roman(3888), "MMMDCCCLXXXVIII")
        self.assertEqual(len(to_roman(3888)), 15)

    def test_to_roman_raises_value_error_for_zero(self) -> None:
        self.assertRaises(ValueError, to_roman, 0)

    def test_to_roman_raises_value_error_for_4000(self) -> None:
        self.assertRaises(ValueError, to_roman, 4000)

    def test_from_roman_raises_value_error_for_every_malformed_string_of_one_to_four_characters(self) -> None:
        valid = {to_roman(n): n for n in range(1, 4000)}
        alphabet = "IVXLCDM"
        for length in range(1, 5):
            for combo in itertools.product(alphabet, repeat=length):
                s = "".join(combo)
                if s in valid:
                    self.assertEqual(from_roman(s), valid[s])
                else:
                    with self.assertRaises(ValueError):
                        from_roman(s)
        for s in ("IIII", "VV", "LL", "DD", "IC", "IM", "XD", "XM", "MMMM", "xiv", "IV1"):
            with self.assertRaises(ValueError):
                from_roman(s)

    def test_from_roman_raises_value_error_for_the_empty_string(self) -> None:
        self.assertRaises(ValueError, from_roman, "")

    def test_from_roman_returns_the_integer_for_each_valid_output(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)
        self.assertEqual(from_roman("IV"), 4)
        self.assertEqual(from_roman("IX"), 9)
        self.assertEqual(from_roman("XL"), 40)
        self.assertEqual(from_roman("XC"), 90)
        self.assertEqual(from_roman("CD"), 400)
        self.assertEqual(from_roman("CM"), 900)
        self.assertEqual(from_roman("MMMCMXCIX"), 3999)
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(9), "IX")
        self.assertEqual(to_roman(44), "XLIV")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")


if __name__ == "__main__":
    unittest.main()
