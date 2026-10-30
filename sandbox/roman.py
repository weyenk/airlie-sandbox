"""Convert integers to Roman numerals and back, for 1 to 3999."""

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

_VALUES = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
}


def to_roman(n: int) -> str:
    """Convert an integer 1..3999 to its Roman numeral, or raise ValueError."""
    if not 1 <= n <= 3999:
        raise ValueError(f"n must be between 1 and 3999, got {n}")
    parts = []
    for value, numeral in _TABLE:
        while n >= value:
            parts.append(numeral)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Parse a Roman numeral string to an integer 1..3999, or raise ValueError."""
    if not s:
        raise ValueError("numeral must not be empty")
    total = 0
    i = 0
    while i < len(s):
        if s[i : i + 2] in _VALUES:
            token = s[i : i + 2]
            i += 2
        elif s[i] in _VALUES:
            token = s[i]
            i += 1
        else:
            raise ValueError(f"unrecognized character at position {i} in {s!r}")
        total += _VALUES[token]
    if not 1 <= total <= 3999:
        raise ValueError(f"total {total} is outside 1..3999 for {s!r}")
    if to_roman(total) != s:
        raise ValueError(f"{s!r} is not a canonical Roman numeral")
    return total
