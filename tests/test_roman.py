import unittest

from sandbox.roman import from_roman, to_roman


class RomanTest(unittest.TestCase):
    def test_to_roman_one_returns_I(self) -> None:
        self.assertEqual(to_roman(1), "I")

    def test_to_roman_four_returns_IV_subtractive(self) -> None:
        self.assertEqual(to_roman(4), "IV")

    def test_to_roman_nine_returns_IX_subtractive(self) -> None:
        self.assertEqual(to_roman(9), "IX")

    def test_to_roman_fourteen_returns_XIV(self) -> None:
        self.assertEqual(to_roman(14), "XIV")

    def test_to_roman_forty_returns_XL_subtractive(self) -> None:
        self.assertEqual(to_roman(40), "XL")

    def test_to_roman_ninety_returns_XC_subtractive(self) -> None:
        self.assertEqual(to_roman(90), "XC")

    def test_to_roman_four_hundred_returns_CD_subtractive(self) -> None:
        self.assertEqual(to_roman(400), "CD")

    def test_to_roman_nine_hundred_returns_CM_subtractive(self) -> None:
        self.assertEqual(to_roman(900), "CM")

    def test_to_roman_3999_returns_MMMCMXCIX(self) -> None:
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_to_roman_zero_raises_ValueError(self) -> None:
        with self.assertRaises(ValueError):
            to_roman(0)

    def test_to_roman_4000_raises_ValueError(self) -> None:
        with self.assertRaises(ValueError):
            to_roman(4000)

    def test_to_roman_negative_raises_ValueError(self) -> None:
        with self.assertRaises(ValueError):
            to_roman(-1)

    def test_to_roman_float_raises_with_must_be_an_int(self) -> None:
        with self.assertRaisesRegex(ValueError, "must be an int"):
            to_roman(3.5)

    def test_to_roman_bool_raises_with_must_be_an_int(self) -> None:
        with self.assertRaisesRegex(ValueError, "must be an int"):
            to_roman(True)

    def test_from_roman_I_returns_1(self) -> None:
        self.assertEqual(from_roman("I"), 1)

    def test_from_roman_IV_returns_4(self) -> None:
        self.assertEqual(from_roman("IV"), 4)

    def test_from_roman_IX_returns_9(self) -> None:
        self.assertEqual(from_roman("IX"), 9)

    def test_from_roman_XIV_returns_14(self) -> None:
        self.assertEqual(from_roman("XIV"), 14)

    def test_from_roman_XL_returns_40(self) -> None:
        self.assertEqual(from_roman("XL"), 40)

    def test_from_roman_XC_returns_90(self) -> None:
        self.assertEqual(from_roman("XC"), 90)

    def test_from_roman_CD_returns_400(self) -> None:
        self.assertEqual(from_roman("CD"), 400)

    def test_from_roman_CM_returns_900(self) -> None:
        self.assertEqual(from_roman("CM"), 900)

    def test_from_roman_MMMCMXCIX_returns_3999(self) -> None:
        self.assertEqual(from_roman("MMMCMXCIX"), 3999)

    def test_from_roman_lowercase_xiv_returns_14(self) -> None:
        self.assertEqual(from_roman("xiv"), 14)

    def test_from_roman_empty_raises_with_malformed(self) -> None:
        with self.assertRaisesRegex(ValueError, "malformed"):
            from_roman("")

    def test_from_roman_IIII_raises_with_malformed(self) -> None:
        with self.assertRaisesRegex(ValueError, "malformed"):
            from_roman("IIII")

    def test_from_roman_VV_raises_with_malformed(self) -> None:
        with self.assertRaisesRegex(ValueError, "malformed"):
            from_roman("VV")

    def test_from_roman_IL_raises_with_malformed(self) -> None:
        with self.assertRaisesRegex(ValueError, "malformed"):
            from_roman("IL")

    def test_from_roman_LC_raises_with_malformed(self) -> None:
        with self.assertRaisesRegex(ValueError, "malformed"):
            from_roman("LC")

    def test_from_roman_non_string_raises_ValueError(self) -> None:
        with self.assertRaises(ValueError):
            from_roman(42)

    def test_round_trip_identity_for_every_in_range_value(self) -> None:
        for n in range(1, 4000):
            result = from_roman(to_roman(n))
            self.assertEqual(result, n)
            self.assertIsInstance(result, int)


if __name__ == "__main__":
    unittest.main()
