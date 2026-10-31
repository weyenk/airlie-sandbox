import itertools
import unittest

from sandbox.roman import from_roman, to_roman

ALPHABET = "IVXLCDM"


class RomanTest(unittest.TestCase):
    def test_to_roman_builds_standard_subtractive_numerals_and_round_trips_for_every_n_in_1_to_3999(self) -> None:
        for n in range(1, 4000):
            numeral = to_roman(n)
            self.assertIsInstance(numeral, str)
            self.assertTrue(all(ch in ALPHABET for ch in numeral))
            self.assertEqual(from_roman(to_roman(n)), n)
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(9), "IX")
        self.assertEqual(to_roman(40), "XL")
        self.assertEqual(to_roman(90), "XC")
        self.assertEqual(to_roman(400), "CD")
        self.assertEqual(to_roman(900), "CM")
        self.assertEqual(to_roman(1994), "MCMXCIV")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_to_roman_raises_value_error_for_out_of_range_n(self) -> None:
        for n in (0, -5, 4000, 100000):
            with self.assertRaises(ValueError) as ctx:
                to_roman(n)
            self.assertIn("n must be in 1..3999", str(ctx.exception))
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_to_roman_raises_value_error_for_non_integer_n(self) -> None:
        for n in (4.5, "IV", True, None):
            with self.assertRaises(ValueError) as ctx:
                to_roman(n)
            self.assertIn("n must be an integer", str(ctx.exception))

    def test_module_exposes_to_roman_and_from_roman_and_bad_input_raises_value_error(self) -> None:
        import sandbox.roman as roman

        self.assertTrue(callable(roman.to_roman))
        self.assertTrue(callable(roman.from_roman))
        with self.assertRaises(ValueError):
            roman.to_roman(0)
        with self.assertRaises(ValueError):
            roman.from_roman("")

    def test_from_roman_returns_the_unique_n_for_every_valid_output(self) -> None:
        valid = {to_roman(n): n for n in range(1, 4000)}
        self.assertEqual(len(valid), 3999)
        for s, n in valid.items():
            self.assertEqual(from_roman(s), n)

    def test_from_roman_accepts_exactly_the_valid_outputs_among_all_strings_of_length_1_to_4(self) -> None:
        valid = {to_roman(n): n for n in range(1, 4000)}
        seen_valid = 0
        for length in range(1, 5):
            for chars in itertools.product(ALPHABET, repeat=length):
                s = "".join(chars)
                if s in valid:
                    seen_valid += 1
                    self.assertEqual(from_roman(s), valid[s])
                else:
                    with self.assertRaises(ValueError) as ctx:
                        from_roman(s)
                    self.assertIn("invalid numeral", str(ctx.exception))
        self.assertEqual(seen_valid, 264)

    def test_from_roman_raises_value_error_for_empty_string(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("")
        self.assertIn("must not be empty", str(ctx.exception))

    def test_from_roman_raises_value_error_for_strings_with_foreign_characters(self) -> None:
        for s in ("IVa", "iv", "I V"):
            with self.assertRaises(ValueError) as ctx:
                from_roman(s)
            self.assertIn("invalid numeral", str(ctx.exception))

    def test_from_roman_raises_value_error_for_non_string_s(self) -> None:
        for s in (4, None, ["I"]):
            with self.assertRaises(ValueError) as ctx:
                from_roman(s)
            self.assertIn("s must be a string", str(ctx.exception))
        self.assertEqual(from_roman("I"), 1)
        self.assertEqual(from_roman("MMMCMXCIX"), 3999)


if __name__ == "__main__":
    unittest.main()
