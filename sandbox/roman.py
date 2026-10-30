"""Roman numeral helpers for the airlie sandbox."""


def to_roman(n: int) -> str:
    """Return the canonical Roman numeral for n (1..3999)."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise ValueError(f"n must be an int, got {type(n).__name__}")
    if not 1 <= n <= 3999:
        raise ValueError(f"n must be in 1..3999, got {n}")
    pairs = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
    ]
    parts = []
    for value, symbol in pairs:
        while n >= value:
            parts.append(symbol)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Return the integer for a canonical Roman numeral (inverse of to_roman)."""
    if not isinstance(s, str):
        raise ValueError(f"s must be a str, got {type(s).__name__}")
    if not s:
        raise ValueError("s must not be empty")
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if any(char not in values for char in s):
        raise ValueError(f"s contains characters outside IVXLCDM: {s!r}")
    total = 0
    for i, char in enumerate(s):
        value = values[char]
        if i + 1 < len(s) and values[s[i + 1]] > value:
            total -= value
        else:
            total += value
    if not 1 <= total <= 3999 or to_roman(total) != s:
        raise ValueError(f"s is not a canonical Roman numeral: {s!r}")
    return total
