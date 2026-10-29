"""Classical Roman-numeral conversion for the range 1 to 3999."""

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
    """Return the classical Roman numeral for 1 <= n <= 3999."""
    if n < 1 or n > 3999:
        raise ValueError(f"n must be between 1 and 3999, got {n}")
    parts = []
    for value, symbol in _TABLE:
        while n >= value:
            parts.append(symbol)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Return the integer value of a well-formed Roman numeral, 1 to 3999."""
    if not s or any(ch not in "IVXLCDM" for ch in s):
        raise ValueError(f"not a Roman numeral: {s!r}")
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if s.count("V") > 1 or s.count("L") > 1 or s.count("D") > 1:
        raise ValueError(f"V, L and D may appear at most once: {s!r}")
    if any(s[i] == s[i + 1] == s[i + 2] == s[i + 3] for i in range(len(s) - 3)):
        raise ValueError(f"a symbol may not repeat more than three times: {s!r}")
    total = 0
    for i, ch in enumerate(s):
        v = values[ch]
        if i + 1 < len(s) and v < values[s[i + 1]]:
            if ch in ("V", "L", "D"):
                raise ValueError(f"V, L and D cannot be subtractive: {s!r}")
            if ch == "I" and s[i + 1] not in ("V", "X"):
                raise ValueError(f"I may only subtract from V or X: {s!r}")
            if ch == "X" and s[i + 1] not in ("L", "C"):
                raise ValueError(f"X may only subtract from L or C: {s!r}")
            if ch == "C" and s[i + 1] not in ("D", "M"):
                raise ValueError(f"C may only subtract from D or M: {s!r}")
            total -= v
        else:
            total += v
    if total < 1 or total > 3999:
        raise ValueError(f"value out of range 1..3999: {s!r}")
    return total
