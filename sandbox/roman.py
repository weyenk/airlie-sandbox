"""Roman numeral conversion for integers 1 to 3999."""

SYMBOLS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

PAIRS = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

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
    """Convert an integer 1..3999 to a canonical uppercase Roman numeral."""
    if not isinstance(n, int) or not 1 <= n <= 3999:
        raise ValueError("n must be an integer from 1 to 3999")
    parts = []
    for value, symbol in _TABLE:
        while n >= value:
            parts.append(symbol)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Decode a well-formed uppercase Roman numeral to an integer 1..3999."""
    if not s:
        raise ValueError("malformed Roman numeral")
    if any(ch not in SYMBOLS for ch in s):
        raise ValueError("malformed Roman numeral")
    if any(ch * 4 in s for ch in "IXCM"):
        raise ValueError("malformed Roman numeral")
    if any(s.count(ch) > 1 for ch in "VLD"):
        raise ValueError("malformed Roman numeral")
    for a, b in zip(s, s[1:]):
        if SYMBOLS[a] < SYMBOLS[b] and a + b not in PAIRS:
            raise ValueError("malformed Roman numeral")
    total = 0
    for i, ch in enumerate(s):
        value = SYMBOLS[ch]
        if i + 1 < len(s) and value < SYMBOLS[s[i + 1]]:
            total -= value
        else:
            total += value
    if not 1 <= total <= 3999:
        raise ValueError("malformed Roman numeral")
    return total
