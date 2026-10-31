"""Canonical Roman numeral conversion for 1 to 3999."""

_VALUES = [
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
    """Return the canonical subtractive Roman numeral for n (1 to 3999)."""
    if not (isinstance(n, int) and not isinstance(n, bool)) or not 1 <= n <= 3999:
        raise ValueError("n must be an integer from 1 to 3999, got " + repr(n))
    parts = []
    for value, numeral in _VALUES:
        while n >= value:
            parts.append(numeral)
            n -= value
    return "".join(parts)


ROMAN_VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
ROMAN_SUBTRACTIVE = {
    ("I", "V"): 4,
    ("I", "X"): 9,
    ("X", "L"): 40,
    ("X", "C"): 90,
    ("C", "D"): 400,
    ("C", "M"): 900,
}
ROMAN_MAX_REPEAT = {"I": 3, "X": 3, "C": 3, "M": 3, "V": 1, "L": 1, "D": 1}


def from_roman(s: str) -> int:
    """Return the integer value of a canonical Roman numeral (1 to 3999)."""
    if not isinstance(s, str):
        raise ValueError("s must be a valid Roman numeral, got " + repr(s))
    total = 0
    previous = None
    previous_letter = None
    run = 0
    i = 0
    while i < len(s):
        letter = s[i]
        if letter not in ROMAN_VALUES:
            raise ValueError("s must be a valid Roman numeral, got " + repr(s))
        if i + 1 < len(s) and (letter, s[i + 1]) in ROMAN_SUBTRACTIVE:
            value = ROMAN_SUBTRACTIVE[(letter, s[i + 1])]
            i += 2
        else:
            value = ROMAN_VALUES[letter]
            i += 1
        if previous is not None and value > previous:
            raise ValueError("s must be a valid Roman numeral, got " + repr(s))
        run = run + 1 if letter == previous_letter else 1
        if run > ROMAN_MAX_REPEAT[letter]:
            raise ValueError("s must be a valid Roman numeral, got " + repr(s))
        previous = value
        previous_letter = letter
        total += value
    if not 1 <= total <= 3999:
        raise ValueError("s must be a valid Roman numeral, got " + repr(s))
    if to_roman(total) != s:
        raise ValueError("s must be a valid Roman numeral, got " + repr(s))
    return total
