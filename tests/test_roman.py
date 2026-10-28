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


class FromRomanTest(unittest.TestCase):
    def test_from_roman_mcmxciv_returns_1994(self) -> None:
        self.assertEqual(sandbox.roman.from_roman("MCMXCIV"), 1994)

    def test_from_roman_mmmcmxcix_returns_3999(self) -> None:
        self.assertEqual(sandbox.roman.from_roman("MMMCMXCIX"), 3999)

    def test_from_roman_iv_returns_4(self) -> None:
        self.assertEqual(sandbox.roman.from_roman("IV"), 4)

    def test_from_roman_iiii_raises_invalid(self) -> None:
        with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
            sandbox.roman.from_roman("IIII")

    def test_from_roman_ic_raises_invalid(self) -> None:
        with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
            sandbox.roman.from_roman("IC")

    def test_from_roman_empty_raises_invalid(self) -> None:
        with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
            sandbox.roman.from_roman("")

    def test_from_roman_abc_raises_invalid(self) -> None:
        with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
            sandbox.roman.from_roman("abc")

    def test_round_trip_is_identity_for_all_1_to_3999(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(sandbox.roman.from_roman(sandbox.roman.to_roman(n)), n)

    def test_from_roman_non_str_raises_invalid(self) -> None:
        with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
            sandbox.roman.from_roman(1994)


if __name__ == "__main__":
    unittest.main()
