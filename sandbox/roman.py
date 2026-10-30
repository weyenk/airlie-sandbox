"""Roman numeral conversion for integers 1..3999."""

_TABLE = (
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
    """Convert an integer 1..3999 to its canonical Roman numeral."""
    if type(n) is not int:
        raise ValueError(f"expected an int, got {type(n).__name__}")
    if not 1 <= n <= 3999:
        raise ValueError(f"n must be in 1..3999, got {n}")
    parts = []
    for value, numeral in _TABLE:
        while n >= value:
            parts.append(numeral)
            n -= value
    return "".join(parts)


_ROMAN_TO_INT = {to_roman(n): n for n in range(1, 4000)}


def from_roman(s: str) -> int:
    """Convert a canonical Roman numeral to the integer 1..3999 it encodes."""
    try:
        return _ROMAN_TO_INT[s]
    except KeyError:
        raise ValueError(f"not a valid Roman numeral for 1..3999: {s!r}") from None
