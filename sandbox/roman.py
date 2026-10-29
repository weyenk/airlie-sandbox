"""Roman numeral conversion for integers 1 to 3999."""

import re

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

_LETTERS = set("MDCLXVI")
_PATTERN = re.compile(r"M{0,4}(CM|CD|C{0,3})?(XL|XC|L|X{1,3})?(IX|IV|V?I{0,3})?")
_VALUES = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}


def to_roman(n: int) -> str:
    """Return the standard Roman numeral for an integer from 1 to 3999."""
    if not isinstance(n, int):
        raise TypeError(f"to_roman expects an integer, got {type(n).__name__}")
    if not 1 <= n <= 3999:
        raise ValueError(f"to_roman expects an integer from 1 to 3999, got {n}")
    parts = []
    for value, letters in _TABLE:
        while n >= value:
            parts.append(letters)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Return the integer a valid Roman numeral for 1 to 3999 represents."""
    if not isinstance(s, str):
        raise TypeError(f"from_roman expects a string, got {type(s).__name__}")
    if s == "" or any(c not in _LETTERS for c in s) or _PATTERN.fullmatch(s) is None:
        raise ValueError(f"malformed Roman numeral: '{s}'")
    values = [_VALUES[c] for c in s]
    value = 0
    for i, v in enumerate(values):
        if i + 1 < len(values) and v < values[i + 1]:
            value -= v
        else:
            value += v
    if not 1 <= value <= 3999:
        raise ValueError(f"Roman numeral out of range 1 to 3999: '{s}'")
    return value
