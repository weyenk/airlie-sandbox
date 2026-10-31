import itertools
import unittest

from sandbox.roman import from_roman, to_roman


class RomanTest(unittest.TestCase):
    def test_every_integer_1_to_3999_round_trips_and_outputs_are_distinct(self) -> None:
        outputs = [to_roman(n) for n in range(1, 4000)]
        self.assertEqual(len(set(outputs)), 3999)
        for n in range(1, 4000):
            self.assertIsInstance(to_roman(n), str)
            self.assertEqual(from_roman(to_roman(n)), n)

    def test_to_roman_uses_subtractive_notation_for_named_and_edge_values(self) -> None:
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(9), "IX")
        self.assertEqual(to_roman(40), "XL")
        self.assertEqual(to_roman(90), "XC")
        self.assertEqual(to_roman(400), "CD")
        self.assertEqual(to_roman(900), "CM")
        self.assertEqual(to_roman(1994), "MCMXCIV")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_from_roman_returns_the_integer_for_a_valid_output(self) -> None:
        self.assertEqual(from_roman("XIV"), 14)
        self.assertEqual(from_roman("MCMXCIV"), 1994)

    def test_to_roman_raises_value_error_for_out_of_range_and_non_int(self) -> None:
        for bad in (0, 4000, -1, 1.5, "14", None):
            with self.assertRaises(ValueError):
                to_roman(bad)

    def test_from_roman_raises_value_error_for_empty_string(self) -> None:
        with self.assertRaises(ValueError):
            from_roman("")

    def test_from_roman_accepts_exactly_the_to_roman_outputs_over_all_1_to_4_char_strings(self) -> None:
        valid = {to_roman(n) for n in range(1, 4000) if len(to_roman(n)) <= 4}
        self.assertEqual(len(valid), 346)
        inverse = {to_roman(n): n for n in range(1, 4000)}
        accepted = set()
        for length in range(1, 5):
            for s in ("".join(p) for p in itertools.product("IVXLCDM", repeat=length)):
                try:
                    value = from_roman(s)
                except ValueError:
                    continue
                accepted.add(s)
                self.assertEqual(value, inverse[s])
        self.assertEqual(accepted, valid)

    def test_from_roman_raises_value_error_for_malformed_and_non_canonical_strings(self) -> None:
        for bad in (
            "IIII", "VX", "IM", "MMMM", "IC", "XD", "LC", "DM", "IL", "LD", "XM",
            "xiv", " XIV ",
        ):
            with self.assertRaises(ValueError):
                from_roman(bad)


if __name__ == "__main__":
    unittest.main()
