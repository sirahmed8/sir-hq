#!/usr/bin/env bash
# Run a brief through OpenCode free models until its done marker appears, switching model on failure or when the agent stops early.
# Usage: cli-run.sh <task-name> <project-folder>   (reads ops/briefs/<task-name>.prompt.txt; done marker ops/agy-runs/done/<task-name>.done)
NAME="$1"; DIR="$2"
PROMPT=/d/Projects/_SIR/ops/briefs/$NAME.prompt.txt
DONE=/d/Projects/_SIR/ops/agy-runs/done/$NAME.done
LOG=/d/Projects/_SIR/ops/agy-runs/cli-$NAME.log
MODELS=(kilo/kilo-auto/free opencode/big-pickle kilo/kilo-auto/free opencode/glm-5.3-flash-free kilo/kilo-auto/free opencode/deepseek-v4.1-flash-free)
CONT="Continue: read .sir/CHECKPOINT.md, the checklist file named in the brief, the brief at $PROMPT and the last commits; finish every unticked item completely (commit and checkpoint after each), then write the report and run the done command. Do not stop until every item is ticked."
cd "$DIR" || exit 1
for round in $(seq 1 12); do
  [ -e "$DONE" ] && { echo "done marker present" >> "$LOG"; exit 0; }
  model=${MODELS[$(( (round-1) % ${#MODELS[@]} ))]}
  echo "=== round $round model $model $(date +%H:%M)" >> "$LOG"
  if [ "$round" -eq 1 ]; then msg="$(cat "$PROMPT")"; else msg="$CONT"; fi
  if [[ "$model" == kilo/* ]]; then timeout 3300 kilo run --auto -m "$model" "$msg" >> "$LOG" 2>&1; else timeout 3300 opencode run -m "$model" "$msg" >> "$LOG" 2>&1; fi
  grep -q "Free usage limit reached" "$LOG" && true
  echo "=== round $round ended code $? $(date +%H:%M)" >> "$LOG"
  sleep 30
done
