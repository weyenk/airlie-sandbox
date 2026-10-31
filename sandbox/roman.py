"""Canonical Roman numeral conversion for 1 to 3999."""

_VALUES = [
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
    """Return the canonical subtractive Roman numeral for n (1 to 3999)."""
    if not (isinstance(n, int) and not isinstance(n, bool)) or not 1 <= n <= 3999:
        raise ValueError("n must be an integer from 1 to 3999, got " + repr(n))
    parts = []
    for value, numeral in _VALUES:
        while n >= value:
            parts.append(numeral)
            n -= value
    return "".join(parts)
