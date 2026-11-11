#!/usr/bin/env bash
# Run a brief through the free CLI agents until its done marker appears.
# Usage: cli-run2.sh <task-name> <project-folder>
# Reads ops/WORKER_PREAMBLE.md + ops/briefs/<task>.prompt.txt, done marker ops/agy-runs/done/<task>.done, log ops/agy-runs/cli-<task>.log
# Which model runs next comes from scripts/cli_pool.py (shared cooldown file, so two tasks never hammer a model that is out of quota).
NAME="$1"; DIR="$2"
ROOT=/d/Projects/_SIR
GAME_SNAP="/d/Projects/SIR Laptop Manager/.sir/game_mode_snapshot.json"
PROMPT=$ROOT/ops/briefs/$NAME.prompt.txt
PREAMBLE=$ROOT/ops/WORKER_PREAMBLE.md
DONE=$ROOT/ops/agy-runs/done/$NAME.done
LOG=$ROOT/ops/agy-runs/cli-$NAME.log
DEVIN="$LOCALAPPDATA/devin/cli/bin/devin.exe"
CONT="Continue task $NAME. Read $PREAMBLE, then .sir/CHECKPOINT.md, the checklist file named in the brief, the brief $PROMPT, git status, git diff --stat and the last commits. Repair anything broken first, then finish every unticked item completely (commit, push and checkpoint after each item), then write the report and run the done command from the manual. Do not stop until every item is ticked and CI on main is green."
cd "$DIR" || exit 1
# Run the whole runner tree at BelowNormal priority so automations never freeze the laptop.
WINPID=$(cat /proc/$$/winpid 2>/dev/null || true)
[ -n "$WINPID" ] && powershell -NoProfile -Command "(Get-Process -Id $WINPID -EA 0).PriorityClass='BelowNormal'" 2>/dev/null
for round in $(seq 1 40); do
  [ -e "$DONE" ] && { echo "done marker present" >> "$LOG"; exit 0; }
  if [ -e "$GAME_SNAP" ]; then echo "=== game mode active: runner paused $(date +%H:%M)" >> "$LOG"; exit 0; fi
  pick=$(python $ROOT/scripts/cli_pool.py pick)
  case "$pick" in
    WAIT*)
      secs=${pick#WAIT }
      echo "=== all free models cooling down, usage limit, next try in $((secs/60)) min $(date +%H:%M)" >> "$LOG"
      echo "=== usage limit: pool empty, runner exits so the autopilot retries later" >> "$LOG"
      exit 0 ;;
  esac
  tool=${pick%%|*}; model=${pick#*|}
  echo "=== round $round $tool $model $(date +%H:%M)" >> "$LOG"
  if [ "$round" -eq 1 ] && [ ! -s "$LOG.started" ]; then msg="$(cat "$PREAMBLE" "$PROMPT")"; touch "$LOG.started"; echo x > "$LOG.started"; else msg="$CONT"; fi
  offset=$(stat -c %s "$LOG"); t0=$(date +%s)
  case "$tool" in
    kilo) timeout 3300 kilo run --auto -m "$model" "$msg" >> "$LOG" 2>&1 ;;
    opencode) timeout 3300 opencode run -m "$model" "$msg" >> "$LOG" 2>&1 ;;
    devin) timeout 3300 "$DEVIN" -p --model "$model" --permission-mode dangerous --respect-workspace-trust false -- "$msg" >> "$LOG" 2>&1 ;;
  esac
  code=$?
  why=$(python $ROOT/scripts/cli_pool.py report "$pick" $code "$LOG" $offset $(( $(date +%s) - t0 )))
  echo "=== round $round ended code $code ($why) $(date +%H:%M)" >> "$LOG"
  sleep 20
done
