"""Roman-numeral helpers for the airlie sandbox."""

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
    """Convert an integer 1..3999 to a standard subtractive Roman numeral."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise ValueError(f"expected an int, got {type(n).__name__}")
    if not 1 <= n <= 3999:
        raise ValueError(f"n must be in the range 1 to 3999, got {n}")
    out = []
    for value, letters in _TABLE:
        while n >= value:
            out.append(letters)
            n -= value
    return "".join(out)


def from_roman(s: str) -> int:
    """Parse a standard Roman numeral back to the integer 1..3999 it encodes."""
    if not isinstance(s, str):
        raise ValueError(f"expected a str, got {type(s).__name__}")
    for n in range(1, 4000):
        if to_roman(n) == s:
            return n
    raise ValueError(f"malformed Roman numeral: {s!r}")
