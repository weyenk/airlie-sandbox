import unittest


class RomanTest(unittest.TestCase):
    def test_import_and_signatures(self) -> None:
        import sandbox.roman

        self.assertTrue(callable(sandbox.roman.to_roman))
        self.assertTrue(callable(sandbox.roman.from_roman))
        self.assertEqual(sandbox.roman.to_roman.__annotations__, {"n": int, "return": str})
        self.assertEqual(sandbox.roman.from_roman.__annotations__, {"s": str, "return": int})

    def test_smoke_to_roman_1994(self) -> None:
        import sandbox.roman

        self.assertEqual(sandbox.roman.to_roman(1994), "MCMXCIV")


if __name__ == "__main__":
    unittest.main()
