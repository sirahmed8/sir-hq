#!/usr/bin/env bash
# Emit one line per new Antigravity completion marker (ops/agy-runs/done/*.done). Used with the Monitor tool.
D=/d/Projects/_SIR/ops/agy-runs/done
mkdir -p "$D"
seen="$D/.seen"
touch "$seen"
while true; do
  for f in "$D"/*.done; do
    [ -e "$f" ] || continue
    b=$(basename "$f")
    if ! grep -qx "$b" "$seen"; then
      echo "$b $(cat "$f")"
      echo "$b" >> "$seen"
    fi
  done
  sleep 3
done
