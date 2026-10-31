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


def from_roman(s: str) -> int:
    """Integer value of a canonical Roman numeral 1..3999; ValueError otherwise."""
    if not s:
        raise ValueError(f"numeral must not be empty, got {s!r}")
    if any(ch not in "IVXLCDM" for ch in s):
        raise ValueError(f"numeral contains non-Roman characters: {s!r}")
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for i, ch in enumerate(s):
        v = values[ch]
        if i + 1 < len(s) and v < values[s[i + 1]]:
            total -= v
        else:
            total += v
    if total < 1 or total > 3999:
        raise ValueError(f"numeral value out of range 1..3999: {s!r}")
    if to_roman(total) != s:
        raise ValueError(f"numeral is not in canonical form: {s!r}")
    return total
