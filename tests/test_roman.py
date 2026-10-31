import itertools
import unittest

from sandbox.roman import from_roman, to_roman


# Independent standard greedy-table implementation, written inside the test file
# (never imported from sandbox.roman). Pins to_roman against the standard system.
STANDARD_TABLE = [
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


def standard_roman(n: int) -> str:
    """Independent reference: greedy standard table over 1..3999."""
    out = []
    for value, letters in STANDARD_TABLE:
        while n >= value:
            out.append(letters)
            n -= value
    return "".join(out)


class RomanTest(unittest.TestCase):
    def test_to_roman_returns_the_standard_numeral_for_every_n_in_1_to_3999(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(to_roman(n), standard_roman(n))

    def test_to_roman_matches_the_request_own_examples(self) -> None:
        self.assertEqual(to_roman(1994), "MCMXCIV")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(900), "CM")

    def test_from_roman_round_trips_every_n_in_1_to_3999(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)
        self.assertEqual(from_roman("MCMXCIV"), 1994)

    def test_to_roman_raises_value_error_for_every_n_outside_1_to_3999(self) -> None:
        for n in range(0, 4001):
            if n < 1 or n > 3999:
                with self.assertRaises(ValueError):
                    to_roman(n)

    def test_to_roman_raises_value_error_for_non_int_inputs(self) -> None:
        with self.assertRaises(ValueError):
            to_roman(1.5)
        with self.assertRaises(ValueError):
            to_roman(True)

    def test_from_roman_raises_value_error_for_empty_string(self) -> None:
        with self.assertRaises(ValueError):
            from_roman("")

    def test_from_roman_raises_value_error_for_every_invalid_string_of_length_1_to_4(self) -> None:
        valid = {to_roman(n) for n in range(1, 4000)}
        self.assertEqual(len(valid), 3999)
        self.assertEqual(sum(1 for s in valid if len(s) <= 4), 346)
        self.assertEqual({s for s in valid if len(s) == 1}, set("IVXLCDM"))
        alphabet = "IVXLCDM"
        for length in (1, 2, 3, 4):
            for combo in itertools.product(alphabet, repeat=length):
                s = "".join(combo)
                if s not in valid:
                    with self.assertRaises(ValueError):
                        from_roman(s)
        for s in ("IIII", "MMMM", "IC", "VX"):
            with self.assertRaises(ValueError):
                from_roman(s)

    def test_from_roman_raises_value_error_for_strings_of_length_15_or_longer(self) -> None:
        with self.assertRaises(ValueError):
            from_roman("M" * 15)
        with self.assertRaises(ValueError):
            from_roman("M" * 20)

    def test_from_roman_raises_value_error_for_non_string_inputs(self) -> None:
        with self.assertRaises(ValueError):
            from_roman(4)
        with self.assertRaises(ValueError):
            from_roman(None)

    def test_from_roman_is_case_sensitive_and_rejects_trailing_junk(self) -> None:
        with self.assertRaises(ValueError):
            from_roman("mcmxciv")
        with self.assertRaises(ValueError):
            from_roman("MCMXCIVX")


if __name__ == "__main__":
    unittest.main()
