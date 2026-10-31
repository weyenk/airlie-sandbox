"""Roman numerals for 1..3999."""

_SUBTRACTIVE = (
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
    (4, "IV"),
    (1, "I"),
)


def to_roman(n: int) -> str:
    """Greedy standard subtractive numeral for 1..3999."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise ValueError("n must be an integer")
    if n < 1 or n > 3999:
        raise ValueError("n must be in 1..3999")
    parts = []
    for value, numeral in _SUBTRACTIVE:
        while n >= value:
            parts.append(numeral)
            n -= value
    return "".join(parts)


_VALID = {to_roman(n): n for n in range(1, 4000)}


def from_roman(s: str) -> int:
    """Parse a standard subtractive numeral back to its integer."""
    if not isinstance(s, str):
        raise ValueError("s must be a string")
    if s == "":
        raise ValueError("s must not be empty")
    if s not in _VALID:
        raise ValueError("invalid numeral: " + repr(s))
    return _VALID[s]
