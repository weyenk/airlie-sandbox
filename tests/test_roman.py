import itertools
import unittest

from sandbox.roman import from_roman, to_roman


class RomanTest(unittest.TestCase):
    def test_to_roman_returns_the_standard_numeral_for_1_and_3999(self) -> None:
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_to_roman_returns_the_subtractive_pairs_for_the_convention_examples(self) -> None:
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(9), "IX")
        self.assertEqual(to_roman(40), "XL")
        self.assertEqual(to_roman(90), "XC")
        self.assertEqual(to_roman(400), "CD")
        self.assertEqual(to_roman(900), "CM")
        self.assertEqual(to_roman(1994), "MCMXCIV")

    def test_from_roman_round_trips_every_integer_from_1_to_3999(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)

    def test_to_roman_raises_value_error_for_0_negatives_and_4000(self) -> None:
        for n in (0, -1, 4000):
            with self.assertRaises(ValueError):
                to_roman(n)

    def test_to_roman_raises_value_error_for_non_int_inputs(self) -> None:
        for value in (1.5, "x"):
            with self.assertRaises(ValueError):
                to_roman(value)

    def test_from_roman_raises_value_error_for_the_empty_string(self) -> None:
        with self.assertRaises(ValueError):
            from_roman("")

    def test_from_roman_raises_value_error_for_every_invalid_string_of_length_1_to_4(self) -> None:
        valid = {to_roman(n) for n in range(1, 4000)}
        self.assertEqual(len(valid), 3999)
        for length in range(1, 5):
            for chars in itertools.product("MCDXLVI", repeat=length):
                s = "".join(chars)
                if s in valid:
                    continue
                with self.assertRaises(ValueError):
                    from_roman(s)

    def test_from_roman_raises_value_error_for_strings_with_non_roman_characters(self) -> None:
        for s in ("A", "I2", "i"):
            with self.assertRaises(ValueError):
                from_roman(s)

    def test_from_roman_raises_value_error_for_long_strings_that_are_not_valid_outputs(self) -> None:
        valid = {to_roman(n) for n in range(1, 4000)}
        self.assertEqual(len(valid), 3999)
        # "MMMM" (length 4) is a secondary pin here; its primary proof is the AC5 exhaustive loop.
        with self.assertRaises(ValueError):
            from_roman("MMMM")
        for s in ("MMMMM", "MMMMC", "ICICI"):
            self.assertNotIn(s, valid)
            with self.assertRaises(ValueError):
                from_roman(s)
        for chars in itertools.product("MCDXLVI", repeat=5):
            s = "".join(chars)
            if s in valid:
                continue
            with self.assertRaises(ValueError):
                from_roman(s)

    def test_from_roman_round_trips_a_long_valid_output(self) -> None:
        self.assertEqual(to_roman(3888), "MMMDCCCLXXXVIII")
        self.assertEqual(from_roman("MMMDCCCLXXXVIII"), 3888)


if __name__ == "__main__":
    unittest.main()
