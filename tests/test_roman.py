import unittest

from sandbox.roman import to_roman


class RomanTest(unittest.TestCase):
    def test_to_roman_returns_a_valid_roman_string_for_every_n_from_1_to_3999(self) -> None:
        for n in range(1, 4000):
            numeral = to_roman(n)
            self.assertIsInstance(numeral, str)
            self.assertGreaterEqual(len(numeral), 1)
            self.assertLessEqual(len(numeral), 15)
            self.assertTrue(set(numeral) <= set("IVXLCDM"))

    def test_to_roman_pins_the_request_examples(self) -> None:
        self.assertEqual(to_roman(1), "I")  # length 1, the AC1 minimum
        self.assertEqual(to_roman(4), "IV")  # subtractive form
        self.assertEqual(to_roman(888), "DCCCLXXXVIII")  # 12 chars
        self.assertEqual(to_roman(900), "CM")  # subtractive form
        self.assertEqual(to_roman(1994), "MCMXCIV")  # the request's own example
        self.assertEqual(to_roman(3999), "MMMCMXCIX")  # the range maximum

    def test_to_roman_results_are_all_distinct_over_1_to_3999(self) -> None:
        self.assertEqual(len({to_roman(n) for n in range(1, 4000)}), 3999)

    def test_to_roman_raises_value_error_outside_1_to_3999_and_succeeds_at_the_boundaries(self) -> None:
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")
        for bad in (0, -1, 4000, -100, 100000):
            with self.assertRaises(ValueError):
                to_roman(bad)

    def test_to_roman_raises_value_error_for_non_integer_input(self) -> None:
        for bad in (1.5, "IV", None, True, False):
            with self.assertRaises(ValueError):
                to_roman(bad)


if __name__ == "__main__":
    unittest.main()
