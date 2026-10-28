"""Roman numeral conversion for the 1..3999 range."""

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
    """Return the canonical Roman numeral for n (1..3999)."""
    if type(n) is not int:
        raise ValueError("n must be an int between 1 and 3999")
    if not 1 <= n <= 3999:
        raise ValueError("n must be between 1 and 3999")
    result = ""
    for value, letters in _TABLE:
        while n >= value:
            result += letters
            n -= value
    return result
