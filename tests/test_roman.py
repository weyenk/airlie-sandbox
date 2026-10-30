import itertools
import unittest

from sandbox.roman import from_roman, to_roman


class RomanTest(unittest.TestCase):
    def test_to_roman_returns_a_valid_roman_string_for_every_n_from_1_to_3999(self) -> None:
        for n in range(1, 4000):
            numeral = to_roman(n)
            self.assertIsInstance(numeral, str)
            self.assertTrue(1 <= len(numeral) <= 15)
            self.assertTrue(set(numeral) <= set("IVXLCDM"))

    def test_to_roman_pins_the_request_examples(self) -> None:
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(888), "DCCCLXXXVIII")
        self.assertEqual(to_roman(900), "CM")
        self.assertEqual(to_roman(1994), "MCMXCIV")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_to_roman_results_are_all_distinct_over_1_to_3999(self) -> None:
        self.assertEqual(len({to_roman(n) for n in range(1, 4000)}), 3999)

    def test_to_roman_raises_value_error_outside_1_to_3999_and_succeeds_at_the_boundaries(self) -> None:
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")
        for n in (0, -1, 4000, -100, 100000):
            with self.assertRaises(ValueError):
                to_roman(n)

    def test_to_roman_raises_value_error_for_non_integer_input(self) -> None:
        for value in (1.5, "IV", None, True, False):
            with self.assertRaises(ValueError):
                to_roman(value)

    def test_from_roman_round_trips_every_n_from_1_to_3999(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)

    def test_from_roman_returns_the_original_n_for_every_string_to_roman_produces(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)

    def test_from_roman_pins_the_inverse_request_examples(self) -> None:
        self.assertEqual(from_roman("IV"), 4)
        self.assertEqual(from_roman("CM"), 900)
        self.assertEqual(from_roman("MCMXCIV"), 1994)
        self.assertEqual(from_roman("MMMCMXCIX"), 3999)

    def test_from_roman_accepts_exactly_the_valid_set_over_all_1_to_4_length_alphabet_strings(self) -> None:
        valid = {to_roman(n) for n in range(1, 4000)}
        self.assertEqual(len(valid), 3999)
        expected = {numeral: n for n in range(1, 4000) for numeral in (to_roman(n),)}
        for length in range(1, 5):
            for letters in itertools.product("IVXLCDM", repeat=length):
                numeral = "".join(letters)
                if numeral in valid:
                    self.assertEqual(from_roman(numeral), expected[numeral])
                else:
                    with self.assertRaises(ValueError):
                        from_roman(numeral)

    def test_from_roman_raises_value_error_on_the_empty_string(self) -> None:
        with self.assertRaises(ValueError):
            from_roman("")

    def test_from_roman_raises_value_error_on_lowercase_and_whitespace_padded_input(self) -> None:
        for s in ("iv", "mmxx", "Iv", " IV", "IV "):
            with self.assertRaises(ValueError):
                from_roman(s)

    def test_from_roman_raises_value_error_on_non_canonical_strings_of_varying_lengths(self) -> None:
        for s in ("IIII", "VV", "DD", "IL", "IC", "ICM", "MMMM", "0", "10"):
            with self.assertRaises(ValueError):
                from_roman(s)

    def test_from_roman_raises_value_error_for_non_string_input(self) -> None:
        for value in (14, None, 4.0, True):
            with self.assertRaises(ValueError):
                from_roman(value)


if __name__ == "__main__":
    unittest.main()
