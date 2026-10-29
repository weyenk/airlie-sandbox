"""Roman numeral conversion for 1 to 3999."""

import re

_CANONICAL = re.compile(r"M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})")

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
    """Canonical uppercase Roman numeral for 1..3999; ValueError otherwise."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise ValueError(f"n must be an int in 1 to 3999, got {type(n).__name__}")
    if not 1 <= n <= 3999:
        raise ValueError(f"n must be in 1 to 3999, got {n}")
    parts = []
    for value, numeral in _TABLE:
        while n >= value:
            parts.append(numeral)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Integer for a canonical uppercase Roman numeral of 1..3999; ValueError otherwise."""
    if not isinstance(s, str):
        raise ValueError(f"s must be a str, got {type(s).__name__}")
    match = _CANONICAL.fullmatch(s)
    if match is None:
        raise ValueError(f"s must be a canonical Roman numeral of 1 to 3999, got {s!r}")
    thousands = len(s) - len(s.lstrip("M"))
    hundreds, tens, ones = match.groups()
    value = (
        thousands * 1000
        + {"": 0, "C": 100, "CC": 200, "CCC": 300, "CD": 400, "D": 500, "DC": 600,
           "DCC": 700, "DCCC": 800, "CM": 900}[hundreds]
        + {"": 0, "X": 10, "XX": 20, "XXX": 30, "XL": 40, "L": 50, "LX": 60,
           "LXX": 70, "LXXX": 80, "XC": 90}[tens]
        + {"": 0, "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6,
           "VII": 7, "VIII": 8, "IX": 9}[ones]
    )
    if not 1 <= value <= 3999:
        raise ValueError(f"s must be a canonical Roman numeral of 1 to 3999, got {s!r}")
    return value
