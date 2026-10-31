"""Tests for sandbox.roman: to_roman and from_roman over 1..3999."""

import itertools
import unittest

from sandbox.roman import from_roman, to_roman

# Independent reference: the standard subtractive table (I, V, X, L, C, D, M with
# IV, IX, XL, XC, CD, CM). The tests compare the module against this, so a stub that
# returns a constant or drifts one row fails.
REF_PAIRS = (
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
)

REF_VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
ALPHABET = "IVXLCDM"


def ref_to_roman(n: int) -> str:
    """Reference standard Roman-numeral representation of n (1..3999)."""
    parts = []
    for value, symbol in REF_PAIRS:
        while n >= value:
            parts.append(symbol)
            n -= value
    return "".join(parts)


def ref_eval(s: str) -> int:
    """Reference standard subtractive evaluation of a string over I, V, X, L, C, D, M."""
    total = 0
    for i, ch in enumerate(s):
        value = REF_VALUES[ch]
        if i + 1 < len(s) and value < REF_VALUES[s[i + 1]]:
            total -= value
        else:
            total += value
    return total


class ToRomanTest(unittest.TestCase):
    def test_to_roman_returns_standard_roman_for_every_n_in_1_to_3999(self) -> None:
        for n in range(1, 4000):
            result = to_roman(n)
            self.assertIsInstance(result, str)
            self.assertEqual(result, ref_to_roman(n))

    def test_to_roman_pins_concrete_values(self) -> None:
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(9), "IX")
        self.assertEqual(to_roman(40), "XL")
        self.assertEqual(to_roman(44), "XLIV")
        self.assertEqual(to_roman(90), "XC")
        self.assertEqual(to_roman(400), "CD")
        self.assertEqual(to_roman(900), "CM")
        self.assertEqual(to_roman(1994), "MCMXCIV")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_to_roman_rejects_out_of_range_with_1_to_3999(self) -> None:
        for n in (0, -1, 4000):
            with self.assertRaises(ValueError) as ctx:
                to_roman(n)
            self.assertIn("1..3999", str(ctx.exception))

    def test_to_roman_rejects_non_integer_with_message(self) -> None:
        for bad in (1.5, "4", True):
            with self.assertRaises(ValueError) as ctx:
                to_roman(bad)
            self.assertIn("n must be an integer", str(ctx.exception))


class FromRomanTest(unittest.TestCase):
    def test_from_roman_round_trips_every_n_in_1_to_3999(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)

    def test_from_roman_rejects_empty_string(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("")
        self.assertIn("empty string", str(ctx.exception))

    def test_from_roman_rejects_off_alphabet_char(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("A")
        self.assertIn("malformed numeral", str(ctx.exception))

    def test_from_roman_exhaustive_over_all_1_to_4_char_in_alphabet_strings(self) -> None:
        # Domain: every string of length 1..4 over I, V, X, L, C, D, M (2,800 strings).
        domain = [
            "".join(p)
            for length in (1, 2, 3, 4)
            for p in itertools.product(ALPHABET, repeat=length)
        ]
        self.assertEqual(len(domain), 2800)

        # Valid outputs of to_roman over 1..3999, per the independent reference.
        valid = {ref_to_roman(n): n for n in range(1, 4000)}
        self.assertEqual(len(valid), 3999)  # to_roman is injective over 1..3999
        in_domain_valid = [s for s in domain if s in valid]
        self.assertEqual(len(in_domain_valid), 346)

        # The 2,453 in-range non-standard strings (e.g. 'IL', 'VV', 'IIM') are
        # accepted per the standard subtractive rule and are out of scope for
        # rejection: the story's out-of-scope section says the standard rule
        # accepts them, so the test documents them as accepted, never rejected.
        in_range_nonstandard = [
            s for s in domain if s not in valid and 1 <= ref_eval(s) <= 3999
        ]
        self.assertEqual(len(in_range_nonstandard), 2453)

        # Exactly one domain string evaluates outside 1..3999.
        out_of_range = [s for s in domain if s not in valid and not 1 <= ref_eval(s) <= 3999]
        self.assertEqual(out_of_range, ["MMMM"])

        for s in domain:
            if s in valid:
                self.assertEqual(from_roman(s), valid[s])
            elif s in in_range_nonstandard:
                self.assertEqual(from_roman(s), ref_eval(s))
            else:
                with self.assertRaises(ValueError) as ctx:
                    from_roman(s)
                self.assertIn("malformed numeral", str(ctx.exception))

    def test_from_roman_rejects_non_string(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman(1994)
        self.assertIn("input must be a string", str(ctx.exception))

    def test_from_roman_rejects_out_of_range_value(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("MMMM")
        self.assertIn("malformed numeral", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
