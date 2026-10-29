"""Roman numerals for 1 to 3999."""


def to_roman(n: int) -> str:
    """Return the canonical uppercase subtractive numeral for n (1..3999)."""
    if type(n) is not int:
        raise ValueError(f"expected an int, got {type(n).__name__}")
    if n < 1 or n > 3999:
        raise ValueError(f"n must be between 1 and 3999, got {n}")
    pairs = ((1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
             (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
             (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"))
    out = []
    for value, letters in pairs:
        while n >= value:
            out.append(letters)
            n -= value
    return "".join(out)


def from_roman(s: str) -> int:
    """Return the integer for a canonical numeral; ValueError for any other string."""
    table = {to_roman(n): n for n in range(1, 4000)}
    try:
        return table[s]
    except KeyError:
        raise ValueError(f"not a valid Roman numeral: {s!r}")
