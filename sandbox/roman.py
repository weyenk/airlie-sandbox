"""Roman numerals for 1..3999."""

from __future__ import annotations

_VALUES = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

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


def to_roman(n: int) -> str:
    """Convert an integer 1..3999 to its canonical Roman numeral."""
    if not 1 <= n <= 3999:
        raise ValueError(f"{n} is not in 1..3999")
    parts: list[str] = []
    for value, symbol in _TABLE:
        while n >= value:
            parts.append(symbol)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Parse an uppercase Roman numeral into an integer 1..3999."""
    if not s or any(ch not in _VALUES for ch in s):
        raise ValueError(f"{s!r} is not a valid Roman numeral")
    if s.count("V") > 1 or s.count("L") > 1 or s.count("D") > 1:
        raise ValueError(f"{s!r} is not a valid Roman numeral")
    for i, ch in enumerate(s):
        run = 1
        while i + run < len(s) and s[i + run] == ch:
            run += 1
        if run > 3:
            raise ValueError(f"{s!r} is not a valid Roman numeral")
        if i + 1 < len(s) and _VALUES[ch] < _VALUES[s[i + 1]]:
            if ch + s[i + 1] not in {"IV", "IX", "XL", "XC", "CD", "CM"}:
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
