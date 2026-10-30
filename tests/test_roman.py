import itertools
import unittest

from sandbox.roman import from_roman, to_roman


class RomanTest(unittest.TestCase):
    def test_round_trip_for_every_integer_in_1_to_3999(self) -> None:
        for n in range(1, 4000):
            self.assertIsInstance(to_roman(n), str)
            self.assertEqual(from_roman(to_roman(n)), n)

    def test_from_roman_returns_the_integer_for_every_canonical_numeral(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)
        self.assertEqual(from_roman("MMMCMXCIX"), 3999)

    def test_from_roman_accepts_upper_case_canonical_input(self) -> None:
        self.assertEqual(from_roman("IV"), 4)

    def test_to_roman_raises_value_error_for_every_integer_outside_1_to_3999(self) -> None:
        for n in (-10000, -1, 0, 1, 3999, 4000, 10000):
            if n < 1 or n > 3999:
                with self.assertRaises(ValueError):
                    to_roman(n)
            else:
                self.assertIsInstance(to_roman(n), str)

    def test_from_roman_raises_value_error_for_every_1_to_4_char_string_that_is_not_canonical(self) -> None:
        valid = {to_roman(n) for n in range(1, 4000)}
        alphabet = "IVXLCDM"
        for length in (1, 2, 3, 4):
            for s in itertools.product(alphabet, repeat=length):
                numeral = "".join(s)
                if numeral in valid:
                    self.assertIsInstance(from_roman(numeral), int)
                else:
                    with self.assertRaises(ValueError):
                        from_roman(numeral)

    def test_from_roman_raises_value_error_for_longer_and_lower_case_strings(self) -> None:
        with self.assertRaises(ValueError):
            from_roman("MMMM")
        with self.assertRaises(ValueError):
            from_roman("MMMMM")
        with self.assertRaises(ValueError):
            from_roman("mmxxvi")

    def test_from_roman_raises_value_error_for_the_empty_string(self) -> None:
        with self.assertRaises(ValueError):
            from_roman("")


if __name__ == "__main__":
    unittest.main()
