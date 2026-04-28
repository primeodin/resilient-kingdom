import math, random, statistics, json

class RuneError(Exception): pass

def clamp(value, low, high):
    return max(low, min(high, value))

def seeded(seed=13):
    r=random.Random(seed); return r

def moving_average(values, window):
    out=[]
    for i in range(len(values)):
        lo=max(0,i-window+1); out.append(sum(values[lo:i+1])/(i-lo+1))
    return out

def ascii_bar(value, width=40, char="#"):
    n=int(clamp(value,0,1)*width); return char*n+"."*(width-n)
