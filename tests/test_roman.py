import unittest

from sandbox.roman import from_roman, to_roman


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

    def test_to_roman_1994_returns_MCMXCIV(self) -> None:
        self.assertEqual(to_roman(1994), "MCMXCIV")

    def test_to_roman_3999_returns_MMMCMXCIX(self) -> None:
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_to_roman_0_raises_ValueError(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            to_roman(0)
        self.assertEqual(str(ctx.exception), "n must be an integer between 1 and 3999")

    def test_to_roman_4000_raises_ValueError(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            to_roman(4000)
        self.assertEqual(str(ctx.exception), "n must be an integer between 1 and 3999")

    def test_to_roman_negative_raises_ValueError(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            to_roman(-1)
        self.assertEqual(str(ctx.exception), "n must be an integer between 1 and 3999")

    def test_to_roman_float_raises_ValueError(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            to_roman(1.5)
        self.assertEqual(str(ctx.exception), "n must be an integer between 1 and 3999")

    def test_to_roman_string_raises_ValueError(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            to_roman("4")
        self.assertEqual(str(ctx.exception), "n must be an integer between 1 and 3999")

    def test_from_roman_I_returns_1(self) -> None:
        self.assertEqual(from_roman("I"), 1)

    def test_from_roman_IV_returns_4(self) -> None:
        self.assertEqual(from_roman("IV"), 4)

    def test_from_roman_MCMXCIV_returns_1994(self) -> None:
        self.assertEqual(from_roman("MCMXCIV"), 1994)

    def test_from_roman_MMMCMXCIX_returns_3999(self) -> None:
        self.assertEqual(from_roman("MMMCMXCIX"), 3999)

    def test_from_roman_IIII_raises_ValueError(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("IIII")
        self.assertEqual(str(ctx.exception), "not a valid Roman numeral")

    def test_from_roman_VIV_raises_ValueError(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("VIV")
        self.assertEqual(str(ctx.exception), "not a valid Roman numeral")

    def test_from_roman_empty_raises_ValueError(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("")
        self.assertEqual(str(ctx.exception), "not a valid Roman numeral")

    def test_from_roman_lowercase_raises_ValueError(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("iv")
        self.assertEqual(str(ctx.exception), "not a valid Roman numeral")

    def test_from_roman_IVX_raises_ValueError(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("IVX")
        self.assertEqual(str(ctx.exception), "not a valid Roman numeral")

    def test_from_roman_digits_raises_ValueError(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("123")
        self.assertEqual(str(ctx.exception), "not a valid Roman numeral")

    def test_from_roman_non_string_raises_ValueError(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman(123)
        self.assertEqual(str(ctx.exception), "not a valid Roman numeral")

    def test_from_roman_MMMM_raises_ValueError(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("MMMM")
        self.assertEqual(str(ctx.exception), "not a valid Roman numeral")

    def test_round_trip_1_to_3999(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)


if __name__ == "__main__":
    unittest.main()
