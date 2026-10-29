"""Tests for sandbox.roman: to_roman and from_roman."""

import unittest

from sandbox.roman import from_roman, to_roman


class RomanTest(unittest.TestCase):
    def test_to_roman_returns_standard_numeral_for_each_example(self) -> None:
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(9), "IX")
        self.assertEqual(to_roman(40), "XL")
        self.assertEqual(to_roman(90), "XC")
        self.assertEqual(to_roman(400), "CD")
        self.assertEqual(to_roman(900), "CM")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_to_roman_returns_LX_for_60(self) -> None:
        self.assertEqual(to_roman(60), "LX")

    def test_from_roman_returns_integer_for_each_example(self) -> None:
        self.assertEqual(from_roman("I"), 1)
        self.assertEqual(from_roman("IV"), 4)
        self.assertEqual(from_roman("XL"), 40)
        self.assertEqual(from_roman("CD"), 400)
        self.assertEqual(from_roman("MMMCMXCIX"), 3999)

    def test_to_roman_raises_value_error_for_0_and_4000(self) -> None:
        with self.assertRaises(ValueError) as zero:
            to_roman(0)
        self.assertIn("1 to 3999", str(zero.exception))
        with self.assertRaises(ValueError) as over:
            to_roman(4000)
        self.assertIn("1 to 3999", str(over.exception))

    def test_from_roman_raises_malformed_for_empty_lowercase_non_roman_and_invalid_sequences(self) -> None:
        for bad in ("", "iv", "A", "IIII", "VV", "LX"):
            with self.assertRaises(ValueError) as ctx:
                from_roman(bad)
            self.assertIn("malformed Roman numeral", str(ctx.exception))

    def test_from_roman_raises_range_error_for_well_formed_out_of_range(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("MMMM")
        self.assertIn("1 to 3999", str(ctx.exception))
        self.assertNotIn("malformed Roman numeral", str(ctx.exception))

    def test_round_trip_from_roman_of_to_roman_is_identity_for_wart_free_subset(self) -> None:
        for n in (1, 4, 9, 40, 90, 400, 900, 3999, 5, 50, 100, 1000, 1999, 2024):
            self.assertEqual(from_roman(to_roman(n)), n)

    def test_to_roman_treats_bool_as_int(self) -> None:
        self.assertEqual(to_roman(True), "I")
        with self.assertRaises(ValueError) as ctx:
            to_roman(False)
        self.assertIn("1 to 3999", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
