import itertools
import unittest

from sandbox.roman import from_roman, to_roman

ROMAN_LETTERS = "IVXLCDM"
SUBTRACTIVE_PAIRS = ("IV", "IX", "XL", "XC", "CD", "CM")


def _has_repeated_subtractive_pair(s: str) -> bool:
    """Return True if any subtractive pair occurs more than once in s."""
    return any(s.count(pair) > 1 for pair in SUBTRACTIVE_PAIRS)


class RomanTest(unittest.TestCase):
    def test_to_roman_returns_a_canonical_numeral_for_every_n_in_1_to_3999(self) -> None:
        for n in range(1, 4000):
            s = to_roman(n)
            self.assertIsInstance(s, str)
            self.assertTrue(all(c in ROMAN_LETTERS for c in s), f"{s!r} has a non-roman letter for {n}")
            self.assertFalse(_has_repeated_subtractive_pair(s), f"{s!r} repeats a subtractive pair for {n}")

    def test_to_roman_raises_value_error_for_every_out_of_range_integer(self) -> None:
        for n in range(0, 4000):
            if n < 1 or n > 3999:
                with self.assertRaises(ValueError):
                    to_roman(n)
            else:
                self.assertIsInstance(to_roman(n), str)
        for n in (0, -1, 4000):
            with self.assertRaises(ValueError):
                to_roman(n)

    def test_from_roman_round_trips_every_n_in_1_to_3999(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)

    def test_from_roman_returns_the_original_n_for_every_valid_output(self) -> None:
        valid = {to_roman(n): n for n in range(1, 4000)}
        self.assertEqual(len(valid), 3999)
        for s, n in valid.items():
            self.assertEqual(from_roman(s), n)

    def test_from_roman_raises_value_error_for_every_1_to_4_char_string_not_in_the_valid_set(self) -> None:
        valid = {to_roman(n) for n in range(1, 4000)}
        for length in range(1, 5):
            for combo in itertools.product(ROMAN_LETTERS, repeat=length):
                s = "".join(combo)
                if s in valid:
                    self.assertIsInstance(from_roman(s), int)
                else:
                    with self.assertRaises(ValueError):
                        from_roman(s)

    def test_from_roman_raises_value_error_for_empty_string(self) -> None:
        with self.assertRaises(ValueError):
            from_roman("")

    def test_from_roman_raises_value_error_for_non_str_argument(self) -> None:
        with self.assertRaises(ValueError):
            from_roman(123)


if __name__ == "__main__":
    unittest.main()
