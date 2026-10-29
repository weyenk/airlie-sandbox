import itertools
import unittest

from sandbox.roman import from_roman, to_roman


class RomanTest(unittest.TestCase):
    def test_round_trip_all_values_1_to_3999(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)

    def test_to_roman_rejects_out_of_range_and_non_int(self) -> None:
        for bad in (0, -1, 4000, True, 1.5, "abc", None):
            with self.assertRaisesRegex(ValueError, "out of range"):
                to_roman(bad)

    def test_from_roman_rejects_all_invalid_strings_length_at_most_4(self) -> None:
        valid = {to_roman(n): n for n in range(1, 4000)}
        alphabet = "IVXLCDM"
        for length in range(5):
            for chars in itertools.product(alphabet, repeat=length):
                s = "".join(chars)
                if s in valid:
                    self.assertEqual(from_roman(s), valid[s])
                else:
                    with self.assertRaisesRegex(ValueError, "malformed"):
                        from_roman(s)
        for bad in ("Z", "1", "a", "mm", "iv", "xc"):
            with self.assertRaisesRegex(ValueError, "malformed"):
                from_roman(bad)

    def test_from_roman_returns_correct_int_for_valid_inputs(self) -> None:
        self.assertEqual(from_roman("I"), 1)
        self.assertEqual(from_roman("MCMXCIV"), 1994)
        self.assertEqual(from_roman("MMMCMXCIX"), 3999)

    def test_to_roman_1994_returns_mcmxciv(self) -> None:
        self.assertEqual(to_roman(1994), "MCMXCIV")


if __name__ == "__main__":
    unittest.main()
