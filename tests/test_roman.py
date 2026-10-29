import unittest

from sandbox.roman import to_roman


class RomanTest(unittest.TestCase):
    def test_to_roman_raises_valueerror_for_out_of_range(self) -> None:
        for n in (0, -1, 4000):
            with self.assertRaises(ValueError) as ctx:
                to_roman(n)
            self.assertNotEqual(str(ctx.exception), "")

    def test_to_roman_returns_canonical_numeral_for_boundaries(self) -> None:
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(9), "IX")
        self.assertEqual(to_roman(40), "XL")
        self.assertEqual(to_roman(90), "XC")
        self.assertEqual(to_roman(400), "CD")
        self.assertEqual(to_roman(900), "CM")

    def test_to_roman_output_uses_only_roman_characters(self) -> None:
        for n in (1, 4, 9, 40, 90, 400, 900, 3999):
            self.assertLessEqual(set(to_roman(n)), set("IVXLCDM"))


if __name__ == "__main__":
    unittest.main()
