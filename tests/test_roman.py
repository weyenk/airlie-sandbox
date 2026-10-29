import itertools
import unittest

from sandbox.roman import from_roman, to_roman

# The seven uppercase Roman-numeral letters. The valid set is built from to_roman,
# so the whole-alphabet rejection tests below stand in for the universal criterion.
ROMAN_ALPHABET = "IVXLCDM"


def _all_strings_over_alphabet(lengths):
    """Yield every string of the given lengths over ROMAN_ALPHABET."""
    for length in lengths:
        for combo in itertools.product(ROMAN_ALPHABET, repeat=length):
            yield "".join(combo)


def _valid_strings():
    """The set of strings to_roman returns for 1..3999 (the canonical forms)."""
    return {to_roman(n) for n in range(1, 4000)}


class RomanTest(unittest.TestCase):
    # ---- to_roman: exact canonical values (kill compensating errors) ----
    def test_to_roman_of_one_is_I(self) -> None:
        self.assertEqual(to_roman(1), "I")

    def test_to_roman_of_four_is_IV(self) -> None:
        self.assertEqual(to_roman(4), "IV")

    def test_to_roman_of_nine_is_IX(self) -> None:
        self.assertEqual(to_roman(9), "IX")

    def test_to_roman_of_forty_is_XL(self) -> None:
        self.assertEqual(to_roman(40), "XL")

    def test_to_roman_of_ninety_is_XC(self) -> None:
        self.assertEqual(to_roman(90), "XC")

    def test_to_roman_of_four_hundred_is_CD(self) -> None:
        self.assertEqual(to_roman(400), "CD")

    def test_to_roman_of_nine_hundred_is_CM(self) -> None:
        self.assertEqual(to_roman(900), "CM")

    def test_to_roman_of_3999_is_MMMCMXCIX(self) -> None:
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    # ---- to_roman: range boundaries name the range ----
    def test_to_roman_of_zero_raises_ValueError_naming_the_range(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            to_roman(0)
        self.assertIn("1 to 3999", str(ctx.exception))

    def test_to_roman_of_4000_raises_ValueError_naming_the_range(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            to_roman(4000)
        self.assertIn("1 to 3999", str(ctx.exception))

    # ---- to_roman: whole range returns a string and does not raise ----
    def test_to_roman_returns_a_string_for_every_n_from_1_to_3999(self) -> None:
        for n in range(1, 4000):
            self.assertIsInstance(to_roman(n), str)

    # ---- to_roman: type traps (bool subclasses int; non-int refused) ----
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

    # ---- from_roman: exact canonical values ----
    def test_from_roman_of_M_is_1000(self) -> None:
        self.assertEqual(from_roman("M"), 1000)

    def test_from_roman_of_IV_is_4(self) -> None:
        self.assertEqual(from_roman("IV"), 4)

    def test_from_roman_of_MCMXCIV_is_1994(self) -> None:
        self.assertEqual(from_roman("MCMXCIV"), 1994)

    def test_from_roman_of_MMMCMXCIX_is_3999(self) -> None:
        self.assertEqual(from_roman("MMMCMXCIX"), 3999)

    # ---- from_roman: round-trip over the full range ----
    def test_from_roman_of_to_roman_is_the_identity_for_every_n_from_1_to_3999(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)

    def test_from_roman_recovers_n_for_every_string_to_roman_returns(self) -> None:
        mapping = {}
        for n in range(1, 4000):
            s = to_roman(n)
            self.assertNotIn(s, mapping)  # to_roman is injective: each numeral is unique
            mapping[s] = n
        for s, n in mapping.items():
            self.assertEqual(from_roman(s), n)

    # ---- from_roman: the empty string is refused (pattern is all-optional) ----
    def test_from_roman_of_empty_string_raises_ValueError(self) -> None:
        with self.assertRaises(ValueError):
            from_roman("")

    # ---- from_roman: whole-alphabet rejection, 1..4 chars (2800 strings) ----
    def test_from_roman_raises_ValueError_for_every_non_canonical_string_of_one_to_four_characters(self) -> None:
        valid = _valid_strings()
        for s in _all_strings_over_alphabet(range(1, 5)):
            if s in valid:
                continue
            with self.assertRaises(ValueError):
                from_roman(s)
        for s in ("A", "iv", "I V", "1"):  # pin the character set
            with self.assertRaises(ValueError):
                from_roman(s)

    # ---- from_roman: whole-alphabet rejection, 5..7 chars ----
    def test_from_roman_raises_ValueError_for_every_non_canonical_string_of_five_to_seven_characters(self) -> None:
        valid = _valid_strings()
        for s in _all_strings_over_alphabet(range(5, 8)):
            if s in valid:
                continue
            with self.assertRaises(ValueError):
                from_roman(s)
        for s in ("AAAAA", "MMMMM", "M" * 16):  # pin the character set / length
            with self.assertRaises(ValueError):
                from_roman(s)


if __name__ == "__main__":
    unittest.main()
