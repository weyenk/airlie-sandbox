"""Canonical Roman-numeral conversion for 1..3999."""

_PAIRS = [
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
    """Return the canonical Roman numeral for n (1..3999)."""
    if not 1 <= n <= 3999:
        raise ValueError(f"n must be an integer from 1 to 3999, got {n}")
    parts: list[str] = []
    for value, letters in _PAIRS:
        while n >= value:
            parts.append(letters)
            n -= value
    return "".join(parts)
