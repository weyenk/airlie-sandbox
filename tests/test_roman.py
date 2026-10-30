import itertools
import unittest

from sandbox.roman import from_roman, to_roman

ALPHABET = "IVXLCDM"


def all_short_strings() -> list[str]:
    """Every 1-4 character string over the Roman alphabet (2800 strings)."""
    return ["".join(chars) for length in (1, 2, 3, 4) for chars in itertools.product(ALPHABET, repeat=length)]


class RomanTest(unittest.TestCase):
    def test_round_trip_for_every_integer_in_range(self) -> None:
        for n in range(1, 4000):
            numeral = to_roman(n)
            self.assertIsInstance(numeral, str)
            self.assertEqual(from_roman(numeral), n)

    def test_rejects_every_non_canonical_string_of_one_to_four_chars(self) -> None:
        canonical = {to_roman(n) for n in range(1, 4000)}
        for s in all_short_strings():
            if s in canonical:
                continue
            with self.assertRaises(ValueError):
                from_roman(s)

    def test_to_roman_raises_value_error_out_of_range(self) -> None:
        for n in (0, -1, -3999, 4000, 10000):
            with self.assertRaises(ValueError) as ctx:
                to_roman(n)
            self.assertRegex(str(ctx.exception), r"1 to 3999")

    def test_to_roman_uses_only_roman_alphabet(self) -> None:
        for n in range(1, 4000):
            self.assertLessEqual(set(to_roman(n)), set(ALPHABET))

    def test_from_roman_rejects_non_alphabet_characters(self) -> None:
        for s in ("iv", "N", "I "):
            with self.assertRaises(ValueError):
                from_roman(s)

    def test_to_roman_output_is_at_most_15_chars(self) -> None:
        for n in range(1, 4000):
            self.assertLessEqual(len(to_roman(n)), 15)

    def test_to_roman_1_is_I(self) -> None:
        self.assertEqual(to_roman(1), "I")

    def test_to_roman_4_is_IV(self) -> None:
        self.assertEqual(to_roman(4), "IV")

    def test_to_roman_9_is_IX(self) -> None:
        self.assertEqual(to_roman(9), "IX")

    def test_to_roman_40_is_XL(self) -> None:
        self.assertEqual(to_roman(40), "XL")

    def test_to_roman_90_is_XC(self) -> None:
        self.assertEqual(to_roman(90), "XC")

    def test_to_roman_400_is_CD(self) -> None:
        self.assertEqual(to_roman(400), "CD")

    def test_to_roman_900_is_CM(self) -> None:
        self.assertEqual(to_roman(900), "CM")

    def test_to_roman_3999_is_MMMCMXCIX(self) -> None:
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_from_roman_accepts_exactly_the_canonical_outputs(self) -> None:
        canonical = {to_roman(n): n for n in range(1, 4000)}
        for s in all_short_strings():
            if s in canonical:
                self.assertEqual(from_roman(s), canonical[s])
            else:
                with self.assertRaises(ValueError) as ctx:
                    from_roman(s)
                self.assertRegex(str(ctx.exception), r"malformed")
        with self.assertRaises(ValueError) as ctx:
            from_roman("")
        self.assertRegex(str(ctx.exception), r"malformed")

    def test_to_roman_rejects_non_int_input(self) -> None:
        with self.assertRaises(TypeError):
            to_roman("I")
        with self.assertRaises(TypeError):
            to_roman(1.0)


if __name__ == "__main__":
    unittest.main()
