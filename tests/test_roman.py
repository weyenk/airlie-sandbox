import itertools
import unittest

from sandbox.roman import from_roman, to_roman


class ToRomanTest(unittest.TestCase):
    def test_import_sandbox_roman_exposes_both_functions(self) -> None:
        import sandbox.roman as roman

        self.assertTrue(hasattr(roman, "to_roman"))
        self.assertTrue(hasattr(roman, "from_roman"))
        self.assertIsInstance(to_roman(1), str)
        self.assertIsInstance(from_roman("I"), int)

    def test_to_roman_matches_the_pinned_literals(self) -> None:
        for number, numeral in {
            1: "I",
            4: "IV",
            9: "IX",
            14: "XIV",
            40: "XL",
            88: "LXXXVIII",
            90: "XC",
            400: "CD",
            900: "CM",
            1994: "MCMXCIV",
            3999: "MMMCMXCIX",
        }.items():
            with self.subTest(number=number):
                result = to_roman(number)
                self.assertIsInstance(result, str)
                self.assertEqual(result, numeral)

    def test_to_roman_round_trips_over_the_whole_range_1_to_3999(self) -> None:
        for n in range(1, 4000):
            with self.subTest(n=n):
                result = to_roman(n)
                self.assertIsInstance(result, str)
                self.assertEqual(from_roman(result), n)

    def test_to_roman_output_uses_only_the_seven_roman_characters(self) -> None:
        allowed = {"M", "C", "D", "L", "X", "V", "I"}
        for n in range(1, 4000):
            with self.subTest(n=n):
                self.assertLessEqual(set(to_roman(n)), allowed)

    def test_to_roman_raises_value_error_out_of_range(self) -> None:
        for n in (0, -1, -3000, 4000, 10000):
            with self.subTest(n=n):
                with self.assertRaises(ValueError):
                    to_roman(n)


class FromRomanTest(unittest.TestCase):
    def test_from_roman_matches_the_pinned_literals(self) -> None:
        for numeral, number in {
            "I": 1,
            "X": 10,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
            "MCMXCIV": 1994,
            "MMMCMXCIX": 3999,
        }.items():
            with self.subTest(numeral=numeral):
                result = from_roman(numeral)
                self.assertIsInstance(result, int)
                self.assertEqual(result, number)

    def test_from_roman_of_to_roman_returns_the_original_int(self) -> None:
        for n in range(1, 4000):
            with self.subTest(n=n):
                result = from_roman(to_roman(n))
                self.assertIsInstance(result, int)
                self.assertEqual(result, n)

    def test_from_roman_refuses_every_1_to_4_char_string_not_in_the_valid_set(self) -> None:
        valid = {to_roman(n) for n in range(1, 4000)}
        alphabet = "MCDLXVI"
        for length in range(1, 5):
            for chars in itertools.product(alphabet, repeat=length):
                s = "".join(chars)
                if s in valid:
                    self.assertIsInstance(from_roman(s), int)
                else:
                    with self.subTest(s=s):
                        with self.assertRaises(ValueError):
                            from_roman(s)

    def test_from_roman_empty_string_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            from_roman("")

    def test_from_roman_raises_value_error_for_strings_of_five_or_more_chars(self) -> None:
        for s in ("I" * 5, "I" * 6, "M" * 5, "M" * 6, "I" * 500, "MMMMMM"):
            with self.subTest(s=s):
                with self.assertRaises(ValueError):
                    from_roman(s)


if __name__ == "__main__":
    unittest.main()
