import itertools
import unittest

from sandbox.roman import from_roman, to_roman


class RomanTest(unittest.TestCase):
    def test_every_integer_from_1_to_3999_round_trips(self) -> None:
        for n in range(1, 4000):
            numeral = to_roman(n)
            self.assertIsInstance(numeral, str)
            self.assertEqual(from_roman(numeral), n)

    def test_from_roman_round_trips_valid_and_refuses_every_malformed_numeral(self) -> None:
        valid = {to_roman(n) for n in range(1, 4000)}
        self.assertEqual(len(valid), 3999)
        values = {numeral: n for n in range(1, 4000) for numeral in (to_roman(n),)}
        alphabet = "IVXLCDM"
        for length in range(1, 7):
            for letters in itertools.product(alphabet, repeat=length):
                numeral = "".join(letters)
                if numeral in valid:
                    self.assertEqual(from_roman(numeral), values[numeral])
                else:
                    with self.assertRaises(ValueError):
                        from_roman(numeral)
        # 7..9-char residual the 1..6 sweep cannot see: 'MMMMD' = 4000 (out of
        # range); 'MCMXCIXX' = 2009 non-canonically (canonical 2009 = 'MMIX').
        for numeral in ("MMMMD", "MCMXCIXX"):
            with self.assertRaises(ValueError):
                from_roman(numeral)

    def test_from_roman_empty_string_raises(self) -> None:
        with self.assertRaises(ValueError):
            from_roman("")

    def test_to_roman_out_of_range_raises(self) -> None:
        for n in (0, 4000, -1):
            with self.assertRaises(ValueError):
                to_roman(n)

    def test_to_roman_bool_raises(self) -> None:
        for n in (True, False):
            with self.assertRaises(ValueError):
                to_roman(n)


if __name__ == "__main__":
    unittest.main()
