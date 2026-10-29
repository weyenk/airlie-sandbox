import itertools
import unittest

import sandbox.roman
from sandbox.roman import from_roman, to_roman


class RomanTest(unittest.TestCase):
    def test_to_roman_raises_valueerror_for_out_of_range(self) -> None:
        for n in (0, -1, 4000):
            with self.assertRaises(ValueError) as ctx:
                to_roman(n)
            self.assertNotEqual(str(ctx.exception), "")

    def test_to_roman_returns_canonical_numeral_for_boundaries(self) -> None:
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(9), "IX")
        self.assertEqual(to_roman(40), "XL")
        self.assertEqual(to_roman(90), "XC")
        self.assertEqual(to_roman(400), "CD")
        self.assertEqual(to_roman(900), "CM")

    def test_to_roman_output_uses_only_roman_characters(self) -> None:
        for n in (1, 4, 9, 40, 90, 400, 900, 3999):
            self.assertTrue(set(to_roman(n)) <= set("IVXLCDM"))

    def test_module_exposes_to_roman_and_from_roman(self) -> None:
        self.assertTrue(callable(sandbox.roman.to_roman))
        self.assertTrue(callable(sandbox.roman.from_roman))

    def test_to_roman_output_is_valid_and_round_trips(self) -> None:
        for n in (1, 4, 9, 40, 90, 400, 900, 3999):
            self.assertTrue(set(to_roman(n)) <= set("IVXLCDM"))
            self.assertEqual(from_roman(to_roman(n)), n)

    def test_from_roman_round_trips_to_roman(self) -> None:
        for n in (1, 4, 9, 40, 90, 400, 900, 3999):
            self.assertEqual(from_roman(to_roman(n)), n)

    def test_from_roman_accepts_exactly_the_valid_outputs(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)

    def test_from_roman_rejects_all_short_malformed_strings_and_samples_longer_ones(self) -> None:
        valid = {to_roman(n): n for n in range(1, 4000)}
        alphabet = "IVXLCDM"
        for length in range(5):
            for s in ("", *("".join(p) for p in itertools.product(alphabet, repeat=length))):
                if s in valid:
                    self.assertEqual(from_roman(s), valid[s])
                else:
                    with self.assertRaises(ValueError) as ctx:
                        from_roman(s)
                    self.assertNotEqual(str(ctx.exception), "")
        for s in ("mcmxciv", "A"):
            with self.assertRaises(ValueError) as ctx:
                from_roman(s)
            self.assertNotEqual(str(ctx.exception), "")


if __name__ == "__main__":
    unittest.main()
