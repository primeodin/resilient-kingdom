# Start here

A cold-start walkthrough for **resilient-kingdom**: the small circuit-breaker demo
in this repository. It names the exact commands and what "good" looks like on the
current tree.

## Prerequisites

- Python 3.8+ on `PATH` (as `python3`, or `python` on Windows).
- No `pip install`: the core demo uses the standard library only.

## 1. Smoke test

```bash
./scripts/smoke.sh
```

The script runs `main.py` and the unit tests, then ends with:

```text
The rune holds.
```

## 2. Run it by hand

```bash
python3 main.py
python3 -m unittest discover -s tests -q
```

## What success looks like

`main.py` prints eight load lines and then the breaker status:

```text
resilience-000 energy=13.10078 peak=5.02562
resilience-001 energy=8.93199 peak=4.70384
...
resilience-007 energy=0.64553 peak=1.63659
{'failures': 3, 'open_for': 2, 'allow': False}
```

The values shift with the deterministic simulation but the shape is stable: eight
`resilience-00N energy=… peak=…` lines followed by the breaker dict with
`failures`, `open_for` and `allow`. The unit tests report `Ran 4 tests` and `OK`.

## Where to go next

- `ARCHIVE_NOTE.md` — the honesty note about what this repository is.
- `CONTRIBUTING.md` — how to propose a change.
- `docs/why-circuit-breakers.md` — a hand-worked breaker trap (success while open
  rewrites history).
- `resilient_kingdom/core.py` — the breaker itself.
