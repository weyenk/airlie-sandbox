import unittest

import sandbox.roman


class RomanTest(unittest.TestCase):
    def test_to_roman_of_1_returns_I(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(1), "I")

    def test_to_roman_of_4_returns_IV(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(4), "IV")

    def test_to_roman_of_9_returns_IX(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(9), "IX")

    def test_to_roman_of_40_returns_XL(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(40), "XL")

    def test_to_roman_of_90_returns_XC(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(90), "XC")

    def test_to_roman_of_400_returns_CD(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(400), "CD")

    def test_to_roman_of_900_returns_CM(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(900), "CM")

    def test_to_roman_of_1984_returns_MCMXCIV(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(1984), "MCMXCIV")

    def test_to_roman_of_3999_returns_MMMCMXCIX(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(3999), "MMMCMXCIX")

    def test_to_roman_of_0_raises_ValueError_with_range_message(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            sandbox.roman.to_roman(0)
        self.assertEqual(str(ctx.exception), "n must be an integer between 1 and 3999")

    def test_to_roman_of_4000_raises_ValueError_with_range_message(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            sandbox.roman.to_roman(4000)
        self.assertEqual(str(ctx.exception), "n must be an integer between 1 and 3999")

    def test_to_roman_of_negative_1_raises_ValueError_with_range_message(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            sandbox.roman.to_roman(-1)
        self.assertEqual(str(ctx.exception), "n must be an integer between 1 and 3999")

    def test_from_roman_of_MMMCMXCIX_returns_3999(self) -> None:
        self.assertEqual(sandbox.roman.from_roman("MMMCMXCIX"), 3999)

    def test_from_roman_of_MCMXCIV_returns_1984(self) -> None:
        self.assertEqual(sandbox.roman.from_roman("MCMXCIV"), 1984)

    def test_from_roman_of_IV_returns_4(self) -> None:
        self.assertEqual(sandbox.roman.from_roman("IV"), 4)

    def test_from_roman_of_I_returns_1(self) -> None:
        self.assertEqual(sandbox.roman.from_roman("I"), 1)

    def test_from_roman_of_empty_string_raises_ValueError_with_invalid_message(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            sandbox.roman.from_roman("")
        self.assertEqual(str(ctx.exception), "not a valid Roman numeral")

    def test_from_roman_of_IIII_raises_ValueError_with_invalid_message(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            sandbox.roman.from_roman("IIII")
        self.assertEqual(str(ctx.exception), "not a valid Roman numeral")

    def test_from_roman_of_VIV_raises_ValueError_with_invalid_message(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            sandbox.roman.from_roman("VIV")
        self.assertEqual(str(ctx.exception), "not a valid Roman numeral")

    def test_from_roman_of_abc_raises_ValueError_with_invalid_message(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            sandbox.roman.from_roman("abc")
        self.assertEqual(str(ctx.exception), "not a valid Roman numeral")

    def test_from_roman_of_MMMM_raises_ValueError_with_invalid_message(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            sandbox.roman.from_roman("MMMM")
        self.assertEqual(str(ctx.exception), "not a valid Roman numeral")

    def test_from_roman_round_trips_to_roman_for_every_n_in_1_to_3999(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(sandbox.roman.from_roman(sandbox.roman.to_roman(n)), n)


if __name__ == "__main__":
    unittest.main()
