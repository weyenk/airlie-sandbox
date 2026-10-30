"""Roman-numeral conversion for 1 to 3999."""

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
    """Return the standard subtractive Roman numeral for n, 1 <= n <= 3999."""
    if not 1 <= n <= 3999:
        raise ValueError("n must be an integer between 1 and 3999")
    parts = []
    for value, letters in _TABLE:
        while n >= value:
            parts.append(letters)
            n -= value
    return "".join(parts)


_CANONICAL = {to_roman(n): n for n in range(1, 4000)}


def from_roman(s: str) -> int:
    """Return the integer for a canonical Roman numeral, or raise ValueError."""
    if s not in _CANONICAL:
        raise ValueError("not a valid Roman numeral")
    return _CANONICAL[s]
