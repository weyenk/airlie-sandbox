import unittest

from sandbox.roman import to_roman, from_roman


class RomanTest(unittest.TestCase):
    def test_import_exposes_to_roman_and_from_roman(self) -> None:
        self.assertTrue(callable(to_roman))
        self.assertTrue(callable(from_roman))
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(from_roman("I"), 1)

    def test_to_roman_returns_canonical_subtractive_forms(self) -> None:
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(9), "IX")
        self.assertEqual(to_roman(40), "XL")
        self.assertEqual(to_roman(90), "XC")
        self.assertEqual(to_roman(400), "CD")
        self.assertEqual(to_roman(900), "CM")
        self.assertEqual(to_roman(1000), "M")
        self.assertEqual(to_roman(1994), "MCMXCIV")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_to_roman_rejects_out_of_range_with_message(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            to_roman(0)
        self.assertIn("not in 1..3999", str(ctx.exception))
        with self.assertRaises(ValueError) as ctx:
            to_roman(-1)
        self.assertIn("not in 1..3999", str(ctx.exception))
        with self.assertRaises(ValueError) as ctx:
            to_roman(4000)
        self.assertIn("not in 1..3999", str(ctx.exception))

    def test_from_roman_parses_canonical_numerals(self) -> None:
        self.assertEqual(from_roman("I"), 1)
        self.assertEqual(from_roman("IV"), 4)
        self.assertEqual(from_roman("IX"), 9)
        self.assertEqual(from_roman("XL"), 40)
        self.assertEqual(from_roman("XC"), 90)
        self.assertEqual(from_roman("CM"), 900)
        self.assertEqual(from_roman("M"), 1000)
        self.assertEqual(from_roman("MCMXCIV"), 1994)
        self.assertEqual(from_roman("MMMCMXCIX"), 3999)

    def test_from_roman_rejects_each_malformed_form_with_message(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("IIII")
        self.assertIn("not a valid Roman numeral", str(ctx.exception))
        with self.assertRaises(ValueError) as ctx:
            from_roman("VV")
        self.assertIn("not a valid Roman numeral", str(ctx.exception))
        with self.assertRaises(ValueError) as ctx:
            from_roman("LL")
        self.assertIn("not a valid Roman numeral", str(ctx.exception))
        with self.assertRaises(ValueError) as ctx:
            from_roman("IC")
        self.assertIn("not a valid Roman numeral", str(ctx.exception))
        with self.assertRaises(ValueError) as ctx:
            from_roman("IM")
        self.assertIn("not a valid Roman numeral", str(ctx.exception))
        with self.assertRaises(ValueError) as ctx:
            from_roman("XM")
        self.assertIn("not a valid Roman numeral", str(ctx.exception))
        with self.assertRaises(ValueError) as ctx:
            from_roman("DM")
        self.assertIn("not a valid Roman numeral", str(ctx.exception))
        with self.assertRaises(ValueError) as ctx:
            from_roman("CDM")
        self.assertIn("not a valid Roman numeral", str(ctx.exception))
        with self.assertRaises(ValueError) as ctx:
            from_roman("MMMM")
        self.assertIn("not a valid Roman numeral", str(ctx.exception))
        with self.assertRaises(ValueError) as ctx:
            from_roman("")
        self.assertIn("not a valid Roman numeral", str(ctx.exception))
        with self.assertRaises(ValueError) as ctx:
            from_roman("abc")
        self.assertIn("not a valid Roman numeral", str(ctx.exception))

    def test_round_trip_holds_for_every_n_in_range(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)


if __name__ == "__main__":
    unittest.main()
