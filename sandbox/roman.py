"""Round-trip conversion between integers 1-3999 and Roman numerals."""

_MESSAGE = "not a valid Roman numeral"

_VALUES = (
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

_CHAR_VALUES = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}


def to_roman(n: int) -> str:
    """Return the standard subtractive Roman numeral for an integer 1-3999."""
    if type(n) is not int or not 1 <= n <= 3999:
        raise ValueError(_MESSAGE)
    parts = []
    for value, numeral in _VALUES:
        parts.append(numeral * (n // value))
        n %= value
    return "".join(parts)


def from_roman(s: str) -> int:
    """Return the integer 1-3999 that a standard Roman numeral spells."""
    if type(s) is not str or not 1 <= len(s) <= 15:
        raise ValueError(_MESSAGE)
    if not set(s) <= set(_CHAR_VALUES):
        raise ValueError(_MESSAGE)
    total = 0
    i = 0
    while i < len(s):
        chosen = None
        for value, numeral in _VALUES:
            if s.startswith(numeral, i):
                chosen = (value, len(numeral))
                break
        if chosen is None:
            raise ValueError(_MESSAGE)
        total += chosen[0]
        i += chosen[1]
    if not 1 <= total <= 3999 or to_roman(total) != s:
        raise ValueError(_MESSAGE)
    return total
