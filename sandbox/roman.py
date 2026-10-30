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
