"""Roman numeral conversion for integers 1..3999."""

from __future__ import annotations

_PLACES = [
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

_LETTERS = set("IVXLCDM")

_VALUE = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def to_roman(n: int) -> str:
    """Return the standard Roman numeral for n, 1 <= n <= 3999."""
    if isinstance(n, bool) or not isinstance(n, int) or not 1 <= n <= 3999:
        raise ValueError(f"n must be an integer in 1..3999, got {n!r}")
    parts: list[str] = []
    for value, numeral in _PLACES:
        while n >= value:
            parts.append(numeral)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Return the integer for a standard Roman numeral, or raise ValueError."""
    if not isinstance(s, str) or not s or any(c not in _LETTERS for c in s):
        raise ValueError(f"not a Roman numeral: {s!r}")
    value = 0
    for i, c in enumerate(s):
        weight = _VALUE[c]
        if i + 1 < len(s) and _VALUE[s[i + 1]] > weight:
            value -= weight
        else:
            value += weight
    if not 1 <= value <= 3999 or to_roman(value) != s:
        raise ValueError(f"not a canonical Roman numeral: {s!r}")
    return value
