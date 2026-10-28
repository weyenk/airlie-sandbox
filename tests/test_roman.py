import unittest

import sandbox.roman


class RomanTest(unittest.TestCase):
    def test_to_roman_returns_canonical_numeral_for_known_values(self) -> None:
        for value, numeral in [
            (1, "I"),
            (4, "IV"),
            (9, "IX"),
            (40, "XL"),
            (90, "XC"),
            (400, "CD"),
            (900, "CM"),
            (1994, "MCMXCIV"),
            (3999, "MMMCMXCIX"),
        ]:
            self.assertEqual(sandbox.roman.to_roman(value), numeral)

    def test_to_roman_raises_value_error_for_out_of_range(self) -> None:
        for value in (0, -1, 4000):
            with self.assertRaisesRegex(ValueError, "1 to 3999"):
                sandbox.roman.to_roman(value)

    def test_to_roman_raises_value_error_for_non_int(self) -> None:
        for value in ("IV", 4.0, None, True):
            with self.assertRaisesRegex(ValueError, "int"):
                sandbox.roman.to_roman(value)

    def test_from_roman_returns_value_for_known_numerals(self) -> None:
        for numeral, value in [
            ("I", 1),
            ("IV", 4),
            ("IX", 9),
            ("XL", 40),
            ("XC", 90),
            ("CM", 900),
            ("MCMXCIV", 1994),
            ("MMMCMXCIX", 3999),
        ]:
            self.assertEqual(sandbox.roman.from_roman(numeral), value)

    def test_from_roman_raises_value_error_for_malformed(self) -> None:
        for numeral in ("IIII", "VV", "IC", "IM", "IXI", "", "IVX"):
            with self.assertRaisesRegex(ValueError, "malformed"):
                sandbox.roman.from_roman(numeral)

    def test_from_roman_raises_value_error_for_out_of_range(self) -> None:
        with self.assertRaisesRegex(ValueError, "1 to 3999"):
            sandbox.roman.from_roman("MMMM")

    def test_from_roman_raises_value_error_for_non_str(self) -> None:
        for value in (1994, None, b"IV"):
            with self.assertRaisesRegex(ValueError, "str"):
                sandbox.roman.from_roman(value)

    def test_from_roman_round_trips_to_roman_for_all_values(self) -> None:
        for value in range(1, 4000):
            self.assertEqual(sandbox.roman.from_roman(sandbox.roman.to_roman(value)), value)


if __name__ == "__main__":
    unittest.main()
