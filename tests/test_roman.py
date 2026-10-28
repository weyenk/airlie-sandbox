import unittest

from sandbox.roman import to_roman


class RomanTest(unittest.TestCase):
    def test_to_roman_returns_canonical_numeral_for_each_pinned_input(self) -> None:
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(9), "IX")
        self.assertEqual(to_roman(10), "X")
        self.assertEqual(to_roman(40), "XL")
        self.assertEqual(to_roman(90), "XC")
        self.assertEqual(to_roman(100), "C")
        self.assertEqual(to_roman(400), "CD")
        self.assertEqual(to_roman(900), "CM")
        self.assertEqual(to_roman(1000), "M")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")
        self.assertEqual(to_roman(2024), "MMXXIV")
        self.assertEqual(to_roman(1994), "MCMXCIV")
        self.assertEqual(to_roman(88), "LXXXVIII")
        self.assertEqual(to_roman(3888), "MMMDCCCLXXXVIII")
        self.assertEqual(to_roman(14), "XIV")
        self.assertEqual(to_roman(999), "CMXCIX")

    def test_to_roman_raises_value_error_with_exact_unquoted_message_for_0_and_4000(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            to_roman(0)
        self.assertEqual(str(ctx.exception), "n must be an integer from 1 to 3999, got 0")
        with self.assertRaises(ValueError) as ctx:
            to_roman(4000)
        self.assertEqual(str(ctx.exception), "n must be an integer from 1 to 3999, got 4000")

    def test_to_roman_raises_value_error_for_negative_input(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            to_roman(-1)
        self.assertEqual(str(ctx.exception), "n must be an integer from 1 to 3999, got -1")


if __name__ == "__main__":
    unittest.main()
