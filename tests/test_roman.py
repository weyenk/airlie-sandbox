import unittest

import sandbox.roman


class RomanTest(unittest.TestCase):
    def test_known_values_pin_the_table(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(1), "I")
        self.assertEqual(sandbox.roman.to_roman(4), "IV")
        self.assertEqual(sandbox.roman.to_roman(9), "IX")
        self.assertEqual(sandbox.roman.to_roman(40), "XL")
        self.assertEqual(sandbox.roman.to_roman(90), "XC")
        self.assertEqual(sandbox.roman.to_roman(400), "CD")
        self.assertEqual(sandbox.roman.to_roman(900), "CM")
        self.assertEqual(sandbox.roman.to_roman(1994), "MCMXCIV")
        self.assertEqual(sandbox.roman.to_roman(3999), "MMMCMXCIX")

    def test_zero_returns_empty_string(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(0), "")
        self.assertIsInstance(sandbox.roman.to_roman(0), str)

    def test_out_of_range_raises_value_error(self) -> None:
        with self.assertRaisesRegex(ValueError, r"outside the range"):
            sandbox.roman.to_roman(-1)
        with self.assertRaisesRegex(ValueError, r"outside the range"):
            sandbox.roman.to_roman(4000)


if __name__ == "__main__":
    unittest.main()
