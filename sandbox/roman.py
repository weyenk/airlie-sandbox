"""Strictly validated Roman-numeral conversion for 1 to 3999."""

import re

_PAIRS = [
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

_PATTERN = re.compile(
    r"M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})"
)

_VALUES = {
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


def to_roman(n: int) -> str:
    """Return the standard uppercase Roman numeral for an int 1 to 3999."""
    if not isinstance(n, int) or not 1 <= n <= 3999:
        raise ValueError("n must be an int between 1 and 3999")
    parts: list[str] = []
    for value, numeral in _PAIRS:
        count, n = divmod(n, value)
        parts.append(numeral * min(count, 3))
    return "".join(parts)


def from_roman(s: str) -> int:
    """Return the int 1 to 3999 of a valid standard Roman numeral."""
    if not isinstance(s, str) or not s or _PATTERN.fullmatch(s) is None:
        raise ValueError("s must be a str between 1 and 3999")
    total = 0
    i = 0
    while i < len(s):
        if s[i : i + 2] in _VALUES:
            total += _VALUES[s[i : i + 2]]
            i += 2
        else:
            total += _VALUES[s[i]]
            i += 1
    return total
