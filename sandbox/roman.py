"""Convert integers to Roman numerals and back, for the 1..3999 range."""

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

_LETTERS = frozenset("IVXLCDM")


def to_roman(n: int) -> str:
    """Return the standard subtractive Roman numeral for 1 <= n <= 3999."""
    if not 1 <= n <= 3999:
        raise ValueError(f"n must be in 1..3999, got {n}")
    parts = []
    for value, numeral in _PAIRS:
        while n >= value:
            parts.append(numeral)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Return the unique n in 1..3999 whose to_roman(n) is s."""
    if not s:
        raise ValueError("s must not be empty")
    if any(ch not in _LETTERS for ch in s):
        raise ValueError(f"s contains invalid characters: {s!r}")
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for i, ch in enumerate(s):
        value = values[ch]
        if i + 1 < len(s) and value < values[s[i + 1]]:
            total -= value
        else:
            total += value
    if not 1 <= total <= 3999 or to_roman(total) != s:
        raise ValueError(f"s is not a canonical Roman numeral: {s!r}")
    return total
