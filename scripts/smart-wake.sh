#!/usr/bin/env bash
# Wake the manager when something big happens, or at the latest after MAX seconds (default 7200). Prints one summary and exits.
# Big = a new done marker (a project finished a cycle), a done marker with fail/blocked, new commits pushed to any project,
# a GitHub 'verify' run that failed, a message from Ahmed on Telegram, or a chat reporting quota. Debounce: waits QUIET seconds
# after the first event so one summary covers a burst.
MAX=${1:-7200}; QUIET=${2:-240}
P=/d/Projects
DONE=$P/_SIR/ops/agy-runs/done
INBOX=$P/_SIR/ops/bus/ahmed-telegram.md
REPOS="AHome:sirahmed8/ahmed-and-habiba|SIR Study:sirahmed8/sir-study|SIR Jobs:sirahmed8/sir-jobs|SIR Laptop Manager:sirahmed8/sir-laptop-manager|SIR Negm Furniture:sirahmed8/sir-negm-furniture|_SIR:sirahmed8/sir-hq"
declare -A head0
IFS='|' read -ra R <<< "$REPOS"
for r in "${R[@]}"; do d="${r%%:*}"; head0["$d"]=$(git -C "$P/$d" rev-parse origin/main 2>/dev/null); done
done0=$(ls "$DONE" 2>/dev/null | grep -v '^hello' | sort | md5sum | cut -c1-8)
list0=$(ls "$DONE" 2>/dev/null | sort)
inbox0=$(wc -l < "$INBOX" 2>/dev/null || echo 0)
start=$(date +%s); first=0; ev=""; tick=0; stall_alert=0
last_activity() { a=$(find "$P/_SIR/ops/agy-runs/reports" -type f -printf '%T@
' 2>/dev/null | sort -n | tail -1 | cut -d. -f1); for r in "${R[@]}"; do d="${r%%:*}"; c=$(git -C "$P/$d" log -1 --format=%ct 2>/dev/null); [ -n "$c" ] && [ "${c:-0}" -gt "${a:-0}" ] && a=$c; done; echo "${a:-0}"; }
add() { ev="$ev$1"$'\n'; [ "$first" -eq 0 ] && first=$(date +%s); }
while true; do
  now=$(date +%s)
  # new done markers
  list=$(ls "$DONE" 2>/dev/null | sort)
  new=$(comm -13 <(echo "$list0") <(echo "$list") | grep -v '^hello')
  for f in $new; do add "DONE: $f $(sed 's/.*"status": "//; s/", "summary": "/ | /; s/", "at".*//' "$DONE/$f" | cut -c1-200)"; done
  list0="$list"
  # Ahmed's Telegram messages
  inbox=$(wc -l < "$INBOX" 2>/dev/null || echo 0)
  if [ "$inbox" -gt "$inbox0" ]; then add "AHMED TELEGRAM: $(tail -n $((inbox-inbox0)) "$INBOX" | cut -c1-300)"; inbox0=$inbox; fi
  # pushed commits (every ~60 s) and CI failures (every ~5 min)
  if [ $((tick % 2)) -eq 0 ]; then
    for r in "${R[@]}"; do d="${r%%:*}"; h=$(git -C "$P/$d" rev-parse origin/main 2>/dev/null)
      if [ -n "$h" ] && [ "$h" != "${head0[$d]}" ]; then n=$(git -C "$P/$d" rev-list --count "${head0[$d]}..$h" 2>/dev/null); add "PUSH: $d +$n commits ($(git -C "$P/$d" log -1 --format=%s "$h" | cut -c1-80))"; head0["$d"]=$h; fi
    done
  fi
  if [ $((tick % 10)) -eq 5 ]; then
    for r in "${R[@]}"; do d="${r%%:*}"; repo="${r##*:}"
      c=$(gh run list -R "$repo" --limit 1 --json conclusion,headSha -q '.[0] | "\(.conclusion) \(.headSha[0:7])"' 2>/dev/null)
      case "$c" in failure*) key="$d $c"; if ! grep -qx "$key" /tmp/smartwake_seen 2>/dev/null; then echo "$key" >> /tmp/smartwake_seen; add "CI FAILED: $d ($c)"; fi;; esac
    done
  fi
  if [ $((tick % 20)) -eq 10 ]; then la=$(last_activity); idle=$((now-la)); if [ "$idle" -gt 2100 ] && [ $((now-stall_alert)) -gt 2400 ]; then stall_alert=$now; add "STALL: no commit or report for $((idle/60)) minutes (check Antigravity quota and rotate the account per ops/ACCOUNT_ROTATION.md, then nudge the chats)"; fi; fi
  tick=$((tick+1))
  if [ "$first" -ne 0 ] && [ $((now-first)) -ge "$QUIET" ]; then echo "SMART WAKE ($(date +%H:%M)): big events"; printf '%s' "$ev"; exit 0; fi
  if [ $((now-start)) -ge "$MAX" ]; then echo "SMART WAKE ($(date +%H:%M)): max wait reached, routine check"; printf '%s' "$ev"; exit 0; fi
  sleep 30
done
