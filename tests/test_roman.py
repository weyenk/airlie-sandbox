import unittest

import sandbox.roman


class RomanTest(unittest.TestCase):
    # --- to_roman: known values ---

    def test_to_roman_1_is_i(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(1), "I")

    def test_to_roman_4_is_iv(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(4), "IV")

    def test_to_roman_40_is_xl(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(40), "XL")

    def test_to_roman_400_is_cd(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(400), "CD")

    def test_to_roman_3999_is_mmmcmxcix(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(3999), "MMMCMXCIX")

    def test_to_roman_known_values(self) -> None:
        self.assertEqual(sandbox.roman.to_roman(9), "IX")
        self.assertEqual(sandbox.roman.to_roman(90), "XC")
        self.assertEqual(sandbox.roman.to_roman(900), "CM")
        self.assertEqual(sandbox.roman.to_roman(1994), "MCMXCIV")

    # --- to_roman: range errors ---

    def test_to_roman_0_raises_range(self) -> None:
        with self.assertRaisesRegex(ValueError, "1 to 3999"):
            sandbox.roman.to_roman(0)

    def test_to_roman_4000_raises_range(self) -> None:
        with self.assertRaisesRegex(ValueError, "1 to 3999"):
            sandbox.roman.to_roman(4000)

    # --- to_roman: type errors ---

    def test_to_roman_non_int_raises_not_an_int(self) -> None:
        for bad in ("IV", 1.5, True):
            with self.assertRaisesRegex(ValueError, "not an int"):
                sandbox.roman.to_roman(bad)

    # --- from_roman: known values ---

    def test_from_roman_i_is_1(self) -> None:
        self.assertEqual(sandbox.roman.from_roman("I"), 1)

    def test_from_roman_mmmcmxcix_is_3999(self) -> None:
        self.assertEqual(sandbox.roman.from_roman("MMMCMXCIX"), 3999)

    # --- from_roman: malformed ---

    def test_from_roman_abc_raises_not_roman(self) -> None:
        with self.assertRaisesRegex(ValueError, "not a Roman numeral"):
            sandbox.roman.from_roman("ABC")

    def test_from_roman_iiii_raises_not_roman(self) -> None:
        with self.assertRaisesRegex(ValueError, "not a Roman numeral") as ctx:
            sandbox.roman.from_roman("IIII")
        self.assertNotIn("1 to 3999", str(ctx.exception))

    def test_from_roman_malformed_raises_not_roman(self) -> None:
        for bad in ("", "v", "VV", "LL", "DD", "VX", "IC"):
            with self.assertRaisesRegex(ValueError, "not a Roman numeral"):
                sandbox.roman.from_roman(bad)

    # --- from_roman: range ---

    def test_from_roman_mmmm_raises_range(self) -> None:
        with self.assertRaisesRegex(ValueError, "1 to 3999") as ctx:
            sandbox.roman.from_roman("MMMM")
        self.assertNotIn("not a Roman numeral", str(ctx.exception))

    # --- round trip ---

    def test_round_trip(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(sandbox.roman.from_roman(sandbox.roman.to_roman(n)), n)


if __name__ == "__main__":
    unittest.main()
