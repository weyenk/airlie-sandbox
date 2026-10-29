import unittest

from sandbox.roman import from_roman, to_roman


class RomanTest(unittest.TestCase):
    def test_known_values_pin_the_table(self) -> None:
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(9), "IX")
        self.assertEqual(to_roman(40), "XL")
        self.assertEqual(to_roman(90), "XC")
        self.assertEqual(to_roman(400), "CD")
        self.assertEqual(to_roman(900), "CM")
        self.assertEqual(to_roman(1994), "MCMXCIV")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_zero_returns_empty_string(self) -> None:
        self.assertEqual(to_roman(0), "")
        self.assertIsInstance(to_roman(0), str)

    def test_out_of_range_raises_value_error(self) -> None:
        for n in (-1, 4000):
            with self.assertRaises(ValueError) as ctx:
                to_roman(n)
            self.assertIn("outside the range", str(ctx.exception))

    def test_round_trip_for_every_n_in_1_to_3999(self) -> None:
        for n in range(1, 4000):
            numeral = to_roman(n)
            self.assertIsInstance(numeral, str)
            self.assertEqual(from_roman(numeral), n)
        for n in (1, 4, 9, 40, 90, 400, 900, 3999):
            self.assertEqual(from_roman(to_roman(n)), n)

    def test_round_trip_extends_to_zero(self) -> None:
        self.assertEqual(to_roman(0), "")
        for n in range(0, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)

    def test_every_string_of_up_to_four_roman_chars_is_accepted_exactly_when_valid(self) -> None:
        alphabet = "IVXLCDM"
        valid = {to_roman(n) for n in range(0, 4000)}
        for length in range(1, 5):
            for i in range(len(alphabet) ** length):
                s = "".join(
                    alphabet[(i // len(alphabet) ** p) % len(alphabet)]
                    for p in range(length)
                )
                if s in valid:
                    self.assertIsInstance(from_roman(s), int)
                else:
                    with self.assertRaises(ValueError) as ctx:
                        from_roman(s)
                    self.assertIn("malformed numeral", str(ctx.exception))
        for s in ("IIII", "VV", "LC", "IM", "xiv", "ABC"):
            with self.assertRaises(ValueError) as ctx:
                from_roman(s)
            self.assertIn("malformed numeral", str(ctx.exception))

    def test_valid_outputs_return_their_n(self) -> None:
        self.assertEqual(from_roman("MCMXCIV"), 1994)
        self.assertEqual(from_roman("MMMCMXCIX"), 3999)
        self.assertEqual(from_roman("IV"), 4)
        self.assertEqual(from_roman(""), 0)


if __name__ == "__main__":
    unittest.main()
