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


def to_roman(n: int) -> str:
    """Convert an integer 1..3999 to its canonical uppercase Roman numeral."""
    parts = []
    for symbol, value in _TABLE:
        while n >= value:
            parts.append(symbol)
            n -= value
    return "".join(parts)
