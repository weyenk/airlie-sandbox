"""Roman numeral conversion for 1 to 3999."""

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

_LETTERS = set("IVXLCDM")


def to_roman(n: int) -> str:
    """Return the Roman numeral for an int in 1 to 3999."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise ValueError(f"{n!r} is not an int")
    if not 1 <= n <= 3999:
        raise ValueError(f"{n} is outside 1 to 3999")
    parts = []
    for value, numeral in _TABLE:
        while n >= value:
            parts.append(numeral)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Return the int for a canonical uppercase Roman numeral in 1 to 3999."""
    if not isinstance(s, str) or not s or any(c not in _LETTERS for c in s):
        raise ValueError(f"{s!r} is not a Roman numeral")
    value = 0
    rest = s
    while rest:
        for v, numeral in _TABLE:
            if rest.startswith(numeral):
                value += v
                rest = rest[len(numeral):]
                break
        else:
            raise ValueError(f"{s!r} is not a Roman numeral")
    if not 1 <= value <= 3999:
        raise ValueError(f"{value} is outside 1 to 3999")
    if to_roman(value) != s:
        raise ValueError(f"{s!r} is not a Roman numeral")
    return value
