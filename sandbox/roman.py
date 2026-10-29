"""Integer-to-Roman and Roman-to-integer conversion for 1..3999."""

_ROMAN_VALUES = [
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
    """Convert an integer 1..3999 to its uppercase Roman numeral."""
    if type(n) is not int or not 1 <= n <= 3999:
        raise ValueError(f"{n!r} is out of range: expected an integer 1..3999")
    parts = []
    for value, numeral in _ROMAN_VALUES:
        while n >= value:
            parts.append(numeral)
            n -= value
    return "".join(parts)


_ROMAN_TO_INT = {to_roman(n): n for n in range(1, 4000)}


def from_roman(s: str) -> int:
    """Parse an uppercase Roman numeral produced by to_roman back to its integer."""
    if s not in _ROMAN_TO_INT:
        raise ValueError(f"{s!r} is malformed: not a valid Roman numeral")
    return _ROMAN_TO_INT[s]
