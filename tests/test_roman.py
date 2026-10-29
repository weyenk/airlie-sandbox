import itertools
import unittest

from sandbox.roman import from_roman, to_roman


class RomanTest(unittest.TestCase):
    def test_to_roman_known_values(self) -> None:
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(9), "IX")
        self.assertEqual(to_roman(40), "XL")
        self.assertEqual(to_roman(90), "XC")
        self.assertEqual(to_roman(400), "CD")
        self.assertEqual(to_roman(900), "CM")
        self.assertEqual(to_roman(14), "XIV")
        self.assertEqual(to_roman(88), "LXXXVIII")
        self.assertEqual(to_roman(1994), "MCMXCIV")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_to_roman_bool_true_returns_I(self) -> None:
        self.assertEqual(to_roman(True), "I")

    def test_to_roman_bool_false_raises(self) -> None:
        with self.assertRaisesRegex(ValueError, r"n must be an int between 1 and 3999"):
            to_roman(False)

    def test_round_trip_all_values_1_to_3999(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)

    def test_to_roman_zero_raises(self) -> None:
        with self.assertRaisesRegex(ValueError, r"n must be an int between 1 and 3999"):
            to_roman(0)

    def test_to_roman_above_max_raises(self) -> None:
        with self.assertRaisesRegex(ValueError, r"n must be an int between 1 and 3999"):
            to_roman(4000)
        with self.assertRaisesRegex(ValueError, r"n must be an int between 1 and 3999"):
            to_roman(-1)

    def test_to_roman_non_int_raises(self) -> None:
        with self.assertRaisesRegex(ValueError, r"n must be an int between 1 and 3999"):
            to_roman(3.5)
        with self.assertRaisesRegex(ValueError, r"n must be an int between 1 and 3999"):
            to_roman("IV")
        with self.assertRaisesRegex(ValueError, r"n must be an int between 1 and 3999"):
            to_roman(None)

    def test_from_roman_known_values(self) -> None:
        self.assertEqual(from_roman("IV"), 4)
        self.assertEqual(from_roman("XIV"), 14)
        self.assertEqual(from_roman("MCMXCIV"), 1994)
        self.assertEqual(from_roman("MMMCMXCIX"), 3999)
        self.assertEqual(from_roman("I"), 1)

    def test_from_roman_non_str_raises(self) -> None:
        with self.assertRaisesRegex(ValueError, r"s must be a str between 1 and 3999"):
            from_roman(123)
        with self.assertRaisesRegex(ValueError, r"s must be a str between 1 and 3999"):
            from_roman(None)

    def test_from_roman_malformed_raises(self) -> None:
        for s in ("", "xl", "A", "IIII", "VV", "IM", "LC"):
            with self.assertRaisesRegex(ValueError, r"s must be a str between 1 and 3999"):
                from_roman(s)

    def test_from_roman_rejects_all_invalid_short_strings(self) -> None:
        valid = {to_roman(n): n for n in range(1, 4000)}
        for length in range(1, 5):
            for chars in itertools.product("IVXLCDM", repeat=length):
                s = "".join(chars)
                if s in valid:
                    self.assertEqual(from_roman(s), valid[s])
                else:
                    with self.assertRaisesRegex(ValueError, r"s must be a str between 1 and 3999"):
                        from_roman(s)


if __name__ == "__main__":
    unittest.main()
