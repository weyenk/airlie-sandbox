import itertools
import unittest

from sandbox.roman import from_roman, to_roman


class RomanTest(unittest.TestCase):
    def test_exposes_to_roman_and_from_roman(self) -> None:
        """to_roman and from_roman are importable and callable."""
        import sandbox.roman

        self.assertTrue(callable(sandbox.roman.to_roman))
        self.assertTrue(callable(sandbox.roman.from_roman))

    def test_to_roman_matches_the_standard_table(self) -> None:
        """The request's own pinned pairs convert in both directions."""
        pairs = {
            1: "I",
            4: "IV",
            9: "IX",
            40: "XL",
            90: "XC",
            400: "CD",
            900: "CM",
            1994: "MCMXCIV",
            3999: "MMMCMXCIX",
        }
        for n, numeral in pairs.items():
            self.assertEqual(to_roman(n), numeral)
            self.assertEqual(from_roman(numeral), n)

    def test_to_roman_returns_a_roman_string_for_every_n_in_range(self) -> None:
        """Every n in 1..3999 yields a non-empty string of I, V, X, L, C, D, M."""
        letters = set("IVXLCDM")
        for n in range(1, 4000):
            s = to_roman(n)
            self.assertIsInstance(s, str)
            self.assertGreater(len(s), 0)
            self.assertTrue(set(s) <= letters, f"{n} -> {s!r} has a non-Roman character")

    def test_from_roman_round_trips_every_n_in_range(self) -> None:
        """from_roman(to_roman(n)) == n for every n in 1..3999."""
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n)

    def test_to_roman_raises_value_error_for_non_integer_or_out_of_range_input(self) -> None:
        """to_roman raises ValueError for each of the eight named bad inputs."""
        for bad in (0, -1, 4000, 1.5, "5", None, True, False):
            with self.assertRaises(ValueError):
                to_roman(bad)

    def test_from_roman_raises_value_error_for_empty_string(self) -> None:
        """from_roman('') raises ValueError."""
        with self.assertRaises(ValueError):
            from_roman("")

    def test_from_roman_accepts_exactly_the_valid_short_numerals(self) -> None:
        """Every one-to-four-character numeral is accepted exactly when it is valid."""
        valid = {to_roman(n): n for n in range(1, 4000)}
        letters = "IVXLCDM"
        accepted = 0
        refused = 0
        for length in (1, 2, 3, 4):
            for combo in itertools.product(letters, repeat=length):
                s = "".join(combo)
                if s in valid:
                    self.assertEqual(from_roman(s), valid[s], f"{s!r} should be accepted")
                    accepted += 1
                else:
                    with self.assertRaises(ValueError, msg=f"{s!r} should be refused"):
                        from_roman(s)
                    refused += 1
        self.assertEqual(accepted, 346)
        self.assertEqual(refused, 2454)
        self.assertIn("L", valid)
        for s in ("VV", "VC", "IIII", "IL", "MMMM"):
            self.assertNotIn(s, valid)

    def test_from_roman_returns_the_original_n_for_every_valid_output(self) -> None:
        """from_roman(s) == n for every s in the valid set, at any length."""
        valid = {to_roman(n): n for n in range(1, 4000)}
        self.assertEqual(len(valid), 3999)
        for s, n in valid.items():
            self.assertEqual(from_roman(s), n)


if __name__ == "__main__":
    unittest.main()
