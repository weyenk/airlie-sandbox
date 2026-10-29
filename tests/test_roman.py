import itertools
import unittest

from sandbox.roman import from_roman, to_roman


class RomanTest(unittest.TestCase):
    def test_to_roman_returns_a_str_for_every_n_in_1_to_3999_without_raising(self) -> None:
        for n in range(1, 4000):
            self.assertIsInstance(to_roman(n), str)

    def test_to_roman_of_1_is_I(self) -> None:
        self.assertEqual(to_roman(1), "I")

    def test_to_roman_of_3999_is_MMMCMXCIX(self) -> None:
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_to_roman_raises_ValueError_for_every_integer_outside_1_to_3999(self) -> None:
        for n in range(-1000, 1):
            with self.assertRaises(ValueError):
                to_roman(n)
        for n in range(4000, 5000):
            with self.assertRaises(ValueError):
                to_roman(n)

    def test_to_roman_raises_ValueError_for_non_int_values(self) -> None:
        for value in (1.0, "5", True):
            with self.assertRaises(ValueError):
                to_roman(value)

    def test_from_roman_raises_ValueError_for_every_1_to_4_char_string_not_in_the_valid_set(self) -> None:
        valid = {to_roman(n): n for n in range(1, 4000)}
        for length in range(1, 5):
            for chars in itertools.product("MDCLXVI", repeat=length):
                s = "".join(chars)
                if s in valid:
                    self.assertEqual(from_roman(s), valid[s])
                else:
                    with self.assertRaises(ValueError):
                        from_roman(s)

    def test_from_roman_raises_ValueError_for_the_empty_string(self) -> None:
        with self.assertRaises(ValueError):
            from_roman("")

    def test_from_roman_of_to_roman_returns_n_for_every_n_in_1_to_3999(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)


if __name__ == "__main__":
    unittest.main()
