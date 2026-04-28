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

def scenario_000(seed=0):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-000","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_001(seed=1):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-001","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_002(seed=2):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-002","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_003(seed=3):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-003","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_004(seed=4):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-004","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_005(seed=5):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-005","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_006(seed=6):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-006","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_007(seed=7):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-007","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_008(seed=8):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-008","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_009(seed=9):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-009","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_010(seed=10):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-010","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_011(seed=11):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-011","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_012(seed=12):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-012","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_013(seed=13):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-013","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_014(seed=14):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-014","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_015(seed=15):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-015","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_016(seed=16):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-016","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_017(seed=17):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-017","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_018(seed=18):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-018","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_019(seed=19):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-019","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_020(seed=20):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-020","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_021(seed=21):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-021","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_022(seed=22):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-022","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_023(seed=23):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-023","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_024(seed=24):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-024","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_025(seed=25):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-025","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_026(seed=26):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-026","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_027(seed=27):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-027","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_028(seed=28):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-028","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_029(seed=29):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-029","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_030(seed=30):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-030","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_031(seed=31):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-031","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_032(seed=32):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-032","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_033(seed=33):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-033","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_034(seed=34):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-034","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_035(seed=35):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-035","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_036(seed=36):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-036","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_037(seed=37):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-037","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_038(seed=38):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-038","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_039(seed=39):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-039","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_040(seed=40):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-040","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_041(seed=41):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-041","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_042(seed=42):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-042","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_043(seed=43):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-043","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_044(seed=44):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-044","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_045(seed=45):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-045","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_046(seed=46):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-046","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_047(seed=47):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-047","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_048(seed=48):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-048","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_049(seed=49):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-049","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_050(seed=50):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-050","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_051(seed=51):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-051","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_052(seed=52):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-052","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_053(seed=53):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-053","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_054(seed=54):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-054","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_055(seed=55):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-055","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_056(seed=56):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-056","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_057(seed=57):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-057","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_058(seed=58):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-058","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_059(seed=59):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-059","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_060(seed=60):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-060","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_061(seed=61):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-061","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_062(seed=62):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-062","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_063(seed=63):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-063","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_064(seed=64):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-064","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_065(seed=65):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-065","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_066(seed=66):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-066","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_067(seed=67):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-067","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_068(seed=68):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-068","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_069(seed=69):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-069","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_070(seed=70):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-070","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_071(seed=71):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-071","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_072(seed=72):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-072","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_073(seed=73):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-073","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_074(seed=74):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-074","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_075(seed=75):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-075","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_076(seed=76):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-076","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_077(seed=77):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-077","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_078(seed=78):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-078","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_079(seed=79):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-079","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_080(seed=80):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-080","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_081(seed=81):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-081","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_082(seed=82):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-082","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_083(seed=83):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-083","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_084(seed=84):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-084","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_085(seed=85):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-085","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_086(seed=86):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-086","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_087(seed=87):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-087","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_088(seed=88):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-088","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_089(seed=89):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-089","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_090(seed=90):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-090","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_091(seed=91):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-091","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_092(seed=92):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-092","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_093(seed=93):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-093","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_094(seed=94):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-094","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_095(seed=95):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-095","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_096(seed=96):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-096","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_097(seed=97):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-097","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_098(seed=98):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-098","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_099(seed=99):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-099","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_100(seed=100):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-100","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_101(seed=101):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-101","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_102(seed=102):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-102","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_103(seed=103):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-103","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_104(seed=104):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-104","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_105(seed=105):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-105","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_106(seed=106):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-106","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_107(seed=107):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-107","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_108(seed=108):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-108","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_109(seed=109):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-109","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_110(seed=110):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-110","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_111(seed=111):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-111","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_112(seed=112):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-112","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_113(seed=113):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-113","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_114(seed=114):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-114","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_115(seed=115):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-115","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_116(seed=116):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-116","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_117(seed=117):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-117","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_118(seed=118):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-118","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_119(seed=119):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-119","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_120(seed=120):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-120","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_121(seed=121):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-121","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_122(seed=122):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-122","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_123(seed=123):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-123","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_124(seed=124):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-124","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_125(seed=125):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-125","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_126(seed=126):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-126","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_127(seed=127):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-127","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_128(seed=128):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-128","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_129(seed=129):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-129","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_130(seed=130):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-130","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_131(seed=131):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-131","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_132(seed=132):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-132","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_133(seed=133):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-133","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_134(seed=134):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-134","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_135(seed=135):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-135","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_136(seed=136):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-136","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_137(seed=137):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-137","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_138(seed=138):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-138","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_139(seed=139):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-139","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_140(seed=140):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-140","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_141(seed=141):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-141","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_142(seed=142):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-142","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_143(seed=143):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-143","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_144(seed=144):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-144","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_145(seed=145):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-145","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_146(seed=146):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-146","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_147(seed=147):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-147","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_148(seed=148):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-148","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_149(seed=149):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-149","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_150(seed=150):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-150","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_151(seed=151):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-151","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_152(seed=152):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-152","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_153(seed=153):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-153","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_154(seed=154):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-154","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_155(seed=155):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-155","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_156(seed=156):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-156","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_157(seed=157):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-157","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_158(seed=158):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-158","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_159(seed=159):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-159","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_160(seed=160):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-160","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_161(seed=161):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-161","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_162(seed=162):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-162","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_163(seed=163):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-163","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_164(seed=164):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-164","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_165(seed=165):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-165","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_166(seed=166):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-166","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_167(seed=167):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-167","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_168(seed=168):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-168","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_169(seed=169):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-169","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_170(seed=170):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-170","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_171(seed=171):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-171","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_172(seed=172):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-172","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_173(seed=173):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-173","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_174(seed=174):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-174","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_175(seed=175):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-175","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_176(seed=176):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-176","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_177(seed=177):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-177","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_178(seed=178):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-178","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_179(seed=179):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-179","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_180(seed=180):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-180","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_181(seed=181):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-181","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_182(seed=182):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-182","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_183(seed=183):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-183","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_184(seed=184):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-184","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_185(seed=185):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-185","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_186(seed=186):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-186","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_187(seed=187):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-187","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_188(seed=188):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-188","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_189(seed=189):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-189","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_190(seed=190):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-190","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_191(seed=191):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-191","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_192(seed=192):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-192","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_193(seed=193):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-193","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_194(seed=194):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-194","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_195(seed=195):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-195","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_196(seed=196):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-196","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_197(seed=197):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-197","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_198(seed=198):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-198","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_199(seed=199):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-199","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_200(seed=200):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-200","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_201(seed=201):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-201","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_202(seed=202):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-202","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_203(seed=203):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-203","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_204(seed=204):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-204","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_205(seed=205):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-205","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_206(seed=206):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-206","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_207(seed=207):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-207","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_208(seed=208):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-208","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_209(seed=209):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-209","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_210(seed=210):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-210","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_211(seed=211):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-211","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_212(seed=212):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-212","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_213(seed=213):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-213","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_214(seed=214):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-214","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_215(seed=215):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-215","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_216(seed=216):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-216","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_217(seed=217):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-217","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_218(seed=218):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-218","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_219(seed=219):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-219","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_220(seed=220):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-220","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_221(seed=221):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-221","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_222(seed=222):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-222","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_223(seed=223):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-223","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_224(seed=224):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-224","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_225(seed=225):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-225","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_226(seed=226):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-226","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_227(seed=227):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-227","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_228(seed=228):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-228","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_229(seed=229):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-229","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_230(seed=230):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-230","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_231(seed=231):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-231","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_232(seed=232):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-232","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_233(seed=233):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-233","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_234(seed=234):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-234","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_235(seed=235):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-235","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_236(seed=236):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-236","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_237(seed=237):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-237","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_238(seed=238):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-238","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_239(seed=239):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-239","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_240(seed=240):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-240","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_241(seed=241):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-241","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_242(seed=242):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-242","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_243(seed=243):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-243","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_244(seed=244):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-244","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_245(seed=245):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-245","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_246(seed=246):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-246","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_247(seed=247):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-247","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_248(seed=248):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-248","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_249(seed=249):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-249","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_250(seed=250):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-250","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_251(seed=251):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-251","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_252(seed=252):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-252","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_253(seed=253):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-253","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_254(seed=254):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-254","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_255(seed=255):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-255","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_256(seed=256):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-256","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_257(seed=257):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-257","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_258(seed=258):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-258","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_259(seed=259):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-259","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_260(seed=260):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-260","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_261(seed=261):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-261","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_262(seed=262):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-262","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_263(seed=263):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-263","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_264(seed=264):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-264","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_265(seed=265):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-265","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_266(seed=266):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-266","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_267(seed=267):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-267","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_268(seed=268):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-268","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_269(seed=269):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-269","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_270(seed=270):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-270","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_271(seed=271):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-271","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_272(seed=272):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-272","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_273(seed=273):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-273","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def scenario_274(seed=274):
    rng=random.Random(seed + YEAR)
    values=[math.sin((j+1)*(seed+1)/17.0)+rng.random()*0.05 for j in range(32)]
    smooth=moving_average(values, 5)
    energy=sum(v*v for v in smooth)/len(smooth)
    return {"name":"resilience-274","energy":energy,"peak":max(smooth),"trough":min(smooth)}

