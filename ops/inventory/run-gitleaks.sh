#!/usr/bin/env bash
# Redacted secret scan: git history for every repo, working tree for non-git folders. Never prints values.
O="/d/Projects/_SIR/ops/inventory/gitleaks"; cd /d/Projects
for d in */; do d="${d%/}"; [ "$d" = "_SIR" ] && continue; [ -L "$d" ] && continue; [ "$d" = ".remember" ] && continue
  if [ -d "$d/.git" ]; then mode=git; else mode=dir; fi
  gitleaks $mode "$d" --redact=100 --no-banner --exit-code 0 -f json -r "$O/$d.json" >"$O/$d.log" 2>&1
  echo "$d | $mode | done"
done
echo ALL_DONE
