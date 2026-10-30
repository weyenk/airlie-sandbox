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


if __name__ == "__main__":
    unittest.main()
