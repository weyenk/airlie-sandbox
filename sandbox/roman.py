"""Roman numeral conversion for 1..3999."""

_VALUES: tuple[tuple[int, str], ...] = (
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

_CHAR_VALUES: dict[str, int] = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1,
}


def to_roman(n: int) -> str:
    """Canonical subtractive roman numeral for 1..3999; ValueError otherwise."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise ValueError(f"to_roman expects an int, got {type(n).__name__}")
    if not 1 <= n <= 3999:
        raise ValueError(f"to_roman expects 1..3999, got {n}")
    parts: list[str] = []
    for value, numeral in _VALUES:
        while n >= value:
            parts.append(numeral)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Integer for a valid roman numeral string; ValueError on any malformed input."""
    if not isinstance(s, str) or s == "":
        raise ValueError(f"from_roman expects a non-empty str, got {s!r}")
    values = [_CHAR_VALUES.get(char) for char in s]
    if any(value is None for value in values):
        raise ValueError(f"from_roman got non-roman characters in {s!r}")
    n = 0
    for i, value in enumerate(values):
        if i + 1 < len(values) and value < values[i + 1]:
            n -= value
        else:
            n += value
    if not 1 <= n <= 3999 or to_roman(n) != s:
        raise ValueError(f"from_roman got malformed numeral {s!r}")
    return n
