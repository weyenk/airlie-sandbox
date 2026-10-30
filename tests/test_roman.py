import itertools
import unittest

import sandbox.roman


class RomanTest(unittest.TestCase):
    def test_import_and_signatures(self) -> None:
        self.assertTrue(callable(sandbox.roman.to_roman))
        self.assertTrue(callable(sandbox.roman.from_roman))
        self.assertEqual(
            sandbox.roman.to_roman.__annotations__, {"n": int, "return": str}
        )
        self.assertEqual(
            sandbox.roman.from_roman.__annotations__, {"s": str, "return": int}
        )

    def test_smoke_to_roman_1994(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(1994), "MCMXCIV")

    def test_from_roman_of_to_roman_round_trips_all_3999(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(
                sandbox.roman.from_roman(sandbox.roman.to_roman(n)), n,
                f"round-trip failed for n={n}",
            )

    def test_to_roman_rejects_out_of_range_with_1_3999_phrase(self) -> None:
        for n in (0, -1, 4000):
            with self.assertRaisesRegex(ValueError, r"1\.\.3999"):
                sandbox.roman.to_roman(n)

    def test_from_roman_rejects_empty_string(self) -> None:
        with self.assertRaises(ValueError):
            sandbox.roman.from_roman("")

    def test_from_roman_rejects_every_1_to_4_char_string_not_in_valid_set(self) -> None:
        valid = {sandbox.roman.to_roman(n) for n in range(1, 4000)}
        self.assertEqual(len(valid), 3999)
        alphabet = "IVXLCDM"
        for length in (1, 2, 3, 4):
            for combo in itertools.product(alphabet, repeat=length):
                s = "".join(combo)
                if s in valid:
                    continue
                with self.assertRaises(ValueError, msg=f"from_roman({s!r}) should raise"):
                    sandbox.roman.from_roman(s)

    def test_to_roman_of_from_roman_round_trips_every_valid_numeral(self) -> None:
        valid = {sandbox.roman.to_roman(n) for n in range(1, 4000)}
        self.assertEqual(len(valid), 3999)
        for s in valid:
            self.assertEqual(
                sandbox.roman.to_roman(sandbox.roman.from_roman(s)), s,
                f"round-trip failed for s={s!r}",
            )


if __name__ == "__main__":
    unittest.main()
