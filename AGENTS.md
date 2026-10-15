# airlie-sandbox — Agent Instructions

A small Python package used to try out airlie's story pipeline end to end. It uses the Python 3 standard library
only: no third-party packages, no network.

## Layout

- `sandbox/` is the package; one module per topic (`sandbox/text.py`, …).
- `tests/` holds `unittest` tests: one `tests/test_<module>.py` per module.

## Rules

- Every change comes with tests that would fail without it.
- Functions are small, typed and documented in one line.
- Do not add dependencies or configuration files.

## Test gate

```sh
python3 -m unittest -q
```
