"""Canonical Roman-numeral conversion for the 1 to 3999 range."""

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
    parts = []
    for value, symbol in TABLE:
        while n >= value:
            parts.append(symbol)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Read a numeral left to right, subtracting a value followed by a larger one."""
    total = 0
    for i, ch in enumerate(s):
        value = VALUES[ch]
        if i + 1 < len(s) and value < VALUES[s[i + 1]]:
            total -= value
        else:
            total += value
    return total
