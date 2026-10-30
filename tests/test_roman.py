import itertools
import unittest

from sandbox.roman import from_roman, to_roman


class RomanTest(unittest.TestCase):
    def test_to_roman_returns_standard_numeral_for_every_n_in_1_to_3999(self) -> None:
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(9), "IX")
        self.assertEqual(to_roman(40), "XL")
        self.assertEqual(to_roman(90), "XC")
        self.assertEqual(to_roman(400), "CD")
        self.assertEqual(to_roman(900), "CM")
        self.assertEqual(to_roman(1000), "M")
        self.assertEqual(to_roman(1994), "MCMXCIV")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")
        outputs = []
        for n in range(1, 4000):
            output = to_roman(n)
            self.assertIsInstance(output, str)
            self.assertEqual(from_roman(output), n)
            outputs.append(output)
        self.assertEqual(len(set(outputs)), 3999)

    def test_to_roman_raises_valueerror_with_exact_message_out_of_range(self) -> None:
        for n in (0, -1, 4000, 10**6):
            with self.assertRaises(ValueError) as ctx:
                to_roman(n)
            self.assertEqual(str(ctx.exception), "n must be an integer between 1 and 3999")

    def test_from_roman_is_inverse_of_to_roman_for_every_n_in_1_to_3999(self) -> None:
        self.assertEqual(from_roman("MCMXCIV"), 1994)
        self.assertEqual(from_roman("MMMCMXCIX"), 3999)
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)

    def test_from_roman_accepts_exactly_the_canonical_1_to_4_char_outputs(self) -> None:
        canonical = {to_roman(n) for n in range(1, 4000)}
        alphabet = "MDCLXVI"
        accepted = 0
        for length in range(1, 5):
            for s in itertools.product(alphabet, repeat=length):
                s = "".join(s)
                if s in canonical:
                    self.assertIsInstance(from_roman(s), int)
                    accepted += 1
                else:
                    with self.assertRaises(ValueError) as ctx:
                        from_roman(s)
                    self.assertEqual(str(ctx.exception), "not a valid Roman numeral")
        self.assertEqual(accepted, 346)

    def test_from_roman_raises_valueerror_with_exact_message_on_empty_string(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("")
        self.assertEqual(str(ctx.exception), "not a valid Roman numeral")


if __name__ == "__main__":
    unittest.main()
