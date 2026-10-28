import unittest

import sandbox.roman


class ToRomanTest(unittest.TestCase):
    def test_to_roman_1994_returns_mcmxciv(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(1994), "MCMXCIV")

    def test_to_roman_3999_returns_mmmcmxcix(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(3999), "MMMCMXCIX")

    def test_to_roman_4_returns_subtractive_iv_not_iiii(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(4), "IV")
        self.assertNotEqual(sandbox.roman.to_roman(4), "IIII")

    def test_to_roman_900_returns_subtractive_cm_not_dcccc(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(900), "CM")
        self.assertNotEqual(sandbox.roman.to_roman(900), "DCCCC")

    def test_to_roman_0_raises_range_error(self) -> None:
        with self.assertRaisesRegex(ValueError, "n must be between 1 and 3999"):
            sandbox.roman.to_roman(0)
        with self.assertRaisesRegex(ValueError, "n must be between 1 and 3999"):
            sandbox.roman.to_roman(-1)

    def test_to_roman_4000_raises_range_error(self) -> None:
        with self.assertRaisesRegex(ValueError, "n must be between 1 and 3999"):
            sandbox.roman.to_roman(4000)

    def test_to_roman_non_int_raises_type_error(self) -> None:
        with self.assertRaisesRegex(ValueError, "n must be an int between 1 and 3999"):
            sandbox.roman.to_roman(1.5)
        with self.assertRaisesRegex(ValueError, "n must be an int between 1 and 3999"):
            sandbox.roman.to_roman("x")


if __name__ == "__main__":
    unittest.main()
