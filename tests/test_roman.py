import unittest

from sandbox.roman import to_roman, from_roman


class RomanTest(unittest.TestCase):
    def test_to_roman_1_returns_I(self) -> None:
        self.assertEqual(to_roman(1), "I")

    def test_to_roman_4_returns_IV(self) -> None:
        self.assertEqual(to_roman(4), "IV")

    def test_to_roman_9_returns_IX(self) -> None:
        self.assertEqual(to_roman(9), "IX")

    def test_to_roman_40_returns_XL(self) -> None:
        self.assertEqual(to_roman(40), "XL")

    def test_to_roman_90_returns_XC(self) -> None:
        self.assertEqual(to_roman(90), "XC")

    def test_to_roman_400_returns_CD(self) -> None:
        self.assertEqual(to_roman(400), "CD")

    def test_to_roman_900_returns_CM(self) -> None:
        self.assertEqual(to_roman(900), "CM")

    def test_to_roman_3999_returns_MMMCMXCIX(self) -> None:
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_to_roman_1984_returns_MCMLXXXIV(self) -> None:
        self.assertEqual(to_roman(1984), "MCMLXXXIV")

    def test_to_roman_0_raises_ValueError(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            to_roman(0)
        self.assertEqual(str(ctx.exception), "n must be between 1 and 3999")

    def test_to_roman_4000_raises_ValueError(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            to_roman(4000)
        self.assertEqual(str(ctx.exception), "n must be between 1 and 3999")

    def test_to_roman_non_int_raises_ValueError(self) -> None:
        for bad in (4.0, "4"):
            with self.assertRaises(ValueError) as ctx:
                to_roman(bad)
            self.assertEqual(str(ctx.exception), "n must be between 1 and 3999")

    def test_from_roman_I_returns_1(self) -> None:
        self.assertEqual(from_roman("I"), 1)

    def test_from_roman_IV_returns_4(self) -> None:
        self.assertEqual(from_roman("IV"), 4)

    def test_from_roman_IX_returns_9(self) -> None:
        self.assertEqual(from_roman("IX"), 9)

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

    def test_from_roman_MCMLXXXIV_returns_1984(self) -> None:
        self.assertEqual(from_roman("MCMLXXXIV"), 1984)

    def test_from_roman_IIII_raises_ValueError(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("IIII")
        self.assertEqual(str(ctx.exception), "invalid Roman numeral: IIII")

    def test_from_roman_VV_raises_ValueError(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("VV")
        self.assertEqual(str(ctx.exception), "invalid Roman numeral: VV")

    def test_from_roman_IC_raises_ValueError(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("IC")
        self.assertEqual(str(ctx.exception), "invalid Roman numeral: IC")

    def test_from_roman_empty_raises_ValueError(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("")
        self.assertEqual(str(ctx.exception), "invalid Roman numeral: ")

    def test_from_roman_lowercase_iv_raises_ValueError(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("iv")
        self.assertEqual(str(ctx.exception), "invalid Roman numeral: iv")

    def test_from_roman_I4_raises_ValueError(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("I4")
        self.assertEqual(str(ctx.exception), "invalid Roman numeral: I4")

    def test_from_roman_non_str_raises_ValueError(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman(4)
        self.assertEqual(str(ctx.exception), "invalid Roman numeral: 4")

    def test_round_trip_all_values_1_to_3999(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)


if __name__ == "__main__":
    unittest.main()
