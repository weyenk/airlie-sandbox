import itertools
import unittest

import sandbox.roman


class RomanTest(unittest.TestCase):
    def test_to_roman_returns_the_standard_numeral_for_every_n_in_1_to_3999(self) -> None:
        table = [
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
        allowed = set("IVXLCDM")
        for n in range(1, 4000):
            reference = ""
            remainder = n
            for value, numeral in table:
                while remainder >= value:
                    reference += numeral
                    remainder -= value
            self.assertEqual(sandbox.roman.to_roman(n), reference)
            self.assertLessEqual(set(sandbox.roman.to_roman(n)), allowed)

    def test_from_roman_round_trips_every_n_in_1_to_3999(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(sandbox.roman.from_roman(sandbox.roman.to_roman(n)), n)

    def test_from_roman_returns_n_for_each_produced_value(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(sandbox.roman.from_roman(sandbox.roman.to_roman(n)), n)

    def test_to_roman_rejects_0_and_4000_with_1_to_3999(self) -> None:
        for n in (0, 4000):
            with self.assertRaises(ValueError) as ctx:
                sandbox.roman.to_roman(n)
            self.assertIn("1 to 3999", str(ctx.exception))

    def test_to_roman_rejects_non_int_and_bool_with_int(self) -> None:
        for value in (1.5, "I", True, False):
            with self.assertRaises(ValueError) as ctx:
                sandbox.roman.to_roman(value)
            self.assertIn("int", str(ctx.exception))

    def test_from_roman_rejects_empty_string(self) -> None:
        with self.assertRaises(ValueError):
            sandbox.roman.from_roman("")

    def test_from_roman_accepts_exactly_the_produced_values_for_1_to_4_char_strings(self) -> None:
        valid = {sandbox.roman.to_roman(n) for n in range(1, 4000)}
        alphabet = "IVXLCDMivxab12"
        for length in range(1, 5):
            for s in itertools.product(alphabet, repeat=length):
                candidate = "".join(s)
                if candidate in valid:
                    self.assertIsInstance(sandbox.roman.from_roman(candidate), int)
                else:
                    with self.assertRaises(ValueError) as ctx:
                        sandbox.roman.from_roman(candidate)
                    self.assertIn("malformed", str(ctx.exception))

    def test_from_roman_rejects_non_str_with_str(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            sandbox.roman.from_roman(5)
        self.assertIn("str", str(ctx.exception))

    def test_from_roman_rejects_every_5_char_string_not_produced_with_malformed(self) -> None:
        valid = {sandbox.roman.to_roman(n) for n in range(1, 4000)}
        alphabet = "IVXLCDM"
        for s in itertools.product(alphabet, repeat=5):
            candidate = "".join(s)
            if candidate in valid:
                self.assertIsInstance(sandbox.roman.from_roman(candidate), int)
            else:
                with self.assertRaises(ValueError) as ctx:
                    sandbox.roman.from_roman(candidate)
                self.assertIn("malformed", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
