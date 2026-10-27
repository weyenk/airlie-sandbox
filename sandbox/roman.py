"""Roman numeral helpers for 1 to 3999."""

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

_PATTERN = re.compile(r"M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})")


def to_roman(n: int) -> str:
    """Return the canonical uppercase Roman numeral for n (1-3999)."""
    if isinstance(n, bool) or not isinstance(n, int) or not 1 <= n <= 3999:
        raise ValueError("n must be an integer between 1 and 3999")
    parts = []
    for value, numeral in _TABLE:
        while n >= value:
            parts.append(numeral)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Parse a canonical uppercase Roman numeral (1-3999) to an integer."""
    if not isinstance(s, str) or s == "":
        raise ValueError("not a valid Roman numeral")
    if not _PATTERN.fullmatch(s):
        raise ValueError("not a valid Roman numeral")
    values = {numeral: value for value, numeral in _TABLE}
    total = 0
    for text in ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"):
        while s.startswith(text):
            total += values[text]
            s = s[len(text):]
    if not 1 <= total <= 3999:
        raise ValueError("not a valid Roman numeral")
    return total
