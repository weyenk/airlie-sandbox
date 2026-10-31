"""Standard Roman numerals over 1..3999."""

import re

_CANONICAL = re.compile(r"(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})")

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
    """Standard Roman numeral for 1..3999; ValueError otherwise."""
    if type(n) is not int or n < 1 or n > 3999:
        raise ValueError(f"n must be an int in 1..3999, got {n!r}")
    out = []
    for value, letters in _TABLE:
        while n >= value:
            out.append(letters)
            n -= value
    return "".join(out)


def from_roman(s: str) -> int:
    """Inverse of to_roman; ValueError on non-str or non-canonical input."""
    if type(s) is not str:
        raise ValueError(f"expected a str, got {type(s).__name__}")
    if not s:
        raise ValueError("expected a non-empty Roman numeral")
    match = _CANONICAL.fullmatch(s)
    if match is None:
        raise ValueError(f"not a canonical Roman numeral: {s!r}")
    thousands, hundreds, tens, ones = match.groups()
    return len(thousands) * 1000 + _hundreds(hundreds) + _tens(tens) + _ones(ones)


def _hundreds(h: str) -> int:
    """Value of the hundreds group."""
    if h == "CM":
        return 900
    if h == "CD":
        return 400
    return (1 if "D" in h else 0) * 500 + h.count("C") * 100


def _tens(t: str) -> int:
    """Value of the tens group."""
    if t == "XC":
        return 90
    if t == "XL":
        return 40
    return (1 if "L" in t else 0) * 50 + t.count("X") * 10


def _ones(o: str) -> int:
    """Value of the ones group."""
    if o == "IX":
        return 9
    if o == "IV":
        return 4
    return (1 if "V" in o else 0) * 5 + o.count("I")
