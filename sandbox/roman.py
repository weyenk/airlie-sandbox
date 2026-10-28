"""Roman numeral conversion for 1 to 3999."""

import re

# Greedy value table, largest first.
_VALUE_TABLE = [
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

# Canonical Roman numeral form: 0-3 M's, then hundreds, tens, ones.
_CANONICAL = re.compile(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")

_LETTER_VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def to_roman(n: int) -> str:
    """Return the canonical Roman numeral for n (1 to 3999)."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise ValueError(f"expected an int, got {type(n).__name__}")
    if n < 1 or n > 3999:
        raise ValueError(f"n must be in the range 1 to 3999, got {n}")
    numeral = ""
    for value, letters in _VALUE_TABLE:
        while n >= value:
            numeral += letters
            n -= value
    return numeral


def from_roman(s: str) -> int:
    """Parse a canonical Roman numeral (1 to 3999) into an int."""
    if not isinstance(s, str):
        raise ValueError(f"expected a str, got {type(s).__name__}")
    if s == "":
        raise ValueError("malformed Roman numeral: empty string")
    value = 0
    for i, letter in enumerate(s):
        if letter not in _LETTER_VALUES:
            raise ValueError(f"malformed Roman numeral: unknown letter {letter!r}")
        current = _LETTER_VALUES[letter]
        if i + 1 < len(s) and current < _LETTER_VALUES[s[i + 1]]:
            value -= current
        else:
            value += current
    if value < 1 or value > 3999:
        raise ValueError(f"Roman numeral out of range 1 to 3999: {s!r}")
    if not _CANONICAL.match(s):
        raise ValueError(f"malformed Roman numeral: {s!r} is not canonical")
    return value
