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

    def test_full_range_round_trip(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(sandbox.roman.from_roman(sandbox.roman.to_roman(n)), n)

    def test_from_roman_direct_decode_pins(self) -> None:
        self.assertEqual(sandbox.roman.from_roman("MCMXCIV"), 1994)
        self.assertEqual(sandbox.roman.from_roman("MMMCMXCIX"), 3999)
        self.assertEqual(sandbox.roman.from_roman("IV"), 4)
        self.assertEqual(sandbox.roman.from_roman("IX"), 9)
        self.assertEqual(sandbox.roman.from_roman("XL"), 40)
        self.assertEqual(sandbox.roman.from_roman("XC"), 90)
        self.assertEqual(sandbox.roman.from_roman("CD"), 400)
        self.assertEqual(sandbox.roman.from_roman("CM"), 900)

    def test_from_roman_reencode_stability(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(
                sandbox.roman.to_roman(sandbox.roman.from_roman(sandbox.roman.to_roman(n))),
                sandbox.roman.to_roman(n),
            )

    def test_from_roman_malformed_raises(self) -> None:
        malformed = (
            "",       # empty
            "xiv",    # lowercase
            "A",      # non-roman character
            "VIV",    # V before a larger digit
            "IC",     # I before anything other than V or X
            "IIII",   # I repeated more than three times
            "LL",     # L before a larger digit / repeated
            "MMMM",   # value 4000, outside 1..3999
        )
        for bad in malformed:
            with self.assertRaises(ValueError):
                sandbox.roman.from_roman(bad)

    def test_from_roman_result_in_range(self) -> None:
        for numeral in ("I", "IV", "IX", "XL", "XC", "CD", "CM", "M", "MCMXCIV", "MMMCMXCIX"):
            n = sandbox.roman.from_roman(numeral)
            self.assertIsInstance(n, int)
            self.assertGreaterEqual(n, 1)
            self.assertLessEqual(n, 3999)


if __name__ == "__main__":
    unittest.main()
