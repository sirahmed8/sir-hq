#!/usr/bin/env bash
# Wait until local time HH:MM, then print one summary of the Antigravity batch and exit (one notification for the manager).
target="$1"
while [ "$(date +%H%M)" -lt "$(echo "$target" | tr -d ':')" ]; do sleep 20; done
D=/d/Projects/_SIR/ops/agy-runs/done
echo "WAKE $target. Done markers:"
for f in "$D"/*.done; do [ -e "$f" ] && echo "$(basename "$f"): $(sed 's/"at".*//' "$f")"; done
echo "Expected:"; cat /d/Projects/_SIR/ops/agy-runs/expected.txt | tr '\n' ' '
