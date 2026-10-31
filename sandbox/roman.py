"""Convert integers 1..3999 to standard Roman numerals and back."""

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

_VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def to_roman(n: int) -> str:
    """Standard subtractive Roman numeral of n in 1..3999."""
    if not (isinstance(n, int) and not isinstance(n, bool)):
        raise ValueError("n must be an integer")
    if not 1 <= n <= 3999:
        raise ValueError("n must be in 1..3999")
    parts = []
    for value, symbol in _TABLE:
        while n >= value:
            parts.append(symbol)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Standard subtractive evaluation of a Roman numeral string."""
    if not isinstance(s, str):
        raise ValueError("input must be a string")
    if not s:
        raise ValueError("empty string")
    for ch in s:
        if ch not in _VALUES:
            raise ValueError("malformed numeral")
    total = 0
    for i, ch in enumerate(s):
        value = _VALUES[ch]
        if i + 1 < len(s) and value < _VALUES[s[i + 1]]:
            total -= value
        else:
            total += value
    if not 1 <= total <= 3999:
        raise ValueError("malformed numeral")
    return total
