"""Roman numeral conversion for 1 to 3999."""

import re

# Descending value/symbol pairs used by to_roman.
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

# Anchored pattern for a canonical Roman numeral.
_PATTERN = re.compile(
    r"^M*(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
)

_HUNDREDS = {
    "": 0, "C": 100, "CC": 200, "CCC": 300,
    "CD": 400, "D": 500, "DC": 600, "DCC": 700,
    "DCCC": 800, "CM": 900,
}

_TENS = {
    "": 0, "X": 10, "XX": 20, "XXX": 30,
    "XL": 40, "L": 50, "LX": 60, "LXX": 70,
    "LXXX": 80, "XC": 90,
}

_ONES = {
    "": 0, "I": 1, "II": 2, "III": 3,
    "IV": 4, "V": 5, "VI": 6, "VII": 7,
    "VIII": 8, "IX": 9,
}


def to_roman(n: int) -> str:
    """Return the canonical Roman numeral for n (1 to 3999)."""
    if not 1 <= n <= 3999:
        raise ValueError(f"{n} is not between 1 and 3999")
    out = []
    for value, symbol in _TABLE:
        while n >= value:
            out.append(symbol)
            n -= value
    return "".join(out)


def from_roman(s: str) -> int:
    """Return the integer for a canonical uppercase Roman numeral."""
    if s == "":
        raise ValueError(f"malformed Roman numeral: {s!r}")
    m = _PATTERN.match(s)
    if m is None:
        raise ValueError(f"malformed Roman numeral: {s!r}")
    hundreds, tens, ones = m.groups()
    thousands = len(m.group(0)) - len(hundreds) - len(tens) - len(ones)
    value = thousands * 1000 + _HUNDREDS[hundreds] + _TENS[tens] + _ONES[ones]
    if not 1 <= value <= 3999:
        raise ValueError(f"{s!r} is not between 1 and 3999")
    return value
