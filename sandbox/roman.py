"""Convert integers 1..3999 to canonical Roman numerals."""

_TABLE: tuple[tuple[int, str], ...] = (
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
    """Return the canonical uppercase Roman numeral for n (1..3999)."""
    if n < 1 or n > 3999:
        raise ValueError(f"n must be between 1 and 3999, got {n}")
    parts: list[str] = []
    for value, letter in _TABLE:
        while n >= value:
            parts.append(letter)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Return the integer 1..3999 whose canonical numeral is s, else raise ValueError."""
    if not isinstance(s, str):
        raise ValueError(f"expected a str, got {type(s).__name__}")
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    parsed = 0
    for i, ch in enumerate(s):
        if ch not in values:
            raise ValueError(f"invalid character {ch!r} in {s!r}")
        v = values[ch]
        if i + 1 < len(s) and v < values[s[i + 1]]:
            parsed -= v
        else:
            parsed += v
    if not 1 <= parsed <= 3999 or to_roman(parsed) != s:
        raise ValueError(f"{s!r} is not a canonical Roman numeral for 1..3999")
    return parsed
