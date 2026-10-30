"""Tests for sandbox.roman: Roman numeral conversion for 1..3999."""

import itertools
import unittest

from sandbox.roman import from_roman, to_roman

REFUSAL = "not a valid Roman numeral"
ALPHABET = "IVXLMCD"


class RomanTest(unittest.TestCase):
    def test_to_roman_round_trips_for_every_integer_in_1_to_3999(self) -> None:
        valid = {to_roman(k) for k in range(1, 4000)}
        for n in range(1, 4000):
            s = to_roman(n)
            self.assertIsInstance(s, str)
            self.assertEqual(from_roman(s), n)
            self.assertIn(s, valid)

    def test_from_roman_returns_n_exactly_for_each_valid_numeral(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)

    def test_to_roman_raises_for_every_out_of_range_integer(self) -> None:
        for n in list(range(-1000, 0)) + list(range(4000, 10001)):
            with self.assertRaises(ValueError) as ctx:
                to_roman(n)
            self.assertIn(REFUSAL, str(ctx.exception))

    def test_to_roman_raises_for_the_requested_examples_0_neg1_4000_10000(self) -> None:
        for n in (0, -1, 4000, 10000):
            with self.assertRaises(ValueError) as ctx:
                to_roman(n)
            self.assertIn(REFUSAL, str(ctx.exception))

    def test_from_roman_accepts_exactly_the_valid_outputs_for_every_1_to_4_character_string(self) -> None:
        valid = {to_roman(n): n for n in range(1, 4000)}
        for length in range(1, 5):
            for chars in itertools.product(ALPHABET, repeat=length):
                s = "".join(chars)
                if s in valid:
                    self.assertEqual(from_roman(s), valid[s])
                else:
                    with self.assertRaises(ValueError) as ctx:
                        from_roman(s)
                    self.assertIn(REFUSAL, str(ctx.exception))

    def test_from_roman_raises_for_the_requested_malformed_examples(self) -> None:
        for s in ("A", "IIII", "IC", "IM", "MMMM", "VX"):
            with self.assertRaises(ValueError) as ctx:
                from_roman(s)
            self.assertIn(REFUSAL, str(ctx.exception))

    def test_from_roman_raises_for_empty_string(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("")
        self.assertIn(REFUSAL, str(ctx.exception))

    def test_pinned_concrete_pair_1994_is_mcmxciv(self) -> None:
        self.assertEqual(to_roman(1994), "MCMXCIV")
        self.assertEqual(from_roman("MCMXCIV"), 1994)

    def test_boundary_values_1_and_3999_convert_and_0_and_4000_raise(self) -> None:
        self.assertEqual(from_roman("I"), 1)
        self.assertEqual(from_roman("MMMCMXCIX"), 3999)
        for n in (0, 4000):
            with self.assertRaises(ValueError) as ctx:
                to_roman(n)
            self.assertIn(REFUSAL, str(ctx.exception))

    def test_to_roman_raises_for_non_integer_inputs_true_and_1_5(self) -> None:
        for value in (True, 1.5):
            with self.assertRaises(ValueError) as ctx:
                to_roman(value)
            self.assertIn(REFUSAL, str(ctx.exception))

    def test_from_roman_raises_for_non_string_and_lowercase_inputs(self) -> None:
        for value in (1994, "mcmxciv"):
            with self.assertRaises(ValueError) as ctx:
                from_roman(value)
            self.assertIn(REFUSAL, str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
