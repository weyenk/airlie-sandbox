"""Roman-numeral conversion for the sandbox: to_roman and from_roman for 1..3999."""

# Canonical value table in descending order.
_TABLE: list[tuple[int, str]] = [
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

# Subtractive pairs, longest first.
_PAIRS: dict[str, int] = {"CM": 900, "CD": 400, "XC": 90, "XL": 40, "IX": 9, "IV": 4}

# Single-letter place values.
_LETTERS: dict[str, int] = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}


def to_roman(n: int) -> str:
    """Return the canonical Roman numeral for n (1..3999)."""
    if not 1 <= n <= 3999:
        raise ValueError("n must be between 1 and 3999")
    parts: list[str] = []
    for value, numeral in _TABLE:
        while n >= value:
            parts.append(numeral)
            n -= value
    return "".join(parts)


def _check_form(s: str) -> None:
    """Raise ValueError('malformed Roman numeral') if s is not a well-formed numeral."""
    if not s:
        raise ValueError("malformed Roman numeral")
    if any(ch not in _LETTERS for ch in s):
        raise ValueError("malformed Roman numeral")
    for letter, max_run in (("I", 3), ("X", 3), ("C", 3), ("M", 4), ("V", 1), ("L", 1), ("D", 1)):
        if letter * (max_run + 1) in s:
            raise ValueError("malformed Roman numeral")
    for i in range(len(s) - 1):
        a, b = s[i], s[i + 1]
        if _LETTERS[a] < _LETTERS[b] and a + b not in _PAIRS:
            raise ValueError("malformed Roman numeral")
    for pair, value in _PAIRS.items():
        for i in range(len(s) - 2):
            if s[i : i + 2] == pair and _LETTERS[s[i + 2]] >= _LETTERS[pair[0]]:
                raise ValueError("malformed Roman numeral")


def from_roman(s: str) -> int:
    """Return the integer value of a Roman numeral string (1..3999)."""
    _check_form(s)
    total = 0
    i = 0
    while i < len(s):
        pair = s[i : i + 2]
        if pair in _PAIRS:
            total += _PAIRS[pair]
            i += 2
        else:
            total += _LETTERS[s[i]]
            i += 1
    if not 1 <= total <= 3999:
        raise ValueError("out of range 1 to 3999")
    return total
