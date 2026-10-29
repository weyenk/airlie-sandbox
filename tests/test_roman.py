import unittest

from sandbox.roman import from_roman, to_roman


class RomanTest(unittest.TestCase):
    def test_to_roman_of_1_returns_I(self) -> None:
        self.assertEqual(to_roman(1), "I")

    def test_to_roman_of_2026_returns_MMXXVI(self) -> None:
        self.assertEqual(to_roman(2026), "MMXXVI")

    def test_to_roman_of_14_returns_XIV(self) -> None:
        self.assertEqual(to_roman(14), "XIV")

    def test_from_roman_round_trips_every_n_from_1_to_3999(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(from_roman(to_roman(n)), n, f"round trip failed for n={n}")

    def test_from_roman_rejects_every_non_canonical_string_of_one_to_four_characters(self) -> None:
        inverse = {to_roman(n): n for n in range(1, 4000)}
        alphabet = "IVXLCDM"
        for length in range(1, 5):
            for index in range(len(alphabet) ** length):
                s = "".join(alphabet[(index // len(alphabet) ** power) % len(alphabet)]
                            for power in range(length - 1, -1, -1))
                if s in inverse:
                    self.assertEqual(from_roman(s), inverse[s], s)
                else:
                    with self.assertRaisesRegex(ValueError, "malformed"):
                        from_roman(s)

    def test_from_roman_rejects_the_examples_named_in_the_request(self) -> None:
        for s in ("IIII", "VV", "xiv"):
            with self.assertRaisesRegex(ValueError, "malformed"):
                from_roman(s)

    def test_from_roman_rejects_the_empty_string(self) -> None:
        with self.assertRaisesRegex(ValueError, "malformed"):
            from_roman("")

    def test_from_roman_rejects_non_string_input(self) -> None:
        for s in (None, 5):
            with self.assertRaisesRegex(ValueError, "malformed"):
                from_roman(s)

    def test_to_roman_rejects_every_integer_outside_1_to_3999(self) -> None:
        for n in list(range(-1000, 0)) + list(range(4000, 5000)):
            with self.assertRaisesRegex(ValueError, r"outside 1\.\.\.3999"):
                to_roman(n)

    def test_to_roman_rejects_non_integer_inputs(self) -> None:
        for n in (1.5, "5", True):
            with self.assertRaises(ValueError):
                to_roman(n)


if __name__ == "__main__":
    unittest.main()
