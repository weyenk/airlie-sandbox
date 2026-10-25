import unittest

from sandbox.roman import from_roman, to_roman


class RomanTest(unittest.TestCase):
    def test_to_roman_of_the_table_values(self) -> None:
        # AC1: canonical uppercase Roman numerals for the table values.
        cases = [
            (1, "I"),
            (4, "IV"),
            (9, "IX"),
            (10, "X"),
            (40, "XL"),
            (90, "XC"),
            (100, "C"),
            (400, "CD"),
            (900, "CM"),
            (1994, "MCMXCIV"),
            (3999, "MMMCMXCIX"),
        ]
        for n, expected in cases:
            with self.subTest(n=n):
                self.assertEqual(to_roman(n), expected)

    def test_from_roman_of_the_table_values(self) -> None:
        # AC2: the reverse of AC1. The subtractive rows (4, 9, 40, 90, 400,
        # 900) guard against a sum-without-subtraction parser.
        cases = [
            ("I", 1),
            ("IV", 4),
            ("IX", 9),
            ("X", 10),
            ("XL", 40),
            ("XC", 90),
            ("C", 100),
            ("CD", 400),
            ("CM", 900),
            ("MCMXCIV", 1994),
            ("MMMCMXCIX", 3999),
        ]
        for s, expected in cases:
            with self.subTest(s=s):
                self.assertEqual(from_roman(s), expected)

    def test_round_trip_over_every_integer_and_canonical_numeral(self) -> None:
        # AC3: every integer 1..3999 round-trips, and so does every canonical
        # numeral (the generator yields exactly the canonical set).
        for n in range(1, 4000):
            with self.subTest(n=n):
                self.assertEqual(from_roman(to_roman(n)), n)
        for s in (to_roman(n) for n in range(1, 4000)):
            with self.subTest(s=s):
                self.assertEqual(to_roman(from_roman(s)), s)

    def test_to_roman_rejects_out_of_range_and_non_int(self) -> None:
        # AC4: 0, 4000, -1, 1.5 and '4' all take the range branch (never
        # TypeError) with the same message phrase.
        for bad in (0, 4000, -1, 1.5, "4"):
            with self.subTest(bad=bad):
                with self.assertRaisesRegex(ValueError, "must be between 1 and 3999"):
                    to_roman(bad)

    def test_from_roman_rejects_malformed_input(self) -> None:
        # AC5: malformed input raises the validity phrase. Case-sensitive, so
        # 'mm' fails; bounded M{0,3}, so 'MMMM' fails; non-canonical
        # thousands/tens pairs 'LM' and 'XM' are rejected.
        for bad in ("", "IIII", "VV", "IC", "mm", "MMMM", "LM", "XM"):
            with self.subTest(bad=bad):
                with self.assertRaisesRegex(ValueError, "is not a valid Roman numeral"):
                    from_roman(bad)

    def test_from_roman_accepts_canonical_mx_and_mmmc(self) -> None:
        # DEVIATION (pinned in-test): AC5 lists 'MX' and 'MMMC' as malformed,
        # but they are the canonical forms of 1010 and 3100; rejecting them
        # would break AC3's round-trip at n=1010/3100. So the tests instead
        # assert they parse to those ints.
        self.assertEqual(from_roman("MX"), 1010)
        self.assertEqual(from_roman("MMMC"), 3100)


if __name__ == "__main__":
    unittest.main()
