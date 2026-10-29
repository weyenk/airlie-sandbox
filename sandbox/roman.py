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


_NUMERAL_TO_VALUE = {to_roman(n): n for n in range(0, 4000)}


def from_roman(s: str) -> int:
    """Return the integer whose Roman numeral is s, or 0 for ''."""
    if not isinstance(s, str):
        raise ValueError(f"{s!r} is not a str")
    try:
        return _NUMERAL_TO_VALUE[s]
    except KeyError:
        raise ValueError(f"{s!r} is a malformed numeral") from None
