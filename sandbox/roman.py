"""Roman numeral conversion for 1..3999."""

from __future__ import annotations

_REFUSAL = "not a valid Roman numeral"

_PAIRS = (
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
)

def to_roman(n: int) -> str:
    """Convert an integer 1..3999 to its standard Roman numeral."""
    if type(n) is not int or n < 1 or n > 3999:
        raise ValueError(f"{n!r} is {_REFUSAL}")
    parts = []
    for value, letters in _PAIRS:
        while n >= value:
            parts.append(letters)
            n -= value
    return "".join(parts)


_VALID = {to_roman(n): n for n in range(1, 4000)}


def from_roman(s: str) -> int:
    """Parse a standard Roman numeral 1..3999 back to its integer."""
    if type(s) is not str or s not in _VALID:
        raise ValueError(f"{s!r} is {_REFUSAL}")
    return _VALID[s]
