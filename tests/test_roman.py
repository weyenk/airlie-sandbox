import unittest
from itertools import product

from sandbox.roman import from_roman, to_roman

ALPHABET = "IVXLCDM"

VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

PLACE_TABLE = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
]


def standard_roman(n: int) -> str:
    """Reference: greedy subtraction over the standard place table."""
    out = []
    for value, numeral in PLACE_TABLE:
        while n >= value:
            out.append(numeral)
            n -= value
    return "".join(out)


def parse_value(s: str) -> int:
    """Reference: additive/subtractive value of a Roman string."""
    total = 0
    for i, ch in enumerate(s):
        v = VALUES[ch]
        if i + 1 < len(s) and v < VALUES[s[i + 1]]:
            total -= v
        else:
            total += v
    return total


def short_numerals() -> list:
    """Every one-to-four character string over the Roman alphabet."""
    return ["".join(p) for length in (1, 2, 3, 4) for p in product(ALPHABET, repeat=length)]


class ToRomanTest(unittest.TestCase):
    def test_to_roman_matches_the_standard_form_for_every_integer_in_1_to_3999(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(to_roman(n), standard_roman(n))

    def test_to_roman_pins_the_request_examples(self) -> None:
        self.assertEqual(to_roman(1994), "MCMXCIV")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_to_roman_raises_valueerror_for_every_integer_outside_1_to_3999(self) -> None:
        for n in range(0, 4001):
            if n < 1 or n > 3999:
                with self.assertRaises(ValueError):
                    to_roman(n)
            else:
                to_roman(n)


class FromRomanTest(unittest.TestCase):
    def test_every_integer_in_1_to_3999_round_trips(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)

    def test_from_roman_pins_the_request_examples(self) -> None:
        self.assertEqual(from_roman("I"), 1)
        self.assertEqual(from_roman("MCMXCIV"), 1994)
        self.assertEqual(from_roman("MMMCMXCIX"), 3999)

    def test_from_roman_raises_valueerror_for_the_empty_string(self) -> None:
        with self.assertRaises(ValueError):
            from_roman("")

    def test_from_roman_refuses_every_non_canonical_short_numeral(self) -> None:
        valid = {to_roman(n) for n in range(1, 4000)}
        for s in short_numerals():
            if s in valid:
                from_roman(s)
            else:
                with self.assertRaises(ValueError):
                    from_roman(s)

    def test_from_roman_refuses_bad_characters_and_out_of_range_values(self) -> None:
        for s in ("A", "m", "mm", "i", "1"):
            with self.assertRaises(ValueError):
                from_roman(s)
        valid = {to_roman(n) for n in range(1, 4000)}
        for s in short_numerals():
            if parse_value(s) == 0 or parse_value(s) > 3999:
                with self.assertRaises(ValueError):
                    from_roman(s)
            elif s in valid:
                from_roman(s)
        with self.assertRaises(ValueError):
            from_roman("MMMDMM")


if __name__ == "__main__":
    unittest.main()
