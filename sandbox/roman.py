"""Roman-numeral conversion for integers 1 to 3999."""

import re

_TOKENS = [
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

_LETTER_VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

_CANONICAL = re.compile(r"M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})")


def to_roman(n: int) -> str:
    """Convert an integer 1..3999 to its canonical Roman numeral."""
    if isinstance(n, bool) or not isinstance(n, int) or not 1 <= n <= 3999:
        raise ValueError(f"n must be an integer in 1..3999, got {n!r}")
    parts = []
    for value, token in _TOKENS:
        while n >= value:
            parts.append(token)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Parse a canonical Roman numeral string back to its integer value."""
    if not isinstance(s, str) or s == "":
        raise ValueError(f"expected a non-empty Roman numeral string, got {s!r}")
    if not _CANONICAL.fullmatch(s):
        raise ValueError(f"not a valid Roman numeral: {s!r}")
    total = 0
    for i, letter in enumerate(s):
        value = _LETTER_VALUES[letter]
        if i < len(s) - 1 and value < _LETTER_VALUES[s[i + 1]]:
            total -= value
        else:
            total += value
    return total
