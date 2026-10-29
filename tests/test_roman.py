"""Tests for sandbox.roman: to_roman and from_roman over 1..3999."""

import unittest
from itertools import product

from sandbox.roman import from_roman, to_roman


class RomanTest(unittest.TestCase):
    def test_to_roman_returns_a_canonical_uppercase_roman_numeral(self) -> None:
        for n in range(1, 4000):
            s = to_roman(n)
            self.assertIsInstance(s, str)
            self.assertTrue(s)
            self.assertTrue(all(c in "IVXLCDM" for c in s))

    def test_to_roman_is_unique_per_integer(self) -> None:
        self.assertEqual(len({to_roman(n) for n in range(1, 4000)}), 3999)

    def test_from_roman_round_trips_to_roman_over_the_full_range(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)

    def test_from_roman_returns_the_integer_for_every_valid_output(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)
        self.assertEqual(from_roman("M"), 1000)

    def test_from_roman_rejects_every_non_valid_one_to_four_character_string(self) -> None:
        valid = {to_roman(n) for n in range(1, 4000)}
        for length in range(1, 5):
            for combo in product("IVXLCDM", repeat=length):
                s = "".join(combo)
                if s in valid:
                    self.assertIsInstance(from_roman(s), int)
                else:
                    with self.assertRaises(ValueError) as ctx:
                        from_roman(s)
                    self.assertIn("not a valid Roman numeral", str(ctx.exception))

    def test_from_roman_rejects_non_alphabet_one_to_four_character_strings(self) -> None:
        for s in ("iv", "I V", "123", "ZZ"):
            with self.assertRaises(ValueError) as ctx:
                from_roman(s)
            self.assertIn("not a valid Roman numeral", str(ctx.exception))

    def test_from_roman_rejects_the_empty_string(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("")
        self.assertIn("not a valid Roman numeral", str(ctx.exception))

    def test_to_roman_raises_out_of_range_for_every_integer_outside_1_to_3999(self) -> None:
        for n in (0, -1, -1000, 4000, 4001, 10**6, False):
            with self.assertRaises(ValueError) as ctx:
                to_roman(n)
            self.assertIn("out of range", str(ctx.exception))
        self.assertEqual(to_roman(True), "I")

    def test_to_roman_raises_value_error_not_type_error_for_non_int_input(self) -> None:
        for n in ("x", 1.5):
            with self.assertRaises(ValueError) as ctx:
                to_roman(n)
            self.assertIn("out of range", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
