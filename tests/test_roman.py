import unittest

from sandbox.roman import to_roman, from_roman


class RomanTest(unittest.TestCase):
    def test_to_roman_returns_canonical_numeral_for_each_pinned_input(self) -> None:
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(9), "IX")
        self.assertEqual(to_roman(10), "X")
        self.assertEqual(to_roman(40), "XL")
        self.assertEqual(to_roman(90), "XC")
        self.assertEqual(to_roman(100), "C")
        self.assertEqual(to_roman(400), "CD")
        self.assertEqual(to_roman(900), "CM")
        self.assertEqual(to_roman(1000), "M")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")
        self.assertEqual(to_roman(2024), "MMXXIV")
        self.assertEqual(to_roman(1994), "MCMXCIV")
        self.assertEqual(to_roman(88), "LXXXVIII")
        self.assertEqual(to_roman(3888), "MMMDCCCLXXXVIII")
        self.assertEqual(to_roman(14), "XIV")
        self.assertEqual(to_roman(999), "CMXCIX")

    def test_to_roman_raises_value_error_with_exact_unquoted_message_for_0_and_4000(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            to_roman(0)
        self.assertEqual(str(ctx.exception), "n must be an integer from 1 to 3999, got 0")
        with self.assertRaises(ValueError) as ctx:
            to_roman(4000)
        self.assertEqual(str(ctx.exception), "n must be an integer from 1 to 3999, got 4000")

    def test_to_roman_raises_value_error_for_negative_input(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            to_roman(-1)
        self.assertEqual(str(ctx.exception), "n must be an integer from 1 to 3999, got -1")

    def test_from_roman_returns_exact_value_for_each_canonical_string(self) -> None:
        self.assertEqual(from_roman("I"), 1)
        self.assertEqual(from_roman("IV"), 4)
        self.assertEqual(from_roman("IX"), 9)
        self.assertEqual(from_roman("X"), 10)
        self.assertEqual(from_roman("XL"), 40)
        self.assertEqual(from_roman("XC"), 90)
        self.assertEqual(from_roman("C"), 100)
        self.assertEqual(from_roman("CD"), 400)
        self.assertEqual(from_roman("CM"), 900)
        self.assertEqual(from_roman("M"), 1000)
        self.assertEqual(from_roman("MMMCMXCIX"), 3999)
        self.assertEqual(from_roman("MMXXIV"), 2024)
        self.assertEqual(from_roman("MCMXCIV"), 1994)
        self.assertEqual(from_roman("LXXXVIII"), 88)
        self.assertEqual(from_roman("MMMDCCCLXXXVIII"), 3888)
        self.assertEqual(from_roman("XIV"), 14)
        self.assertEqual(from_roman("CMXCIX"), 999)

    def test_from_roman_is_case_insensitive(self) -> None:
        self.assertEqual(from_roman("mcmxciv"), 1994)

    def test_from_roman_rejects_empty_string(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("")
        self.assertEqual(str(ctx.exception), "not a valid Roman numeral: ''")

    def test_from_roman_rejects_non_roman_characters(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("AAAA")
        self.assertEqual(str(ctx.exception), "not a valid Roman numeral: 'AAAA'")

    def test_from_roman_rejects_non_canonical_iiii(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("IIII")
        self.assertEqual(str(ctx.exception), "not a valid Roman numeral: 'IIII'")

    def test_from_roman_rejects_non_canonical_ic(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("IC")
        self.assertEqual(str(ctx.exception), "not a valid Roman numeral: 'IC'")

    def test_from_roman_rejects_non_canonical_vx(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("VX")
        self.assertEqual(str(ctx.exception), "not a valid Roman numeral: 'VX'")

    def test_from_roman_rejects_non_canonical_iiv(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("IIV")
        self.assertEqual(str(ctx.exception), "not a valid Roman numeral: 'IIV'")

    def test_round_trip_is_exact_for_every_n_from_1_to_3999(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)

    def test_both_names_importable_and_round_trip_1994(self) -> None:
        from sandbox.roman import to_roman, from_roman

        self.assertEqual(to_roman(1994), "MCMXCIV")
        self.assertEqual(from_roman("MCMXCIV"), 1994)


if __name__ == "__main__":
    unittest.main()
