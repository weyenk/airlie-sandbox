"""Roman numeral conversion for the airlie sandbox."""

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
    """Canonical Roman numeral of n for 1..3999; ValueError outside that range."""
    if n < 1 or n > 3999:
        raise ValueError(f"n must be between 1 and 3999, got {n}")
    parts = []
    for value, numeral in _TABLE:
        while n >= value:
            parts.append(numeral)
            n -= value
    return "".join(parts)
