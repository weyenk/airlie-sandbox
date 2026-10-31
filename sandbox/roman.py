"""Standard-library Roman numeral conversion for integers 1..3999."""

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
    """Canonical subtractive Roman numeral for n in 1..3999."""
    if isinstance(n, bool) or not isinstance(n, int) or not 1 <= n <= 3999:
        raise ValueError("to_roman expects an int in 1..3999")
    parts: list[str] = []
    for value, letters in _TABLE:
        while n >= value:
            parts.append(letters)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Inverse of to_roman: parse a canonical Roman numeral back to an int."""
    if not isinstance(s, str):
        raise ValueError("from_roman got a malformed numeral")
    if len(s) == 0 or len(s) > 15 or any(ch not in _VALUES for ch in s):
        raise ValueError("from_roman expected a numeral of 1 to 15 characters")
    total = 0
    for i, ch in enumerate(s):
        value = _VALUES[ch]
        if i + 1 < len(s) and value < _VALUES[s[i + 1]]:
            total -= value
        else:
            total += value
    if not 1 <= total <= 3999 or to_roman(total) != s:
        raise ValueError("from_roman got a malformed numeral")
    return total
