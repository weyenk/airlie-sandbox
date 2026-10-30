import itertools
import unittest

from sandbox.roman import from_roman, to_roman


class RomanTest(unittest.TestCase):
    def test_round_trip_for_every_integer_1_to_3999(self) -> None:
        for n in range(1, 4000):
            numeral = to_roman(n)
            self.assertIsInstance(numeral, str)
            self.assertEqual(from_roman(numeral), n)

    def test_to_roman_1_is_I(self) -> None:
        self.assertEqual(to_roman(1), "I")

    def test_out_of_range_integers_raise_value_error(self) -> None:
        for bad in (0, -1, -100, 4000, 5000, 10000):
            with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
                to_roman(bad)
        for bad in (0, -5, 4000, 100000):
            with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
                from_roman(bad)

    def test_every_string_of_length_1_to_4_outside_the_valid_set_raises(self) -> None:
        valid = {to_roman(n) for n in range(1, 4000)}
        for length in range(1, 5):
            for chars in itertools.product("IVXLCDM", repeat=length):
                s = "".join(chars)
                if s in valid:
                    from_roman(s)
                else:
                    with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
                        from_roman(s)

    def test_empty_string_raises_value_error(self) -> None:
        with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
            from_roman("")

    def test_strings_longer_than_15_chars_raise_value_error(self) -> None:
        self.assertEqual(max(len(to_roman(n)) for n in range(1, 4000)), 15)
        self.assertEqual(from_roman("MMMDCCCLXXXVIII"), 3888)
        with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
            from_roman("MMMDCCCLXXXVIIII")

    def test_every_valid_output_parses_to_its_integer(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)
        for bad in ("IIII", "IIV", "VV", "iiii", "1234", " I"):
            with self.assertRaisesRegex(ValueError, "not a valid Roman numeral"):
                from_roman(bad)


if __name__ == "__main__":
    unittest.main()
