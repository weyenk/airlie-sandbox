import inspect
import itertools
import unittest

import sandbox
import sandbox.roman


class RomanTest(unittest.TestCase):
    def test_import_exposes_both_callables(self) -> None:
        self.assertTrue(callable(sandbox.roman.to_roman))
        self.assertTrue(callable(sandbox.roman.from_roman))
        to_sig = inspect.signature(sandbox.roman.to_roman)
        self.assertEqual(list(to_sig.parameters), ["n"])
        self.assertEqual(to_sig.parameters["n"].annotation, int)
        self.assertEqual(to_sig.return_annotation, str)
        from_sig = inspect.signature(sandbox.roman.from_roman)
        self.assertEqual(list(from_sig.parameters), ["s"])
        self.assertEqual(from_sig.parameters["s"].annotation, str)
        self.assertEqual(from_sig.return_annotation, int)

    def test_to_roman_output_is_structurally_valid_for_every_n(self) -> None:
        allowed = set("IVXLCDM")
        for n in range(1, 4000):
            s = sandbox.roman.to_roman(n)
            self.assertIsInstance(s, str)
            self.assertTrue(set(s) <= allowed, f"{s} uses letters outside IVXLCDM")
            for letter in "IVXLCDM":
                self.assertNotIn(letter * 4, s, f"{s} repeats {letter} more than three times")
            for bad in ("VC", "LM", "IL", "XD"):
                self.assertNotIn(bad, s, f"{s} contains {bad}")

    def test_round_trip_holds_for_every_n(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(sandbox.roman.from_roman(sandbox.roman.to_roman(n)), n)

    def test_to_roman_out_of_range_raises_valueerror(self) -> None:
        for n in (0, 4000):
            with self.assertRaises(ValueError) as ctx:
                sandbox.roman.to_roman(n)
            self.assertIn("1 to 3999", str(ctx.exception))

    def test_to_roman_non_int_raises_valueerror(self) -> None:
        for arg in (1.5, "IV", True, None):
            with self.assertRaises(ValueError):
                sandbox.roman.to_roman(arg)

    def test_from_roman_refuses_every_invalid_1_to_4_char_string(self) -> None:
        valid = {sandbox.roman.to_roman(n) for n in range(1, 4000)}
        alphabet = "IVXLCDM"
        for length in range(1, 5):
            for candidate in itertools.product(alphabet, repeat=length):
                s = "".join(candidate)
                if s in valid:
                    self.assertEqual(sandbox.roman.to_roman(sandbox.roman.from_roman(s)), s)
                else:
                    with self.assertRaises(ValueError) as ctx:
                        sandbox.roman.from_roman(s)
                    self.assertIn("malformed", str(ctx.exception))

    def test_from_roman_empty_string_raises_valueerror(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            sandbox.roman.from_roman("")
        self.assertIn("malformed", str(ctx.exception))

    def test_from_roman_non_str_raises_valueerror(self) -> None:
        for arg in (1, 1.5, None):
            with self.assertRaises(ValueError):
                sandbox.roman.from_roman(arg)


if __name__ == "__main__":
    unittest.main()
