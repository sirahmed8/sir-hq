#!/usr/bin/env bash
# One event per batch: wait until every task named in ops/agy-runs/expected.txt has a done marker, then print one summary and exit.
# Prints a single ATTENTION summary earlier if a task reports fail/blocked or the deadline passes (default 28 min) with tasks missing.
D=/d/Projects/_SIR/ops/agy-runs/done
E=/d/Projects/_SIR/ops/agy-runs/expected.txt
DEADLINE=$(( $(date +%s) + ${1:-1680} ))
summ() {
  while read -r n; do
    [ -z "$n" ] && continue
    if [ -e "$D/$n.done" ]; then echo "$n: $(cat "$D/$n.done" | sed 's/"at".*//' )"; else echo "$n: MISSING"; fi
  done < "$E"
}
while true; do
  total=0; done_n=0; bad=0
  while read -r n; do
    [ -z "$n" ] && continue
    total=$((total+1))
    if [ -e "$D/$n.done" ]; then
      done_n=$((done_n+1))
      grep -qE '"status": "(fail|blocked)"' "$D/$n.done" && bad=$((bad+1))
    fi
  done < "$E"
  if [ "$total" -gt 0 ] && [ "$done_n" -eq "$total" ]; then
    echo "BATCH COMPLETE ($done_n/$total, $bad failed or blocked):"; summ; exit 0
  fi
  if [ "$bad" -gt 0 ] && [ "$done_n" -gt 0 ] && [ $(( $(date +%s) )) -ge "$DEADLINE" ]; then :; fi
  if [ "$(date +%s)" -ge "$DEADLINE" ]; then
    echo "ATTENTION deadline reached ($done_n/$total done, $bad failed or blocked):"; summ; exit 0
  fi
  sleep 10
done
