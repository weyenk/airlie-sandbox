import unittest

from sandbox.roman import to_roman


def standard_roman(n: int) -> str:
    """The conventional Roman numeral of n, by greedy subtraction over the place table."""
    table = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    parts = []
    for value, numeral in table:
        while n >= value:
            parts.append(numeral)
            n -= value
    return "".join(parts)


class ToRomanTest(unittest.TestCase):
    def test_to_roman_matches_the_standard_form_for_every_integer_in_1_to_3999(self) -> None:
        for n in range(1, 4000):
            self.assertEqual(to_roman(n), standard_roman(n))

    def test_to_roman_pins_the_request_examples(self) -> None:
        self.assertEqual(to_roman(1994), "MCMXCIV")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_to_roman_raises_valueerror_for_every_integer_outside_1_to_3999(self) -> None:
        for n in range(0, 4001):
            if n < 1 or n > 3999:
                with self.assertRaises(ValueError):
                    to_roman(n)
            else:
                to_roman(n)


if __name__ == "__main__":
    unittest.main()
