"""Roman-numeral conversion for the sandbox: to_roman and from_roman for 1..3999."""

# Canonical value table in descending order.
_TABLE: list[tuple[int, str]] = [
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

# Subtractive pairs, longest first.
_PAIRS: dict[str, int] = {"CM": 900, "CD": 400, "XC": 90, "XL": 40, "IX": 9, "IV": 4}

# Single-letter place values.
_LETTERS: dict[str, int] = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}


def to_roman(n: int) -> str:
    """Return the canonical Roman numeral for n (1..3999)."""
    parts: list[str] = []
    for value, numeral in _TABLE:
        while n >= value:
            parts.append(numeral)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Return the integer value of a Roman numeral string."""
    total = 0
    i = 0
    while i < len(s):
        pair = s[i : i + 2]
        if pair in _PAIRS:
            total += _PAIRS[pair]
            i += 2
        else:
            total += _LETTERS[s[i]]
            i += 1
    return total
