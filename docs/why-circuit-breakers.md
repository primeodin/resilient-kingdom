# Why circuit breakers (trip ≠ recover)

> Shop teaching for `resilient-kingdom`: a breaker is not a retry loop. It is a **permission gate**. Failures trip the gate; cooldown only restores *permission to try* — a success still has to land before you trust the path again.

## The trap in one picture

`CircuitBreaker` in `resilient_kingdom/core.py` (defaults: `threshold=3`, `cooldown=2`):

```text
closed  --(N failures)-->  open (open_for = cooldown)
  ^                              |
  |                         tick…tick
  +--------(success)------ half-open-ish (allow=True again)
```

There is no separate half-open *state* object — `allow()` is just `open_for <= 0`. Callers are supposed to ask `allow()` before hitting the dependency. If you skip that check, a stray success while the gate is still open rewrites history (see trap below).

## Hand-worked demo (matches `main.py` resilience branch)

```python
from resilient_kingdom.core import CircuitBreaker

cb = CircuitBreaker(threshold=3, cooldown=2)
print(cb.status())  # {'failures': 0, 'open_for': 0, 'allow': True}

cb.record(False)  # failures=1, still allow
cb.record(False)  # failures=2, still allow
cb.record(False)  # failures=3 → open_for=2, allow=False
print(cb.status())  # {'failures': 3, 'open_for': 2, 'allow': False}
```

That last line is exactly what `python3 main.py` prints after the scenario table on this tree.

| Step | Call | `failures` | `open_for` | `allow` |
| --- | --- | ---: | ---: | --- |
| 0 | (fresh) | 0 | 0 | True |
| 1 | `record(False)` | 1 | 0 | True |
| 2 | `record(False)` | 2 | 0 | True |
| 3 | `record(False)` | 3 | **2** | **False** |
| 4 | `tick()` | 3 | 1 | False |
| 5 | `tick()` | 3 | **0** | **True** |
| 6 | `record(True)` | **0** | 0 | True |

Cooldownown ticks do **not** clear `failures`. Only a success does. Permission returned; trust still unpaid until `record(True)`.

## Trap: success while open (forgot to gate on `allow`)

```python
cb = CircuitBreaker(threshold=3, cooldown=2)
[cb.record(False) for _ in range(3)]
print(cb.status())      # open: allow=False, open_for=2
cb.record(True)         # oops — no allow() check
print(cb.status())      # {'failures': 0, 'open_for': 0, 'allow': True}
```

The breaker "healed" without waiting out the cooldown because `record(True)` always resets. Shop rule: **trip ≠ recover**. Opening is the trip. Cooldown is recovery *permission*. Success is the only trust reset — and you should only attempt it when `allow()` says so.

## Rage meter (stress, not the gate)

`RageMeter.score()` blends average latency/100 with the failure fraction, then clamps to `[0, 1]`:

```python
rm = RageMeter()
rm.observe(50, True)
rm.observe(120, False)
rm.observe(80, False)
rm.score()  # → 1.0  (0.833 latency term + 0.667 fail term → clamp)
```

Useful as a dashboard signal. It does **not** open the breaker. Keep the meter for humans; keep the breaker for the call path.

## Shop judgment

| Situation | Do this |
| --- | --- |
| Dependency flapping (timeouts, 5xx) | Breaker with a small threshold + explicit `allow()` before each call |
| Teaching / local tools | Print `status()` after each record/tick so the trip is visible |
| Tempted to auto-`record(True)` on any response | Gate first. A lucky 200 during open must not erase the siege unless you meant half-open probe |
| Only watching a rage/latency gauge | That is a smoke alarm, not a door lock. Wire the breaker separately |

If you change threshold/cooldown semantics, update this doc and the resilience branch in `main.py` in the same PR — a breaker nobody can explain is just a boolean with anxiety.

## Run it

```bash
python3 main.py
# …scenario lines…
# {'failures': 3, 'open_for': 2, 'allow': False}

./scripts/smoke.sh   # unit tests + the same main path
```
