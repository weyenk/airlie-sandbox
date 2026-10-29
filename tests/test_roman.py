import unittest

from sandbox.roman import to_roman


class RomanTest(unittest.TestCase):
    def test_to_roman_of_one_is_I(self) -> None:
        self.assertEqual(to_roman(1), "I")

    def test_to_roman_of_four_is_IV(self) -> None:
        self.assertEqual(to_roman(4), "IV")

    def test_to_roman_of_3999_is_MMMCMXCIX(self) -> None:
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_to_roman_of_9_is_IX(self) -> None:
        self.assertEqual(to_roman(9), "IX")

    def test_to_roman_of_40_is_XL(self) -> None:
        self.assertEqual(to_roman(40), "XL")

    def test_to_roman_of_90_is_XC(self) -> None:
        self.assertEqual(to_roman(90), "XC")

    def test_to_roman_of_400_is_CD(self) -> None:
        self.assertEqual(to_roman(400), "CD")

    def test_to_roman_of_900_is_CM(self) -> None:
        self.assertEqual(to_roman(900), "CM")

    def test_to_roman_of_zero_raises_ValueError_naming_the_range(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            to_roman(0)
        self.assertIn("1 to 3999", str(ctx.exception))

    def test_to_roman_of_4000_raises_ValueError_naming_the_range(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            to_roman(4000)
        self.assertIn("1 to 3999", str(ctx.exception))

    def test_to_roman_returns_a_string_for_every_n_from_1_to_3999(self) -> None:
        for n in range(1, 4000):
            self.assertIsInstance(to_roman(n), str)

    def test_to_roman_rejects_bool_input(self) -> None:
        with self.assertRaises(ValueError):
            to_roman(True)
        with self.assertRaises(ValueError):
            to_roman(False)

    def test_to_roman_rejects_non_int_input(self) -> None:
        with self.assertRaises(ValueError):
            to_roman("4")
        with self.assertRaises(ValueError):
            to_roman(4.0)


if __name__ == "__main__":
    unittest.main()
