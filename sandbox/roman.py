"""Roman numeral codec for 1 to 3999."""

def to_roman(n: int) -> str:
    """Render 1..3999 as a standard subtractive uppercase Roman numeral."""
    if n < 1 or n > 3999:
        raise ValueError(f"n must be an integer from 1 to 3999, got {n!r}")
    table = [
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
    parts = []
    for value, numeral in table:
        while n >= value:
            parts.append(numeral)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Parse a standard subtractive uppercase Roman numeral back to 1..3999."""
    if not isinstance(s, str) or len(s) > 15 or any(c not in "IVXLCDM" for c in s):
        raise ValueError(f"not a Roman numeral: {s!r}")
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for i, c in enumerate(s):
        v = values[c]
        if i + 1 < len(s) and values[s[i + 1]] > v:
            total -= v
        else:
            total += v
    if to_roman(total) != s:
        raise ValueError(f"not a canonical Roman numeral: {s!r}")
    return total
