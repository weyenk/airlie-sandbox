"""Roman numeral conversion for 1..3999."""

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

_LETTER_VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def to_roman(n: int) -> str:
    """Return the canonical Roman numeral for n in 1..3999."""
    if not 1 <= n <= 3999:
        raise ValueError(f"n must be in 1..3999, got {n}")
    parts = []
    for value, letters in _TABLE:
        while n >= value:
            parts.append(letters)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Return the sum of the letter values in s (lenient, no subtractive rules)."""
    if not s:
        raise ValueError("s must not be empty")
    for char in s:
        if char not in _LETTER_VALUES:
            raise ValueError(f"invalid character {char!r} in Roman numeral")
    return sum(_LETTER_VALUES[c] for c in s)
