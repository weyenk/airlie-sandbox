"""Standard-library Roman numeral conversion for the airlie sandbox."""

_TABLE = (
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1),
)


_INVALID = "not a valid Roman numeral"


def to_roman(n: int) -> str:
    """Convert an integer 1..3999 to its canonical uppercase Roman numeral."""
    if isinstance(n, bool) or not isinstance(n, int) or not 1 <= n <= 3999:
        raise ValueError(f"{n!r} is {_INVALID}")
    parts = []
    for symbol, value in _TABLE:
        while n >= value:
            parts.append(symbol)
            n -= value
    return "".join(parts)
