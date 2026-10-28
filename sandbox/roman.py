"""Convert between integers and Roman numerals for 1 to 3999."""

import re

_VALUES = [
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

_LETTERS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

_CANONICAL = re.compile(r"M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})")


def to_roman(n: int) -> str:
    """Return the standard Roman numeral for an integer 1..3999."""
    if isinstance(n, bool) or not isinstance(n, int) or not 1 <= n <= 3999:
        raise ValueError("n must be between 1 and 3999")
    parts = []
    for value, symbol in _VALUES:
        while n >= value:
            parts.append(symbol)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Return the integer value of a canonical uppercase Roman numeral."""
    if not isinstance(s, str):
        raise ValueError("invalid Roman numeral: " + str(s))
    if s == "" or not _CANONICAL.fullmatch(s):
        raise ValueError("invalid Roman numeral: " + s)
    total = 0
    for i, ch in enumerate(s):
        value = _LETTERS[ch]
        if i + 1 < len(s) and value < _LETTERS[s[i + 1]]:
            total -= value
        else:
            total += value
    return total
