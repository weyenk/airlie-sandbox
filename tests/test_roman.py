import inspect
import itertools
import unittest

from sandbox.roman import to_roman, from_roman


class RomanTest(unittest.TestCase):
    def test_both_functions_are_importable_callables_with_typed_signatures_and_one_line_docstrings(self) -> None:
        self.assertTrue(callable(to_roman))
        self.assertTrue(callable(from_roman))
        self.assertEqual(str(inspect.signature(to_roman)), "(n: int) -> str")
        self.assertEqual(str(inspect.signature(from_roman)), "(s: str) -> int")
        self.assertTrue(to_roman.__doc__)
        self.assertNotIn("\n", to_roman.__doc__.strip())
        self.assertTrue(from_roman.__doc__)
        self.assertNotIn("\n", from_roman.__doc__.strip())

    def test_to_roman_returns_the_conventional_form_at_anchors_and_a_seven_letter_str_for_every_n_in_1_to_3999(self) -> None:
        self.assertEqual(to_roman(1994), "MCMXCIV")
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(9), "IX")
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")
        for n in range(1, 4000):
            result = to_roman(n)
            self.assertIsInstance(result, str)
            self.assertTrue(set(result) <= set("IVXLCDM"))

    def test_from_roman_of_to_roman_round_trips_every_integer_1_to_3999(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)

    def test_to_roman_of_from_roman_of_to_roman_returns_the_same_numeral_for_every_n_1_to_3999(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(to_roman(from_roman(to_roman(n))), to_roman(n))

    def test_to_roman_raises_value_error_outside_1_to_3999(self) -> None:
        with self.assertRaises(ValueError):
            to_roman(0)
        with self.assertRaises(ValueError):
            to_roman(4000)

    def test_from_roman_returns_n_for_every_valid_numeral(self) -> None:
        self.assertEqual(from_roman("MCMXCIV"), 1994)
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)

    def test_from_roman_accepts_exactly_the_canonical_numerals_over_all_one_to_four_char_strings(self) -> None:
        valid = {to_roman(n) for n in range(1, 4000) if len(to_roman(n)) <= 4}
        for length in (1, 2, 3, 4):
            for chars in itertools.product("IVXLCDM", repeat=length):
                s = "".join(chars)
                if s in valid:
                    n = from_roman(s)
                    self.assertEqual(s, to_roman(n))
                else:
                    with self.assertRaises(ValueError):
                        from_roman(s)
        # Illustrative non-canonical strings (each 1-4 chars, none equal to
        # to_roman(n) for any n in 1..3999): the six in-alphabet ones are
        # subsumed by the sweep above; 'ABC' is outside the seven-letter
        # alphabet but is still a 1-4 char string AC7 covers.
        for s in ("IIII", "IM", "MMMM", "IC", "XLX", "VX", "ABC"):
            with self.assertRaises(ValueError):
                from_roman(s)

    def test_from_roman_raises_value_error_for_empty_string(self) -> None:
        with self.assertRaises(ValueError):
            from_roman("")


if __name__ == "__main__":
    unittest.main()
