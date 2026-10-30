import itertools
import unittest

from sandbox.roman import from_roman, to_roman


class RomanTest(unittest.TestCase):
    def test_to_roman_round_trips_every_integer_from_1_to_3999(self) -> None:
        for n in range(1, 4000):
            numeral = to_roman(n)
            self.assertIsInstance(numeral, str)
            self.assertEqual(from_roman(numeral), n)

    def test_to_roman_raises_value_error_containing_1_3999_for_out_of_range_integers(self) -> None:
        for n in (0, 4000, -1, 10000):
            with self.assertRaisesRegex(ValueError, "1\\.\\.3999"):
                to_roman(n)

    def test_from_roman_raises_value_error_containing_not_a_roman_numeral_for_empty_string(self) -> None:
        with self.assertRaisesRegex(ValueError, "not a roman numeral"):
            from_roman("")

    def test_from_roman_refuses_every_non_valid_string_of_one_to_four_roman_characters(self) -> None:
        valid = {to_roman(n) for n in range(1, 4000)}
        self.assertEqual(len(valid), 3999)
        self.assertEqual(max(len(x) for x in valid), 15)
        alphabet = "IVXLCDM"
        for length in (1, 2, 3, 4):
            for combo in itertools.product(alphabet, repeat=length):
                s = "".join(combo)
                if s in valid:
                    continue
                with self.assertRaises(ValueError):
                    from_roman(s)
        for s in ("IIII", "VV", "DD", "IC", "XM", "IM", "LC", "IXI", "iv", "I V"):
            with self.assertRaises(ValueError):
                from_roman(s)

    def test_from_roman_returns_the_unique_integer_for_every_valid_output(self) -> None:
        inverse = {}
        for n in range(1, 4000):
            s = to_roman(n)
            self.assertNotIn(s, inverse)
            inverse[s] = n
        for s, n in inverse.items():
            self.assertEqual(from_roman(s), n)
        self.assertEqual(from_roman("I"), 1)
        self.assertEqual(from_roman("IV"), 4)
        self.assertEqual(from_roman("CM"), 900)
        self.assertEqual(from_roman("MMMCMXCIX"), 3999)

    def test_to_roman_raises_value_error_for_non_integer_arguments(self) -> None:
        for arg in (4.0, "IV", None, True):
            with self.assertRaises(ValueError):
                to_roman(arg)


if __name__ == "__main__":
    unittest.main()
