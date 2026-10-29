"""Canonical Roman numerals for integers 1 to 3999."""

_TABLE = (
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
    """Return the canonical Roman numeral for n, raising ValueError outside 1..3999."""
    if n < 1 or n > 3999:
        raise ValueError(f"n must be between 1 and 3999, got {n}")
    parts = []
    for value, letters in _TABLE:
        parts.append(letters * (n // value))
        n %= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Return the unique n in 1..3999 with to_roman(n) == s, raising ValueError otherwise."""
    if not isinstance(s, str):
        raise ValueError(f"expected a str, got {type(s).__name__}")
    if s == "":
        raise ValueError("expected a non-empty Roman numeral")
    inverse = {to_roman(n): n for n in range(1, 4000)}
    if s not in inverse:
        raise ValueError(f"{s!r} is not a canonical Roman numeral for 1..3999")
    return inverse[s]
