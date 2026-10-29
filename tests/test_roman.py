import unittest

import sandbox.roman


class RomanTest(unittest.TestCase):
    def test_to_roman_1_returns_I(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(1), "I")

    def test_to_roman_out_of_range_raises(self) -> None:
        with self.assertRaises(ValueError):
            sandbox.roman.to_roman(0)
        with self.assertRaises(ValueError):
            sandbox.roman.to_roman(4000)

    def test_to_roman_direct_value_pins(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(1994), "MCMXCIV")
        self.assertEqual(sandbox.roman.to_roman(3999), "MMMCMXCIX")
        self.assertEqual(sandbox.roman.to_roman(4), "IV")
        self.assertEqual(sandbox.roman.to_roman(9), "IX")
        self.assertEqual(sandbox.roman.to_roman(40), "XL")
        self.assertEqual(sandbox.roman.to_roman(90), "XC")
        self.assertEqual(sandbox.roman.to_roman(400), "CD")
        self.assertEqual(sandbox.roman.to_roman(900), "CM")


if __name__ == "__main__":
    unittest.main()
