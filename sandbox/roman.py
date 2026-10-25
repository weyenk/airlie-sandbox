"""Convert between integers 1-3999 and canonical Roman numerals."""

_TABLE = (
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
)

import re

_VALUES = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

_CANONICAL = re.compile(r"M{0,3}(?:CM|CD|D?C{0,3})?(?:XC|XL|L?X{0,3})?(?:IX|IV|V?I{0,3})?")


def to_roman(n: int) -> str:
    """Convert an integer 1-3999 to its canonical uppercase Roman numeral."""
    if not isinstance(n, int) or not 1 <= n <= 3999:
        raise ValueError(f"{n!r} must be between 1 and 3999")
    parts = []
    for value, numeral in _TABLE:
        while n >= value:
            parts.append(numeral)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Parse a canonical uppercase Roman numeral into its integer 1-3999."""
    if not isinstance(s, str) or not s or not _CANONICAL.fullmatch(s):
        raise ValueError(f"{s!r} is not a valid Roman numeral")
    value = 0
    for i, ch in enumerate(s):
        v = _VALUES[ch]
        if i + 1 < len(s) and v < _VALUES[s[i + 1]]:
            value -= v
        else:
            value += v
    if not 1 <= value <= 3999:
        raise ValueError(f"{s!r} is not a valid Roman numeral")
    return value
