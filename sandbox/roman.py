"""Roman numerals: to_roman and from_roman over 1..3999."""

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
    """Canonical Roman numeral for 1..3999; ValueError 'out of range' otherwise."""
    if not isinstance(n, int) or not 1 <= n <= 3999:
        raise ValueError(f"{n!r} is out of range (1..3999)")
    parts: list[str] = []
    for value, letters in _PAIRS:
        while n >= value:
            parts.append(letters)
            n -= value
    return "".join(parts)


_VALID: dict[str, int] = {to_roman(n): n for n in range(1, 4000)}


def from_roman(s: str) -> int:
    """Inverse of to_roman; ValueError 'not a valid Roman numeral' for anything else."""
    if not isinstance(s, str) or s not in _VALID:
        raise ValueError(f"{s!r} is not a valid Roman numeral")
    return _VALID[s]
