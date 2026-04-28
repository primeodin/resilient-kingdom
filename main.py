#!/usr/bin/env python3
"""resilient-kingdom: honest retrospective 2020 chapter."""
import math, random

def rage_curve(x):
    return 1.0 / (1.0 + math.exp(-x))

def demo(seed=7):
    random.seed(seed)
    total = 0.0
    for i in range(8):
        sample = random.random() * 2 - 1
        total += rage_curve(sample * 3)
        print("step=%02d sample=%+.3f focus=%.3f" % (i, sample, total/(i+1)))
    return total/8

if __name__ == "__main__":
    print("resilient-kingdom")
    print("mean-focus=%.4f" % demo())
