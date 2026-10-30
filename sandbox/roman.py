"""Canonical subtractive Roman numerals for 1 to 3999."""

_PAIRS = (
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


def to_roman(n: int) -> str:
    """Return the canonical subtractive Roman numeral for n (1 to 3999)."""
    if type(n) is not int or n < 1 or n > 3999:
        raise ValueError(f"n must be an int from 1 to 3999, got {n!r}")
    parts = []
    for value, letters in _PAIRS:
        while n >= value:
            parts.append(letters)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Return the integer that s is the canonical Roman numeral of (1 to 3999)."""
    if not isinstance(s, str) or s == "":
        raise ValueError(f"s must be a non-empty str, got {s!r}")
    numeral = _NUMERALS.get(s)
    if numeral is None:
        raise ValueError(f"not a valid Roman numeral for 1 to 3999: {s!r}")
    return numeral


_NUMERALS = {to_roman(n): n for n in range(1, 4000)}
