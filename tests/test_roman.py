import unittest

from sandbox.roman import to_roman, from_roman


class RomanTest(unittest.TestCase):
    # --- to_roman: canonical return values (AC1-AC9) ---
    def test_to_roman_1_returns_I(self) -> None:
        self.assertEqual(to_roman(1), "I")

    def test_to_roman_4_returns_IV_not_IIII(self) -> None:
        self.assertEqual(to_roman(4), "IV")

    def test_to_roman_9_returns_IX(self) -> None:
        self.assertEqual(to_roman(9), "IX")

    def test_to_roman_40_returns_XL(self) -> None:
        self.assertEqual(to_roman(40), "XL")

    def test_to_roman_90_returns_XC(self) -> None:
        self.assertEqual(to_roman(90), "XC")

    def test_to_roman_400_returns_CD(self) -> None:
        self.assertEqual(to_roman(400), "CD")

    def test_to_roman_900_returns_CM(self) -> None:
        self.assertEqual(to_roman(900), "CM")

    def test_to_roman_1994_returns_MCMXCIV(self) -> None:
        self.assertEqual(to_roman(1994), "MCMXCIV")

    def test_to_roman_3999_returns_MMMCMXCIX(self) -> None:
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    # --- to_roman: out-of-range raises (AC10-AC12) ---
    def test_to_roman_0_raises_range_error(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            to_roman(0)
        self.assertEqual(str(ctx.exception), "to_roman: n must be between 1 and 3999")

    def test_to_roman_4000_raises_range_error(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            to_roman(4000)
        self.assertEqual(str(ctx.exception), "to_roman: n must be between 1 and 3999")

    def test_to_roman_negative_raises_range_error(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            to_roman(-1)
        self.assertEqual(str(ctx.exception), "to_roman: n must be between 1 and 3999")

    # --- from_roman: canonical return values (AC13-AC21) ---
    def test_from_roman_I_returns_1(self) -> None:
        self.assertEqual(from_roman("I"), 1)

    def test_from_roman_IV_returns_4(self) -> None:
        self.assertEqual(from_roman("IV"), 4)

    def test_from_roman_IX_returns_9(self) -> None:
        self.assertEqual(from_roman("IX"), 9)

    def test_from_roman_XL_returns_40(self) -> None:
        self.assertEqual(from_roman("XL"), 40)

    def test_from_roman_XC_returns_90(self) -> None:
        self.assertEqual(from_roman("XC"), 90)

    def test_from_roman_CD_returns_400(self) -> None:
        self.assertEqual(from_roman("CD"), 400)

    def test_from_roman_CM_returns_900(self) -> None:
        self.assertEqual(from_roman("CM"), 900)

    def test_from_roman_MCMXCIV_returns_1994(self) -> None:
        self.assertEqual(from_roman("MCMXCIV"), 1994)

    def test_from_roman_MMMCMXCIX_returns_3999(self) -> None:
        self.assertEqual(from_roman("MMMCMXCIX"), 3999)

    # --- from_roman: malformed input raises (AC22-AC27) ---
    def test_from_roman_lowercase_iv_raises(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("iv")
        self.assertEqual(str(ctx.exception), "from_roman: 'iv' is not a valid Roman numeral")

    def test_from_roman_empty_raises(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("")
        self.assertEqual(str(ctx.exception), "from_roman: '' is not a valid Roman numeral")

    def test_from_roman_VC_raises(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("VC")
        self.assertEqual(str(ctx.exception), "from_roman: 'VC' is not a valid Roman numeral")

    def test_from_roman_IL_raises(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("IL")
        self.assertEqual(str(ctx.exception), "from_roman: 'IL' is not a valid Roman numeral")

    def test_from_roman_MMMM_raises(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("MMMM")
        self.assertEqual(str(ctx.exception), "from_roman: 'MMMM' is not a valid Roman numeral")

    def test_from_roman_I1_raises(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("I1")
        self.assertEqual(str(ctx.exception), "from_roman: 'I1' is not a valid Roman numeral")

    # --- round-trip over a fixed representative sample (AC28) ---
    def test_round_trip_over_representative_sample(self) -> None:
        samples = [1, 9, 10, 40, 90, 100, 400, 900, 1000, 1994, 3999]
        for n in samples:
            self.assertEqual(from_roman(to_roman(n)), n)

    # --- from_roman: run-length and subtractive-pair strictness (AC29-AC32) ---
    def test_from_roman_IIII_raises_run_length(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("IIII")
        self.assertEqual(str(ctx.exception), "from_roman: 'IIII' is not a valid Roman numeral")

    def test_from_roman_VV_raises_run_length(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("VV")
        self.assertEqual(str(ctx.exception), "from_roman: 'VV' is not a valid Roman numeral")

    def test_from_roman_IC_raises_subtractive_pair(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("IC")
        self.assertEqual(str(ctx.exception), "from_roman: 'IC' is not a valid Roman numeral")

    def test_from_roman_IM_raises_subtractive_pair(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            from_roman("IM")
        self.assertEqual(str(ctx.exception), "from_roman: 'IM' is not a valid Roman numeral")


if __name__ == "__main__":
    unittest.main()
