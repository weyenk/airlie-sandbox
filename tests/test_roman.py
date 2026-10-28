import unittest

from sandbox.roman import from_roman, to_roman


class ToRomanTest(unittest.TestCase):
    def test_to_roman_returns_canonical_subtractive_numerals(self) -> None:
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(9), "IX")
        self.assertEqual(to_roman(14), "XIV")
        self.assertEqual(to_roman(40), "XL")
        self.assertEqual(to_roman(90), "XC")
        self.assertEqual(to_roman(400), "CD")
        self.assertEqual(to_roman(900), "CM")
        self.assertEqual(to_roman(1994), "MCMXCIV")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_to_roman_below_one_raises_value_error(self) -> None:
        for n in (0, -5):
            with self.assertRaises(ValueError) as ctx:
                to_roman(n)
            self.assertIn("1 to 3999", str(ctx.exception))

    def test_to_roman_above_3999_raises_value_error(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            to_roman(4000)
        self.assertIn("1 to 3999", str(ctx.exception))


class FromRomanTest(unittest.TestCase):
    def test_from_roman_decodes_well_formed_numerals(self) -> None:
        self.assertEqual(from_roman("I"), 1)
        self.assertEqual(from_roman("IV"), 4)
        self.assertEqual(from_roman("MCMXCIV"), 1994)
        self.assertEqual(from_roman("MMMCMXCIX"), 3999)

    def test_from_roman_malformed_raises_value_error(self) -> None:
        for s in ("", "iv", "A", "IIII", "IL", "IC", "VX", "VV", "LL", "DD", "MMMM"):
            with self.assertRaises(ValueError) as ctx:
                from_roman(s)
            self.assertIn("malformed", str(ctx.exception))

    def test_round_trip_identity_over_whole_domain(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)


if __name__ == "__main__":
    unittest.main()
