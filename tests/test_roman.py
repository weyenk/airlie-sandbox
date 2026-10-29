import unittest

import sandbox.roman


class RomanTest(unittest.TestCase):
    def test_importing_sandbox_roman_exposes_both_callables(self) -> None:
        self.assertTrue(hasattr(sandbox.roman, "to_roman"))
        self.assertTrue(hasattr(sandbox.roman, "from_roman"))
        self.assertTrue(callable(sandbox.roman.to_roman))
        self.assertTrue(callable(sandbox.roman.from_roman))

    def test_to_roman_round_trips_every_integer_in_range(self) -> None:
        allowed = {"M", "D", "C", "L", "X", "V", "I"}
        for n in range(1, 4000):
            numeral = sandbox.roman.to_roman(n)
            self.assertIsInstance(numeral, str)
            self.assertLessEqual(set(numeral), allowed)
            self.assertEqual(sandbox.roman.from_roman(numeral), n)

    def test_to_roman_and_from_roman_agree_on_fixed_pairs(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(1994), "MCMXCIV")
        self.assertEqual(sandbox.roman.from_roman("IX"), 9)

    def test_to_roman_is_canonical_for_every_integer_in_range(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(
                sandbox.roman.to_roman(sandbox.roman.from_roman(sandbox.roman.to_roman(n))),
                sandbox.roman.to_roman(n),
            )

    def test_to_roman_rejects_out_of_range_integers(self) -> None:
        for n in (0, -1, -100, 4000, 4001, 100000):
            with self.assertRaises(ValueError) as ctx:
                sandbox.roman.to_roman(n)
            self.assertIn("n must be between 1 and 3999", str(ctx.exception))

    def test_from_roman_rejects_disallowed_characters(self) -> None:
        for s in ("A", "iv", "M1", "MMa", " "):
            with self.assertRaises(ValueError) as ctx:
                sandbox.roman.from_roman(s)
            self.assertIn("malformed Roman numeral", str(ctx.exception))

    def test_from_roman_rejects_subtractive_rule_violations(self) -> None:
        for s in (
            "IIII",
            "VV",
            "IL",
            "IC",
            "IM",
            "IVX",
            "VX",
            "XXXX",
            "CCCC",
            "MMMMM",
            "LL",
            "DD",
            "IXI",
            "XCX",
        ):
            with self.assertRaises(ValueError) as ctx:
                sandbox.roman.from_roman(s)
            self.assertIn("malformed Roman numeral", str(ctx.exception))

    def test_from_roman_rejects_well_formed_numeral_over_3999(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            sandbox.roman.from_roman("MMMM")
        self.assertIn("out of range 1 to 3999", str(ctx.exception))
        self.assertNotIn("malformed Roman numeral", str(ctx.exception))

    def test_from_roman_rejects_empty_string(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            sandbox.roman.from_roman("")
        self.assertIn("malformed Roman numeral", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
