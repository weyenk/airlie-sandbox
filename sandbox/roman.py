"""Canonical Roman numerals for the 1..3999 range."""

import re

_TABLE = [
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

_CANONICAL = re.compile(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")


def to_roman(n: int) -> str:
    """Return the canonical Roman numeral for n (1..3999)."""
    if not isinstance(n, int) or isinstance(n, bool) or not 1 <= n <= 3999:
        raise ValueError("to_roman: n must be between 1 and 3999")
    parts = []
    for value, letters in _TABLE:
        while n >= value:
            parts.append(letters)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Return the integer for a canonical Roman numeral (1..3999)."""
    if not isinstance(s, str) or not _CANONICAL.match(s):
        raise ValueError(f"from_roman: '{s}' is not a valid Roman numeral")
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for i, ch in enumerate(s):
        value = values[ch]
        if i + 1 < len(s) and value < values[s[i + 1]]:
            total -= value
        else:
            total += value
    if not 1 <= total <= 3999:
        raise ValueError(f"from_roman: '{s}' is not a valid Roman numeral")
    return total
