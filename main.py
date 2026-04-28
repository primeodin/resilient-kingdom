#!/usr/bin/env python3
import json
from resilient_kingdom.core import *

def main():
    print(PROJECT + " :: " + DOMAIN)
    rows=run_scenarios(8)
    for row in rows:
        print("{name} energy={energy:.5f} peak={peak:.5f}".format(**row))
    if DOMAIN == "montecarlo":
        path, trace, rate = metropolis_paths(steps=80)
        print("acceptance", round(rate,3)); print(trace.render(4))
    elif DOMAIN == "entropy":
        print(json.dumps(compression_report("rune rage winter code"), sort_keys=True))
    elif DOMAIN == "neural":
        net=TinyNetwork(); data=battle_dataset(20)
        for _ in range(4):
            for x,y in data: net.train_one(x,y)
        print("prediction", round(net.forward(data[0][0])[1],3))
    elif DOMAIN == "quantum":
        c=Circuit().add("H",H).add("X",X).add("H",H)
        print(c.ascii()); print([round(abs(x)**2,3) for x in c.run()])
    elif DOMAIN == "rl":
        q,trace=q_learn(episodes=8); print(trace.render(4))
    elif DOMAIN == "attention":
        head=AttentionHead(3); print(head.attend([1,0,1], [[1,0,0],[0,1,0],[1,0,1]], [[1,0],[0,1],[1,1]]))
    elif DOMAIN == "resilience":
        cb=CircuitBreaker(); [cb.record(False) for _ in range(3)]; print(cb.status())
    else:
        print(simulate(12).render(4))
if __name__ == "__main__": main()
