"""Roman numerals: to_roman and from_roman for 1 to 3999."""

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

_LETTERS = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def to_roman(n: int) -> str:
    """Canonical greedy-subtractive Roman numeral for 1..3999."""
    if not 1 <= n <= 3999:
        raise ValueError(f"n must be in 1..3999, got {n}")
    parts = []
    for value, numeral in _TABLE:
        while n >= value:
            parts.append(numeral)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Parse a canonical Roman numeral for 1..3999, else raise ValueError."""
    if not s or any(ch not in _LETTERS for ch in s):
        raise ValueError(f"not a Roman numeral: {s!r}")
    value = 0
    for i, ch in enumerate(s):
        v = _LETTERS[ch]
        if i + 1 < len(s) and _LETTERS[s[i + 1]] > v:
            value -= v
        else:
            value += v
    if not 1 <= value <= 3999 or to_roman(value) != s:
        raise ValueError(f"not a canonical Roman numeral: {s!r}")
    return value