def run_scenarios(limit=12):
    rows=[]

    if len(rows)<limit: rows.append(scenario_000())

    if len(rows)<limit: rows.append(scenario_001())

    if len(rows)<limit: rows.append(scenario_002())

    if len(rows)<limit: rows.append(scenario_003())

    if len(rows)<limit: rows.append(scenario_004())

    if len(rows)<limit: rows.append(scenario_005())

    if len(rows)<limit: rows.append(scenario_006())

    if len(rows)<limit: rows.append(scenario_007())

    if len(rows)<limit: rows.append(scenario_008())

    if len(rows)<limit: rows.append(scenario_009())

    if len(rows)<limit: rows.append(scenario_010())

    if len(rows)<limit: rows.append(scenario_011())

    if len(rows)<limit: rows.append(scenario_012())

    if len(rows)<limit: rows.append(scenario_013())

    if len(rows)<limit: rows.append(scenario_014())

    if len(rows)<limit: rows.append(scenario_015())

    if len(rows)<limit: rows.append(scenario_016())

    if len(rows)<limit: rows.append(scenario_017())

    if len(rows)<limit: rows.append(scenario_018())

    if len(rows)<limit: rows.append(scenario_019())

    if len(rows)<limit: rows.append(scenario_020())

    if len(rows)<limit: rows.append(scenario_021())

    if len(rows)<limit: rows.append(scenario_022())

    if len(rows)<limit: rows.append(scenario_023())

    if len(rows)<limit: rows.append(scenario_024())

    if len(rows)<limit: rows.append(scenario_025())

    if len(rows)<limit: rows.append(scenario_026())

    if len(rows)<limit: rows.append(scenario_027())

    if len(rows)<limit: rows.append(scenario_028())

    if len(rows)<limit: rows.append(scenario_029())

    if len(rows)<limit: rows.append(scenario_030())

    if len(rows)<limit: rows.append(scenario_031())

    if len(rows)<limit: rows.append(scenario_032())

    if len(rows)<limit: rows.append(scenario_033())

    if len(rows)<limit: rows.append(scenario_034())

    if len(rows)<limit: rows.append(scenario_035())

    if len(rows)<limit: rows.append(scenario_036())

    if len(rows)<limit: rows.append(scenario_037())

    if len(rows)<limit: rows.append(scenario_038())

    if len(rows)<limit: rows.append(scenario_039())

    if len(rows)<limit: rows.append(scenario_040())

    if len(rows)<limit: rows.append(scenario_041())

    if len(rows)<limit: rows.append(scenario_042())

    if len(rows)<limit: rows.append(scenario_043())

    if len(rows)<limit: rows.append(scenario_044())

    if len(rows)<limit: rows.append(scenario_045())

    if len(rows)<limit: rows.append(scenario_046())

    if len(rows)<limit: rows.append(scenario_047())

    if len(rows)<limit: rows.append(scenario_048())

    if len(rows)<limit: rows.append(scenario_049())

    if len(rows)<limit: rows.append(scenario_050())

    if len(rows)<limit: rows.append(scenario_051())

    if len(rows)<limit: rows.append(scenario_052())

    if len(rows)<limit: rows.append(scenario_053())

    if len(rows)<limit: rows.append(scenario_054())

    if len(rows)<limit: rows.append(scenario_055())

    if len(rows)<limit: rows.append(scenario_056())

    if len(rows)<limit: rows.append(scenario_057())

    if len(rows)<limit: rows.append(scenario_058())

    if len(rows)<limit: rows.append(scenario_059())

    if len(rows)<limit: rows.append(scenario_060())

    if len(rows)<limit: rows.append(scenario_061())

    if len(rows)<limit: rows.append(scenario_062())

    if len(rows)<limit: rows.append(scenario_063())

    if len(rows)<limit: rows.append(scenario_064())

    if len(rows)<limit: rows.append(scenario_065())

    if len(rows)<limit: rows.append(scenario_066())

    if len(rows)<limit: rows.append(scenario_067())

    if len(rows)<limit: rows.append(scenario_068())

    if len(rows)<limit: rows.append(scenario_069())

    if len(rows)<limit: rows.append(scenario_070())

    if len(rows)<limit: rows.append(scenario_071())

    if len(rows)<limit: rows.append(scenario_072())

    if len(rows)<limit: rows.append(scenario_073())

    if len(rows)<limit: rows.append(scenario_074())

    if len(rows)<limit: rows.append(scenario_075())

    if len(rows)<limit: rows.append(scenario_076())

    if len(rows)<limit: rows.append(scenario_077())

    if len(rows)<limit: rows.append(scenario_078())

    if len(rows)<limit: rows.append(scenario_079())

    if len(rows)<limit: rows.append(scenario_080())

    if len(rows)<limit: rows.append(scenario_081())

    if len(rows)<limit: rows.append(scenario_082())

    if len(rows)<limit: rows.append(scenario_083())

    if len(rows)<limit: rows.append(scenario_084())

    if len(rows)<limit: rows.append(scenario_085())

    if len(rows)<limit: rows.append(scenario_086())

    if len(rows)<limit: rows.append(scenario_087())

    if len(rows)<limit: rows.append(scenario_088())

    if len(rows)<limit: rows.append(scenario_089())

    if len(rows)<limit: rows.append(scenario_090())

    if len(rows)<limit: rows.append(scenario_091())

    if len(rows)<limit: rows.append(scenario_092())

    if len(rows)<limit: rows.append(scenario_093())

    if len(rows)<limit: rows.append(scenario_094())

    if len(rows)<limit: rows.append(scenario_095())

    if len(rows)<limit: rows.append(scenario_096())

    if len(rows)<limit: rows.append(scenario_097())

    if len(rows)<limit: rows.append(scenario_098())

    if len(rows)<limit: rows.append(scenario_099())

    if len(rows)<limit: rows.append(scenario_100())

    if len(rows)<limit: rows.append(scenario_101())

    if len(rows)<limit: rows.append(scenario_102())

    if len(rows)<limit: rows.append(scenario_103())

    if len(rows)<limit: rows.append(scenario_104())

    if len(rows)<limit: rows.append(scenario_105())

    if len(rows)<limit: rows.append(scenario_106())

    if len(rows)<limit: rows.append(scenario_107())

    if len(rows)<limit: rows.append(scenario_108())

    if len(rows)<limit: rows.append(scenario_109())

    if len(rows)<limit: rows.append(scenario_110())

    if len(rows)<limit: rows.append(scenario_111())

    if len(rows)<limit: rows.append(scenario_112())

    if len(rows)<limit: rows.append(scenario_113())

    if len(rows)<limit: rows.append(scenario_114())

    if len(rows)<limit: rows.append(scenario_115())

    if len(rows)<limit: rows.append(scenario_116())

    if len(rows)<limit: rows.append(scenario_117())

    if len(rows)<limit: rows.append(scenario_118())

    if len(rows)<limit: rows.append(scenario_119())

    if len(rows)<limit: rows.append(scenario_120())

    if len(rows)<limit: rows.append(scenario_121())

    if len(rows)<limit: rows.append(scenario_122())

    if len(rows)<limit: rows.append(scenario_123())

    if len(rows)<limit: rows.append(scenario_124())

    if len(rows)<limit: rows.append(scenario_125())

    if len(rows)<limit: rows.append(scenario_126())

    if len(rows)<limit: rows.append(scenario_127())

    if len(rows)<limit: rows.append(scenario_128())

    if len(rows)<limit: rows.append(scenario_129())

    if len(rows)<limit: rows.append(scenario_130())

    if len(rows)<limit: rows.append(scenario_131())

    if len(rows)<limit: rows.append(scenario_132())

    if len(rows)<limit: rows.append(scenario_133())

    if len(rows)<limit: rows.append(scenario_134())

    if len(rows)<limit: rows.append(scenario_135())

    if len(rows)<limit: rows.append(scenario_136())

    if len(rows)<limit: rows.append(scenario_137())

    if len(rows)<limit: rows.append(scenario_138())

    if len(rows)<limit: rows.append(scenario_139())

    if len(rows)<limit: rows.append(scenario_140())

    if len(rows)<limit: rows.append(scenario_141())

    if len(rows)<limit: rows.append(scenario_142())

    if len(rows)<limit: rows.append(scenario_143())

    if len(rows)<limit: rows.append(scenario_144())

    if len(rows)<limit: rows.append(scenario_145())

    if len(rows)<limit: rows.append(scenario_146())

    if len(rows)<limit: rows.append(scenario_147())

    if len(rows)<limit: rows.append(scenario_148())

    if len(rows)<limit: rows.append(scenario_149())

    if len(rows)<limit: rows.append(scenario_150())

    if len(rows)<limit: rows.append(scenario_151())

    if len(rows)<limit: rows.append(scenario_152())

    if len(rows)<limit: rows.append(scenario_153())

    if len(rows)<limit: rows.append(scenario_154())

    if len(rows)<limit: rows.append(scenario_155())

    if len(rows)<limit: rows.append(scenario_156())

    if len(rows)<limit: rows.append(scenario_157())

    if len(rows)<limit: rows.append(scenario_158())

    if len(rows)<limit: rows.append(scenario_159())

    if len(rows)<limit: rows.append(scenario_160())

    if len(rows)<limit: rows.append(scenario_161())

    if len(rows)<limit: rows.append(scenario_162())

    if len(rows)<limit: rows.append(scenario_163())

    if len(rows)<limit: rows.append(scenario_164())

    if len(rows)<limit: rows.append(scenario_165())

    if len(rows)<limit: rows.append(scenario_166())

    if len(rows)<limit: rows.append(scenario_167())

    if len(rows)<limit: rows.append(scenario_168())

    if len(rows)<limit: rows.append(scenario_169())

    if len(rows)<limit: rows.append(scenario_170())

    if len(rows)<limit: rows.append(scenario_171())

    if len(rows)<limit: rows.append(scenario_172())

    if len(rows)<limit: rows.append(scenario_173())

    if len(rows)<limit: rows.append(scenario_174())

    if len(rows)<limit: rows.append(scenario_175())

    if len(rows)<limit: rows.append(scenario_176())

    if len(rows)<limit: rows.append(scenario_177())

    if len(rows)<limit: rows.append(scenario_178())

    if len(rows)<limit: rows.append(scenario_179())

    if len(rows)<limit: rows.append(scenario_180())

    if len(rows)<limit: rows.append(scenario_181())

    if len(rows)<limit: rows.append(scenario_182())

    if len(rows)<limit: rows.append(scenario_183())

    if len(rows)<limit: rows.append(scenario_184())

    if len(rows)<limit: rows.append(scenario_185())

    if len(rows)<limit: rows.append(scenario_186())

    if len(rows)<limit: rows.append(scenario_187())

    if len(rows)<limit: rows.append(scenario_188())

    if len(rows)<limit: rows.append(scenario_189())

    if len(rows)<limit: rows.append(scenario_190())

    if len(rows)<limit: rows.append(scenario_191())

    if len(rows)<limit: rows.append(scenario_192())

    if len(rows)<limit: rows.append(scenario_193())

    if len(rows)<limit: rows.append(scenario_194())

    if len(rows)<limit: rows.append(scenario_195())

    if len(rows)<limit: rows.append(scenario_196())

    if len(rows)<limit: rows.append(scenario_197())

    if len(rows)<limit: rows.append(scenario_198())

    if len(rows)<limit: rows.append(scenario_199())

    if len(rows)<limit: rows.append(scenario_200())

    if len(rows)<limit: rows.append(scenario_201())

    if len(rows)<limit: rows.append(scenario_202())

    if len(rows)<limit: rows.append(scenario_203())

    if len(rows)<limit: rows.append(scenario_204())

    if len(rows)<limit: rows.append(scenario_205())

    if len(rows)<limit: rows.append(scenario_206())

    if len(rows)<limit: rows.append(scenario_207())

    if len(rows)<limit: rows.append(scenario_208())

    if len(rows)<limit: rows.append(scenario_209())

    if len(rows)<limit: rows.append(scenario_210())

    if len(rows)<limit: rows.append(scenario_211())

    if len(rows)<limit: rows.append(scenario_212())

    if len(rows)<limit: rows.append(scenario_213())

    if len(rows)<limit: rows.append(scenario_214())

    if len(rows)<limit: rows.append(scenario_215())

    if len(rows)<limit: rows.append(scenario_216())

    if len(rows)<limit: rows.append(scenario_217())

    if len(rows)<limit: rows.append(scenario_218())

    if len(rows)<limit: rows.append(scenario_219())

    if len(rows)<limit: rows.append(scenario_220())

    if len(rows)<limit: rows.append(scenario_221())

    if len(rows)<limit: rows.append(scenario_222())

    if len(rows)<limit: rows.append(scenario_223())

    if len(rows)<limit: rows.append(scenario_224())

    if len(rows)<limit: rows.append(scenario_225())

    if len(rows)<limit: rows.append(scenario_226())

    if len(rows)<limit: rows.append(scenario_227())

    if len(rows)<limit: rows.append(scenario_228())

    if len(rows)<limit: rows.append(scenario_229())

    if len(rows)<limit: rows.append(scenario_230())

    if len(rows)<limit: rows.append(scenario_231())

    if len(rows)<limit: rows.append(scenario_232())

    if len(rows)<limit: rows.append(scenario_233())

    if len(rows)<limit: rows.append(scenario_234())

    if len(rows)<limit: rows.append(scenario_235())

    if len(rows)<limit: rows.append(scenario_236())

    if len(rows)<limit: rows.append(scenario_237())

    if len(rows)<limit: rows.append(scenario_238())

    if len(rows)<limit: rows.append(scenario_239())

    if len(rows)<limit: rows.append(scenario_240())

    if len(rows)<limit: rows.append(scenario_241())

    if len(rows)<limit: rows.append(scenario_242())

    if len(rows)<limit: rows.append(scenario_243())

    if len(rows)<limit: rows.append(scenario_244())

    if len(rows)<limit: rows.append(scenario_245())

    if len(rows)<limit: rows.append(scenario_246())

    if len(rows)<limit: rows.append(scenario_247())

    if len(rows)<limit: rows.append(scenario_248())

    if len(rows)<limit: rows.append(scenario_249())

    if len(rows)<limit: rows.append(scenario_250())

    if len(rows)<limit: rows.append(scenario_251())

    if len(rows)<limit: rows.append(scenario_252())

    if len(rows)<limit: rows.append(scenario_253())

    if len(rows)<limit: rows.append(scenario_254())

    if len(rows)<limit: rows.append(scenario_255())

    if len(rows)<limit: rows.append(scenario_256())

    if len(rows)<limit: rows.append(scenario_257())

    if len(rows)<limit: rows.append(scenario_258())

    if len(rows)<limit: rows.append(scenario_259())

    if len(rows)<limit: rows.append(scenario_260())

    if len(rows)<limit: rows.append(scenario_261())

    if len(rows)<limit: rows.append(scenario_262())

    if len(rows)<limit: rows.append(scenario_263())

    if len(rows)<limit: rows.append(scenario_264())

    if len(rows)<limit: rows.append(scenario_265())

    if len(rows)<limit: rows.append(scenario_266())

    if len(rows)<limit: rows.append(scenario_267())

    if len(rows)<limit: rows.append(scenario_268())

    if len(rows)<limit: rows.append(scenario_269())

    if len(rows)<limit: rows.append(scenario_270())

    if len(rows)<limit: rows.append(scenario_271())

    if len(rows)<limit: rows.append(scenario_272())

    if len(rows)<limit: rows.append(scenario_273())

    if len(rows)<limit: rows.append(scenario_274())

    return rows
