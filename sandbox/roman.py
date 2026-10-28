"""Convert integers 1-3999 to canonical Roman numerals and back."""

from __future__ import annotations

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

_SYMBOLS: dict[str, int] = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def to_roman(n: int) -> str:
    """Return the canonical Roman numeral for an integer 1-3999."""
    if type(n) is not int:
        raise ValueError(f"to_roman: {n!r} must be an int, got {type(n).__name__}")
    if not 1 <= n <= 3999:
        raise ValueError(f"to_roman: {n} out of range, expected 1..3999")
    parts: list[str] = []
    for value, letters in _TABLE:
        if n >= value:
            parts.append(letters * (n // value))
            n %= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Parse a canonical Roman numeral (case-insensitive) back to an integer."""
    if type(s) is not str:
        raise ValueError(f"from_roman: {s!r} must be a str, got {type(s).__name__}")
    s = s.upper()
    if not s:
        raise ValueError("from_roman: '' is malformed")
    values = [_SYMBOLS.get(ch) for ch in s]
    if any(v is None for v in values):
        raise ValueError(f"from_roman: {s!r} is malformed")
    total = 0
    for i, v in enumerate(values):
        if i + 1 < len(values) and v < values[i + 1]:
            total -= v
        else:
            total += v
    if to_roman(total) != s:
        raise ValueError(f"from_roman: {s!r} is malformed")
    return total
