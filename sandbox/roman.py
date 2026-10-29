"""Roman numerals for 1..3999."""

import re

_PAIRS = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
]

_CANONICAL = re.compile(r"M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})")

_VALUES = {
    "M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100,
    "XC": 90, "L": 50, "XL": 40, "X": 10,
    "IX": 9, "V": 5, "IV": 4, "I": 1,
}


def to_roman(n: int) -> str:
    """Return the canonical Roman numeral for n, 1..3999."""
    if type(n) is not int:
        raise ValueError(f"expected an int, got {type(n).__name__}")
    if not 1 <= n <= 3999:
        raise ValueError(f"{n} is outside 1..3999 (outside 1...3999)")
    parts = []
    for value, numeral in _PAIRS:
        while n >= value:
            parts.append(numeral)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Return the integer for a canonical Roman numeral, 1..3999."""
    if type(s) is not str:
        raise ValueError(f"expected a str, got {type(s).__name__}: malformed")
    if s == "" or _CANONICAL.fullmatch(s) is None:
        raise ValueError(f"{s!r} is not a canonical Roman numeral: malformed")
    total = 0
    rest = s
    while rest:
        for length in (2, 1):
            unit = rest[:length]
            if unit in _VALUES:
                total += _VALUES[unit]
                rest = rest[length:]
                break
        else:
            raise ValueError(f"{s!r} is not a canonical Roman numeral: malformed")
    return total
