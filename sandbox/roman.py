"""Roman numeral conversion for the 1..3999 range."""

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


def to_roman(n: int) -> str:
    """Return the canonical Roman numeral for n (1..3999)."""
    if type(n) is not int:
        raise ValueError("n must be an int between 1 and 3999")
    if not 1 <= n <= 3999:
        raise ValueError("n must be between 1 and 3999")
    result = ""
    for value, letters in _TABLE:
        while n >= value:
            result += letters
            n -= value
    return result


_CANONICAL = re.compile(
    r"^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
)

_TOKEN_VALUES = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
}


def from_roman(s: str) -> int:
    """Return the integer value of a canonical uppercase Roman numeral (1..3999)."""
    if type(s) is not str:
        raise ValueError("not a valid Roman numeral")
    match = _CANONICAL.fullmatch(s)
    if match is None or s == "":
        raise ValueError("not a valid Roman numeral")
    total = 0
    for group in match.groups():
        if not group:
            continue
        if len(group) == 2 and group in _TOKEN_VALUES:
            total += _TOKEN_VALUES[group]
        else:
            for ch in group:
                total += _TOKEN_VALUES[ch]
    return total
