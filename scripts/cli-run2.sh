#!/usr/bin/env bash
# Run a brief through the free CLI agents in turns until its done marker appears.
# Usage: cli-run2.sh <task-name> <project-folder>
# Reads ops/briefs/<task-name>.prompt.txt, done marker ops/agy-runs/done/<task-name>.done, log ops/agy-runs/cli-<task-name>.log
NAME="$1"; DIR="$2"
PROMPT=/d/Projects/_SIR/ops/briefs/$NAME.prompt.txt
DONE=/d/Projects/_SIR/ops/agy-runs/done/$NAME.done
LOG=/d/Projects/_SIR/ops/agy-runs/cli-$NAME.log
DEVIN="$LOCALAPPDATA/devin/cli/bin/devin.exe"
# order: strongest free first; a tool that reports a limit is skipped by the next round automatically
TOOLS=(kilo:kilo/kilo-auto/free opencode:opencode/big-pickle devin:swe-2-flash-medium opencode:openrouter/nvidia/nemotron-3-ultra-550b-a55b:free opencode:opencode/glm-5.3-flash-free kilo:kilo/kilo-auto/free opencode:opencode/deepseek-v4.1-flash-free opencode:openrouter/openrouter/free)
CONT="Continue: read .sir/CHECKPOINT.md, the checklist file named in the brief, the brief file $PROMPT and git status plus the last commits; finish every unticked item completely (commit and checkpoint after each item), then write the report and run the done command. Web research is allowed (if the web search tool crashes use curl or fetch), never put private data in a query. Do not stop until every item is ticked."
cd "$DIR" || exit 1
for round in $(seq 1 24); do
  [ -e "$DONE" ] && { echo "done marker present" >> "$LOG"; exit 0; }
  entry=${TOOLS[$(( (round-1) % ${#TOOLS[@]} ))]}
  tool=${entry%%:*}; model=${entry#*:}
  echo "=== round $round $tool $model $(date +%H:%M)" >> "$LOG"
  if [ "$round" -eq 1 ]; then msg="$(cat "$PROMPT")"; else msg="$CONT"; fi
  case "$tool" in
    kilo) timeout 3300 kilo run --auto -m "$model" "$msg" >> "$LOG" 2>&1 ;;
    opencode) timeout 3300 opencode run -m "$model" "$msg" >> "$LOG" 2>&1 ;;
    devin) timeout 3300 "$DEVIN" -p --model "$model" --permission-mode smart --respect-workspace-trust false -- "$msg" >> "$LOG" 2>&1 ;;
  esac
  echo "=== round $round ended code $? $(date +%H:%M)" >> "$LOG"
  sleep 30
done
