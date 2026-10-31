import inspect
import unittest
from itertools import product

import sandbox.roman as roman


# The test's own independent canonical construction: greedy subtraction over the
# classical value/symbol table. This is what to_roman is checked against, so it
# must not be imported from the module under test.
_REFERENCE_TABLE = [
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
]

_ALPHABET = "IVXLCDM"


def _reference_roman(n: int) -> str:
    """Canonical numeral for n by greedy subtraction over _REFERENCE_TABLE."""
    parts = []
    for value, symbol in _REFERENCE_TABLE:
        while n >= value:
            parts.append(symbol)
            n -= value
    return "".join(parts)


def _valid_outputs() -> dict:
    """Map each of the 3999 distinct to_roman outputs back to its unique n."""
    return {roman.to_roman(n): n for n in range(1, 4000)}


class RomanTest(unittest.TestCase):
    def test_module_exposes_to_roman_and_from_roman_with_correct_signatures(self) -> None:
        self.assertTrue(callable(roman.to_roman))
        self.assertTrue(callable(roman.from_roman))

        to_sig = inspect.signature(roman.to_roman)
        self.assertEqual(list(to_sig.parameters), ["n"])
        self.assertIs(to_sig.parameters["n"].annotation, int)
        self.assertIs(to_sig.return_annotation, str)

        from_sig = inspect.signature(roman.from_roman)
        self.assertEqual(list(from_sig.parameters), ["s"])
        self.assertIs(from_sig.parameters["s"].annotation, str)
        self.assertIs(from_sig.return_annotation, int)

    def test_to_roman_matches_standard_for_every_n_in_1_to_3999(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(roman.to_roman(n), _reference_roman(n))

        # The request's own pinned examples: they pin the reference table so the
        # whole-range comparison above is not a tautology.
        pinned = {
            1: "I",
            4: "IV",
            9: "IX",
            40: "XL",
            90: "XC",
            400: "CD",
            900: "CM",
            1994: "MCMXCIV",
            3888: "MMMDCCCLXXXVIII",
            3999: "MMMCMXCIX",
        }
        for n, expected in pinned.items():
            self.assertEqual(roman.to_roman(n), expected)

    def test_every_integer_in_1_to_3999_round_trips(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(roman.from_roman(roman.to_roman(n)), n)

    def test_every_to_roman_output_is_accepted_and_maps_back_to_its_unique_n(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(roman.from_roman(roman.to_roman(n)), n)
        self.assertEqual(roman.from_roman("MCMXCIV"), 1994)

    def test_from_roman_accepts_exactly_the_valid_1_to_4_char_outputs(self) -> None:
        valid = _valid_outputs()
        for length in (1, 2, 3, 4):
            for combo in product(_ALPHABET, repeat=length):
                s = "".join(combo)
                try:
                    result = roman.from_roman(s)
                except ValueError:
                    raised = True
                else:
                    raised = False
                if s in valid:
                    self.assertFalse(raised, "%r should be accepted" % s)
                    self.assertEqual(result, valid[s])
                else:
                    self.assertTrue(raised, "%r should raise ValueError" % s)

        # Named invalid 1-4-char strings each raise.
        for s in ("IIII", "MMMM", "VV", "XCXC", "VIV"):
            with self.assertRaises(ValueError):
                roman.from_roman(s)

    def test_from_roman_raises_on_empty_string(self) -> None:
        with self.assertRaises(ValueError):
            roman.from_roman("")

    def test_from_roman_raises_on_invalid_5_to_8_char_strings(self) -> None:
        valid = _valid_outputs()
        for length in (5, 6, 7, 8):
            for combo in product(_ALPHABET, repeat=length):
                s = "".join(combo)
                try:
                    result = roman.from_roman(s)
                except ValueError:
                    raised = True
                else:
                    raised = False
                if s in valid:
                    self.assertFalse(raised, "%r should be accepted" % s)
                    self.assertEqual(result, valid[s])
                else:
                    self.assertTrue(raised, "%r should raise ValueError" % s)

        # Named invalid 5+-char strings each raise.
        for s in ("IIII" * 3, "MMMM" + "I", "MMMMM"):
            with self.assertRaises(ValueError):
                roman.from_roman(s)

        # Named valid 5+-char outputs are accepted and map back to their n.
        self.assertEqual(roman.from_roman("MCMXCIV"), 1994)
        self.assertEqual(roman.from_roman("MMMCMXCIX"), 3999)

    def test_to_roman_raises_on_out_of_range_integers(self) -> None:
        for n in (0, -1, 4000):
            with self.assertRaises(ValueError):
                roman.to_roman(n)
        self.assertEqual(roman.to_roman(1), "I")
        self.assertEqual(roman.to_roman(3999), "MMMCMXCIX")

    def test_to_roman_raises_on_bool_input(self) -> None:
        with self.assertRaises(ValueError):
            roman.to_roman(True)
        with self.assertRaises(ValueError):
            roman.to_roman(False)


if __name__ == "__main__":
    unittest.main()
