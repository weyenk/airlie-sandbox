"""Convert between integers 1..3999 and standard Roman numerals."""

import itertools

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

_PLACES: tuple[tuple[str, ...], ...] = (
    ("", "M", "MM", "MMM"),
    ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"),
    ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"),
    ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"),
)

_VALUES: dict[str, int] = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def to_roman(n: int) -> str:
    """Return the standard Roman numeral for n (1..3999); raise ValueError otherwise."""
    if not isinstance(n, int) or isinstance(n, bool) or not 1 <= n <= 3999:
        raise ValueError(f"n must be an integer in 1..3999, got {n!r}")
    parts: list[str] = []
    for value, symbol in _TABLE:
        count, n = divmod(n, value)
        parts.append(symbol * count)
    return "".join(parts)


def from_roman(s: str) -> int:
    """Return the integer for a canonical Roman numeral; raise ValueError otherwise."""
    if not isinstance(s, str) or s == "":
        raise ValueError(f"s must be a non-empty string, got {s!r}")
    if any(ch not in _VALUES for ch in s):
        raise ValueError(f"s contains symbols outside IVXLCDM: {s!r}")
    if not _is_canonical(s):
        raise ValueError(f"s is not a canonical Roman numeral: {s!r}")
    value = _evaluate(s)
    if not 1 <= value <= 3999:
        raise ValueError(f"s evaluates outside 1..3999: {s!r}")
    return value


def _is_canonical(s: str) -> bool:
    """Return True if s is built from the per-place canonical pieces in order."""
    for thousands, hundreds, tens, ones in itertools.product(*_PLACES):
        if thousands + hundreds + tens + ones == s:
            return True
    return False


def _evaluate(s: str) -> int:
    """Return the value of s, subtracting a symbol worth less than the one after it."""
    total = 0
    for i, ch in enumerate(s):
        value = _VALUES[ch]
        if i + 1 < len(s) and value < _VALUES[s[i + 1]]:
            total -= value
        else:
            total += value
    return total


if __name__ == "__main__":
    print(to_roman(1994), from_roman("MCMXCIV"))
