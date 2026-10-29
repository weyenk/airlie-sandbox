"""Roman numerals for 1 to 3999."""

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

_PAT = re.compile(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")


def to_roman(n: int) -> str:
    """Standard Roman numeral for 1..3999; ValueError otherwise."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise ValueError(f"expected an int, got {type(n).__name__}")
    if not 1 <= n <= 3999:
        raise ValueError(f"n must be in the range 1 to 3999, got {n}")
    out = ""
    for value, numeral in _TABLE:
        while n >= value:
            out += numeral
            n -= value
    return out


def from_roman(s: str) -> int:
    """Inverse of to_roman; ValueError on non-str, empty or malformed input."""
    if not isinstance(s, str):
        raise ValueError(f"expected a str, got {type(s).__name__}")
    if not s:
        raise ValueError("expected a non-empty str")
    if not _PAT.match(s):
        raise ValueError(f"malformed Roman numeral: {s!r}")
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for i, ch in enumerate(s):
        value = values[ch]
        if i + 1 < len(s) and values[s[i + 1]] > value:
            total -= value
        else:
            total += value
    return total
