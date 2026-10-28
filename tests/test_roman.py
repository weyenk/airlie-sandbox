import unittest

import sandbox.roman


class RomanTest(unittest.TestCase):
    def test_to_roman_1_returns_I(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(1), "I")

    def test_to_roman_4_returns_IV(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(4), "IV")

    def test_to_roman_9_returns_IX(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(9), "IX")

    def test_to_roman_40_returns_XL(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(40), "XL")

    def test_to_roman_90_returns_XC(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(90), "XC")

    def test_to_roman_400_returns_CD(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(400), "CD")

    def test_to_roman_900_returns_CM(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(900), "CM")

    def test_to_roman_1994_returns_MCMXCIV(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(1994), "MCMXCIV")

    def test_to_roman_3999_returns_MMMCMXCIX(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(3999), "MMMCMXCIX")

    def test_to_roman_0_raises_range(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            sandbox.roman.to_roman(0)
        self.assertIn("between 1 and 3999", str(ctx.exception))

    def test_to_roman_4000_raises_range(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            sandbox.roman.to_roman(4000)
        self.assertIn("between 1 and 3999", str(ctx.exception))

    def test_to_roman_negative_raises_range(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            sandbox.roman.to_roman(-1)
        self.assertIn("between 1 and 3999", str(ctx.exception))

    def test_from_roman_I_returns_1(self) -> None:
        self.assertEqual(sandbox.roman.from_roman("I"), 1)

    def test_from_roman_IV_returns_4(self) -> None:
        self.assertEqual(sandbox.roman.from_roman("IV"), 4)

    def test_from_roman_IX_returns_9(self) -> None:
        self.assertEqual(sandbox.roman.from_roman("IX"), 9)

    def test_from_roman_XL_returns_40(self) -> None:
        self.assertEqual(sandbox.roman.from_roman("XL"), 40)

    def test_from_roman_XC_returns_90(self) -> None:
        self.assertEqual(sandbox.roman.from_roman("XC"), 90)

    def test_from_roman_CD_returns_400(self) -> None:
        self.assertEqual(sandbox.roman.from_roman("CD"), 400)

    def test_from_roman_CM_returns_900(self) -> None:
        self.assertEqual(sandbox.roman.from_roman("CM"), 900)

    def test_from_roman_MCMXCIV_returns_1994(self) -> None:
        self.assertEqual(sandbox.roman.from_roman("MCMXCIV"), 1994)

    def test_from_roman_MMMCMXCIX_returns_3999(self) -> None:
        self.assertEqual(sandbox.roman.from_roman("MMMCMXCIX"), 3999)

    def test_from_roman_IC_raises_malformed(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            sandbox.roman.from_roman("IC")
        self.assertIn("malformed", str(ctx.exception))

    def test_from_roman_IIII_raises_malformed(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            sandbox.roman.from_roman("IIII")
        self.assertIn("malformed", str(ctx.exception))

    def test_from_roman_empty_raises_malformed(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            sandbox.roman.from_roman("")
        self.assertIn("malformed", str(ctx.exception))

    def test_from_roman_abc_raises_malformed(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            sandbox.roman.from_roman("abc")
        self.assertIn("malformed", str(ctx.exception))

    def test_from_roman_MMMM_raises_range(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            sandbox.roman.from_roman("MMMM")
        self.assertIn("between 1 and 3999", str(ctx.exception))

    def test_to_roman_and_from_roman_are_inverses_over_1_to_3999(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(sandbox.roman.from_roman(sandbox.roman.to_roman(n)), n)


if __name__ == "__main__":
    unittest.main()
