import itertools
import unittest

from sandbox.roman import from_roman, to_roman


class RomanTest(unittest.TestCase):
    def test_to_roman_returns_str_and_round_trips_for_every_n_in_range(self) -> None:
        for n in range(1, 4000):
            numeral = to_roman(n)
            self.assertIsInstance(numeral, str)
            self.assertEqual(from_roman(numeral), n)

    def test_to_roman_is_injective_over_1_to_3999(self) -> None:
        self.assertEqual(len({to_roman(n) for n in range(1, 4000)}), 3999)

    def test_to_roman_of_1_is_I(self) -> None:
        self.assertEqual(to_roman(1), "I")

    def test_to_roman_uses_only_roman_letters(self) -> None:
        letters = set("IVXLCDM")
        for n in range(1, 4000):
            self.assertLessEqual(set(to_roman(n)), letters)

    def test_to_roman_is_at_most_15_chars(self) -> None:
        for n in range(1, 4000):
            self.assertLessEqual(len(to_roman(n)), 15)
        self.assertEqual(len(to_roman(3888)), 15)

    def test_to_roman_raises_out_of_range_and_3999_is_largest(self) -> None:
        with self.assertRaises(ValueError):
            to_roman(0)
        with self.assertRaises(ValueError):
            to_roman(4000)
        self.assertIsInstance(to_roman(3999), str)

    def test_from_roman_of_I_is_1_and_raises_on_every_non_valid_string(self) -> None:
        self.assertEqual(from_roman("I"), 1)
        valid = {to_roman(n) for n in range(1, 4000)}
        for length in (1, 2, 3, 4):
            for s in ("".join(p) for p in itertools.product("IVXLCDM", repeat=length)):
                if s not in valid:
                    with self.assertRaises(ValueError):
                        from_roman(s)

    def test_from_roman_raises_on_malformed_strings(self) -> None:
        for s in ("IIII", "VV", "IC", "XM", "IM", "VVV", "LL", "DD", "MMMM", "XCX", "IL", "XD"):
            with self.assertRaises(ValueError):
                from_roman(s)

    def test_from_roman_raises_on_empty_string(self) -> None:
        with self.assertRaises(ValueError):
            from_roman("")

    def test_from_roman_raises_on_non_str_input(self) -> None:
        with self.assertRaises(ValueError):
            from_roman(5)


if __name__ == "__main__":
    unittest.main()
