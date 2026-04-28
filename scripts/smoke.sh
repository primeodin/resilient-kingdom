#!/usr/bin/env bash
set -euo pipefail
python3 main.py | head -40
python3 -m unittest discover -s tests -q
echo "The rune holds."
