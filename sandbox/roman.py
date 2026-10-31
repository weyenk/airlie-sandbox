"""Roman numerals for 1..3999 with strict validation."""

ALPHABET = "IVXLCDM"

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
    """Canonical subtractive Roman numeral for an int in 1..3999."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise ValueError(f"expected an int in 1..3999, got {type(n).__name__}")
    if not 1 <= n <= 3999:
        raise ValueError(f"expected an int in 1..3999, got {n}")
    parts = []
    for value, numeral in _TABLE:
        while n >= value:
            parts.append(numeral)
            n -= value
    return "".join(parts)


VALID_ROMANS = {to_roman(n) for n in range(1, 4000)}

_VALUES = {c: v for c, v in zip(ALPHABET, (1, 5, 10, 50, 100, 500, 1000))}


def from_roman(s: str) -> int:
    """Value of a canonical uppercase Roman numeral, or ValueError."""
    if not isinstance(s, str):
        raise ValueError(f"expected a str, got {type(s).__name__}")
    if s not in VALID_ROMANS:
        raise ValueError(f"not a valid Roman numeral: {s!r}")
    total = 0
    for i, c in enumerate(s):
        value = _VALUES[c]
        if i + 1 < len(s) and value < _VALUES[s[i + 1]]:
            total -= value
        else:
            total += value
    return total
