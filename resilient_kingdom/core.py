import math, random, statistics
from .utils import clamp, moving_average, ascii_bar

PROJECT="resilient-kingdom"
DOMAIN="resilience"
YEAR=2020

class Trace:
    def __init__(self):
        self.rows=[]
    def add(self, step, value, note=""):
        self.rows.append({"step":step,"value":float(value),"note":note})
    def mean(self):
        return statistics.mean([r["value"] for r in self.rows]) if self.rows else 0.0
    def render(self, limit=12):
        lines=[]
        for r in self.rows[:limit]:
            lines.append(f"{r['step']:03d} {r['value']:.5f} {ascii_bar(abs(r['value'])%1.0, 24)} {r['note']}")
        return "\n".join(lines)

class CircuitBreaker:
    def __init__(self, threshold=3, cooldown=2): self.threshold=threshold; self.cooldown=cooldown; self.failures=0; self.open_for=0
    def allow(self): return self.open_for<=0
    def tick(self): self.open_for=max(0,self.open_for-1)
    def record(self, ok):
        if ok: self.failures=0; self.open_for=0
        else:
            self.failures+=1
            if self.failures>=self.threshold: self.open_for=self.cooldown
    def status(self): return {"failures":self.failures,"open_for":self.open_for,"allow":self.allow()}

class RageMeter:
    def __init__(self): self.values=[]
    def observe(self, latency, ok=True): self.values.append((latency,ok))
    def score(self):
        if not self.values: return 0.0
        bad=sum(1 for _,ok in self.values if not ok); avg=sum(v for v,_ in self.values)/len(self.values)
        return clamp(avg/100.0 + bad/len(self.values), 0, 1)

def scenario(index=0, seed=None):
    """Return one deterministic teaching scenario without generated boilerplate.

    Earlier drafts carried hundreds of numbered functions. That made the forge
    look loud but not stronger. The real rune is the parameterization: same idea,
    one readable path, many repeatable cases.
    """
    if index < 0:
        raise ValueError("scenario index must be non-negative")
    if seed is None:
        seed = index
    rng = random.Random(seed + YEAR + index * 17)
    period = 11.0 + (index % 7)
    damping = 0.82 + (index % 5) * 0.025
    values = []
    carry = 0.0
    for j in range(32):
        signal = math.sin((j + 1) * (index + 1) / period)
        noise = (rng.random() - 0.5) * 0.08
        carry = damping * carry + signal + noise
        values.append(carry)
    smooth = moving_average(values, 5)
    energy = sum(v * v for v in smooth) / len(smooth)
    return {"name": f"resilience-{index:03d}", "energy": energy, "peak": max(smooth), "trough": min(smooth)}


def run_scenarios(limit=8, seed=0):
    if limit < 0:
        raise ValueError("limit must be non-negative")
    return [scenario(i, seed + i) for i in range(limit)]
