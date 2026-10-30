"""Canonical Roman-numeral conversion for the 1 to 3999 range."""

import re

CANONICAL = re.compile(r"M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})")

TABLE = [
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

VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def to_roman(n: int) -> str:
    """Build the canonical upper-case numeral for n greedily, largest first."""
    if n < 1 or n > 3999:
        raise ValueError(f"n must be in 1..3999, got {n}")
    parts = []
    for value, symbol in TABLE:
        while n >= value:
            parts.append(symbol)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Read a numeral left to right, subtracting a value followed by a larger one."""
    if not s or not CANONICAL.fullmatch(s):
        raise ValueError(f"not a canonical Roman numeral: {s!r}")
    total = 0
    for i, ch in enumerate(s):
        value = VALUES[ch]
        if i + 1 < len(s) and value < VALUES[s[i + 1]]:
            total -= value
        else:
            total += value
    return total
