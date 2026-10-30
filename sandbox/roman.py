"""Convert integers 1 to 3999 to Roman numerals and back."""

ALPHABET = "IVXLCDM"

_TABLE: tuple[tuple[int, str], ...] = (
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


def to_roman(n: int) -> str:
    """Return the canonical Roman numeral for an integer 1 to 3999."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"expected an int, got {type(n).__name__}")
    if not 1 <= n <= 3999:
        raise ValueError(f"n must be an integer from 1 to 3999, got {n}")
    parts: list[str] = []
    for value, numeral in _TABLE:
        while n >= value:
            parts.append(numeral)
            n -= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Return the integer a canonical Roman numeral 1 to 3999 stands for."""
    if not s or any(ch not in ALPHABET for ch in s) or s not in _CANONICAL:
        raise ValueError(f"malformed Roman numeral: {s!r}")
    return _CANONICAL[s]


_CANONICAL: dict[str, int] = {to_roman(n): n for n in range(1, 4000)}
