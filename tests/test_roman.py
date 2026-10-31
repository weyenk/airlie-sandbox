import itertools
import random
import unittest

from sandbox.roman import from_roman, to_roman

ALPHABET = "IVXLCDM"


def valid_outputs() -> set:
    return {to_roman(n) for n in range(1, 4000)}


class RomanTest(unittest.TestCase):
    def test_round_trip_and_charset_for_every_n_in_1_to_3999(self) -> None:
        for n in range(1, 4000):
            numeral = to_roman(n)
            self.assertIsInstance(numeral, str)
            self.assertTrue(set(numeral) <= set(ALPHABET))
            self.assertEqual(from_roman(numeral), n)
        self.assertEqual(to_roman(1994), "MCMXCIV")
        self.assertEqual(to_roman(1999), "MCMXCIX")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_to_roman_rejects_ints_outside_1_to_3999(self) -> None:
        for n in (0, -1, 4000):
            with self.assertRaises(ValueError) as ctx:
                to_roman(n)
            self.assertIn("1..3999", str(ctx.exception))
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_to_roman_rejects_non_ints(self) -> None:
        for value in (1.0, "IV", True):
            with self.assertRaises(ValueError) as ctx:
                to_roman(value)
            self.assertIn("int in 1..3999", str(ctx.exception))

    def test_from_roman_rejects_every_invalid_1_to_4_char_string(self) -> None:
        valid = valid_outputs()
        for length in range(1, 5):
            for chars in itertools.product(ALPHABET, repeat=length):
                s = "".join(chars)
                if s in valid:
                    continue
                with self.assertRaises(ValueError):
                    from_roman(s)

    def test_from_roman_rejects_empty_string(self) -> None:
        with self.assertRaises(ValueError):
            from_roman("")

    def test_from_roman_rejects_invalid_5_to_7_char_strings(self) -> None:
        valid = valid_outputs()
        rng = random.Random(42)
        sample = []
        while len(sample) < 20:
            s = "".join(rng.choice(ALPHABET) for _ in range(rng.randint(5, 7)))
            if s not in valid and s not in sample:
                sample.append(s)
        self.assertTrue(sample)
        for s in sample:
            self.assertNotIn(s, valid)
            with self.assertRaises(ValueError):
                from_roman(s)

    def test_from_roman_rejects_non_str_input(self) -> None:
        with self.assertRaises(ValueError):
            from_roman(12)


if __name__ == "__main__":
    unittest.main()
