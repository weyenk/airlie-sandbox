"""Roman numeral conversion between integers 1..3999 and standard Roman numerals."""

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
    """Canonical Roman numeral for n in 1..3999; ValueError otherwise."""
    if isinstance(n, bool) or not isinstance(n, int) or not 1 <= n <= 3999:
        raise ValueError(f"n must be an integer in 1..3999, got {n!r}")
    parts = []
    for value, symbol in _TABLE:
        while n >= value:
            parts.append(symbol)
            n -= value
    return "".join(parts)


_VALID = {to_roman(n): n for n in range(1, 4000)}


def from_roman(s: str) -> int:
    """Integer for a standard Roman numeral; ValueError if s is not one of the 3999 valid outputs."""
    if not isinstance(s, str):
        raise ValueError(f"s must be a string, got {type(s).__name__}")
    if s not in _VALID:
        raise ValueError(f"not a valid Roman numeral: {s!r}")
    return _VALID[s]
