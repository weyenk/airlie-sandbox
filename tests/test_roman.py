import unittest

from sandbox.roman import to_roman

ROMAN_LETTERS = frozenset("IVXLCDM")
SUBTRACTIVE_PAIRS = ("IV", "IX", "XL", "XC", "CD", "CM")


def _has_repeated_subtractive_pair(s: str) -> bool:
    """Return True if any subtractive pair occurs more than once in s."""
    return any(s.count(pair) > 1 for pair in SUBTRACTIVE_PAIRS)


class RomanTest(unittest.TestCase):
    def test_to_roman_returns_a_canonical_numeral_for_every_n_in_1_to_3999(self) -> None:
        for n in range(1, 4000):
            numeral = to_roman(n)
            self.assertIsInstance(numeral, str, f"to_roman({n}) did not return a str")
            self.assertTrue(
                set(numeral) <= ROMAN_LETTERS,
                f"to_roman({n}) = {numeral!r} contains letters outside I, V, X, L, C, D, M",
            )
            self.assertFalse(
                _has_repeated_subtractive_pair(numeral),
                f"to_roman({n}) = {numeral!r} repeats a subtractive pair",
            )

    def test_to_roman_raises_value_error_for_every_out_of_range_integer(self) -> None:
        for n in range(0, 4000):
            if n < 1 or n > 3999:
                with self.assertRaises(ValueError):
                    to_roman(n)
            else:
                self.assertIsInstance(to_roman(n), str, f"to_roman({n}) should be accepted")
        for n in (0, -1, 4000):
            with self.assertRaises(ValueError):
                to_roman(n)


if __name__ == "__main__":
    unittest.main()
