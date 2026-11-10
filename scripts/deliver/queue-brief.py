"""Print the autopilot work queue in simple Arabic (used by the Telegram button "queue" and /queue)."""
import json
import sys
import time
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
OPS = Path("D:/Projects/_SIR/ops")


def load(name: str, default):
    try:
        return json.loads((OPS / name).read_text(encoding="utf-8"))
    except Exception:
        return default


queue = load("AUTOPILOT_QUEUE.json", [])
state = load("autopilot_state.json", {})
lines = ["[الإدارة] قايمة الشغل:"]
current_seen = False
for task in queue:
    if task.get("done"):
        mark = "خلصت"
    elif not current_seen:
        mark = "شغالة دلوقتي"
        current_seen = True
    else:
        mark = "مستنية دورها"
    lines.append(f"- {task.get('title', task['name'])}: {mark}")
if not queue:
    lines.append("- مفيش مهام في القايمة.")
tick = state.get("last_tick")
if tick:
    lines.append(f"آخر فحص من الطيار الآلي: من {int((time.time() - tick) / 60)} دقيقة.")
if state.get("paused_for_game"):
    lines.append("الشغل واقف مؤقتا لأن فيه لعبة شغالة.")
print("\n".join(lines))
