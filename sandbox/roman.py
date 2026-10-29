"""Convert integers to Roman numerals for 0..3999."""

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
    """Return the canonical Roman numeral for n (0..3999), or '' for 0."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise ValueError(f"{n!r} is not an int")
    if n < 0 or n > 3999:
        raise ValueError(f"{n} is outside the range 0..3999")
    if n == 0:
        return ""
    parts = []
    for value, letters in _TABLE:
        count, n = divmod(n, value)
        parts.append(letters * count)
    return "".join(parts)
