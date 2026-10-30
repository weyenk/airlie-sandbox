"""Canonical Roman-numeral conversion for integers 1..3999."""

from __future__ import annotations

_TABLE: tuple[tuple[int, str], ...] = (
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

_VALUES: dict[str, int] = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def to_roman(n: int) -> str:
    """Return the canonical Roman numeral for n in 1..3999, else raise ValueError."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise ValueError(f"{n!r} is not an integer in 1..3999")
    if not 1 <= n <= 3999:
        raise ValueError(f"{n} is outside the supported range 1..3999")
    parts: list[str] = []
    for value, numeral in _TABLE:
        while n >= value:
            parts.append(numeral)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Return the integer 1..3999 for a canonical Roman numeral, else raise ValueError."""
    if not isinstance(s, str):
        raise ValueError(f"{s!r} is not a roman numeral")
    if not s or any(ch not in _VALUES for ch in s):
        raise ValueError(f"{s!r} is not a roman numeral")
    value = 0
    for i, ch in enumerate(s):
        v = _VALUES[ch]
        if i + 1 < len(s) and v < _VALUES[s[i + 1]]:
            value -= v
        else:
            value += v
    if not 1 <= value <= 3999:
        raise ValueError(f"{s!r} is outside the supported range 1..3999")
    if to_roman(value) != s:
        raise ValueError(f"{s!r} is not a roman numeral")
    return value
