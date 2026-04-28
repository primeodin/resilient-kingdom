#!/usr/bin/env bash
set -euo pipefail
echo "resilient-kingdom: smoke test for the 2020 retrospective chapter"
if [ -f Makefile ]; then make >/tmp/resilient-kingdom.build.log 2>&1 || { cat /tmp/resilient-kingdom.build.log; exit 1; }; fi
if [ -f main.py ]; then python3 main.py >/tmp/resilient-kingdom.run.log; head -20 /tmp/resilient-kingdom.run.log; fi
if [ -f main ]; then ./main 55; fi
if [ -f engine ]; then ./engine | head -12; fi
if [ -f Arena.java ]; then javac Arena.java && java Arena 55; fi
if [ -f deploy.sh ]; then ./deploy.sh old-engine ice-node; fi
echo "The rune holds."
