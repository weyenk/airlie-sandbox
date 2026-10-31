"""Convert between integers 1..3999 and standard Roman numerals."""

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

_LETTER_VALUES = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}


def to_roman(n: int) -> str:
    """Return the standard Roman numeral for n (1..3999), or raise ValueError."""
    if not isinstance(n, int) or isinstance(n, bool) or n < 1 or n > 3999:
        raise ValueError(f"n must be an integer from 1 to 3999, got {n!r}")
    parts = []
    for value, numeral in _TABLE:
        while n >= value:
            parts.append(numeral)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Return the integer for a standard Roman numeral, or raise ValueError."""
    if not isinstance(s, str) or s == "":
        raise ValueError(f"expected a Roman numeral string, got {s!r}")
    if any(char not in _LETTER_VALUES for char in s):
        raise ValueError(f"expected only the letters MCDXLVI, got {s!r}")
    value = 0
    for i, char in enumerate(s):
        current = _LETTER_VALUES[char]
        if i + 1 < len(s) and current < _LETTER_VALUES[s[i + 1]]:
            value -= current
        else:
            value += current
    if not 1 <= value <= 3999 or s != to_roman(value):
        raise ValueError(f"{s!r} is not a standard Roman numeral")
    return value
