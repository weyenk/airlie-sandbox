"""Tests for sandbox.roman: to_roman and from_roman over 1..3999."""

import itertools
import unittest

from sandbox.roman import from_roman, to_roman

UPPERCASE_ROMAN = "MDCLXIV"
MIXED_ROMAN = "MDCLXIVmdclxiv"
UPPERCASE_SET = set(UPPERCASE_ROMAN)


def all_strings_over(alphabet: str, min_len: int = 1, max_len: int = 4) -> list[str]:
    """Every string of min_len..max_len characters over alphabet, in length order."""
    strings: list[str] = []
    for length in range(min_len, max_len + 1):
        strings.extend("".join(chars) for chars in itertools.product(alphabet, repeat=length))
    return strings


def valid_outputs() -> dict[str, int]:
    """Each valid roman numeral string mapped to the integer to_roman turns into it."""
    return {to_roman(n): n for n in range(1, 4000)}


class RomanTest(unittest.TestCase):
    def test_round_trip_over_every_integer_1_to_3999(self) -> None:
        for n in range(1, 4000):
            numeral = to_roman(n)
            self.assertIsInstance(numeral, str, f"to_roman({n}) did not return a str")
            self.assertEqual(
                from_roman(numeral),
                n,
                f"from_roman(to_roman({n})) != {n} (got {from_roman(numeral)!r})",
            )

    def test_from_roman_rejects_every_1_to_4_char_string_not_a_valid_output(self) -> None:
        valid = valid_outputs()
        for s in all_strings_over(UPPERCASE_ROMAN):
            if s in valid:
                self.assertEqual(
                    from_roman(s),
                    valid[s],
                    f"from_roman({s!r}) != {valid[s]}",
                )
            else:
                with self.assertRaises(ValueError, msg=f"from_roman({s!r}) did not raise"):
                    from_roman(s)

    def test_from_roman_empty_string_raises(self) -> None:
        with self.assertRaises(ValueError, msg="from_roman('') did not raise"):
            from_roman("")

    def test_to_roman_out_of_range_raises(self) -> None:
        for n in (0, -1, -100, 4000, 4001, 10**6):
            with self.assertRaises(ValueError, msg=f"to_roman({n}) did not raise"):
                to_roman(n)

    def test_to_roman_non_integer_raises(self) -> None:
        for x in ("4", 4.0, None, True, False):
            with self.assertRaises(ValueError, msg=f"to_roman({x!r}) did not raise"):
                to_roman(x)

    def test_from_roman_rejects_every_1_to_4_char_string_with_lowercase_or_non_roman_char(self) -> None:
        for s in all_strings_over(MIXED_ROMAN):
            if any(char not in UPPERCASE_SET for char in s):
                with self.assertRaises(ValueError, msg=f"from_roman({s!r}) did not raise"):
                    from_roman(s)
        for s in ("A", "1", " "):
            with self.assertRaises(ValueError, msg=f"from_roman({s!r}) did not raise"):
                from_roman(s)

    def test_from_roman_rejects_every_1_to_4_char_uppercase_string_not_a_valid_output_and_over_4_char_out_of_range(self) -> None:
        valid = valid_outputs()
        for s in all_strings_over(UPPERCASE_ROMAN):
            if s in valid:
                self.assertEqual(
                    from_roman(s),
                    valid[s],
                    f"from_roman({s!r}) != {valid[s]}",
                )
            else:
                with self.assertRaises(ValueError, msg=f"from_roman({s!r}) did not raise"):
                    from_roman(s)
        with self.assertRaises(ValueError, msg="from_roman('MMMMM') did not raise"):
            from_roman("MMMMM")

    def test_to_roman_4_is_subtractive_iv(self) -> None:
        self.assertEqual(to_roman(4), "IV")


if __name__ == "__main__":
    unittest.main()
