"""One screen: every AI tool under SIR management. Usage: python scripts/ai-status.py
Shows the autopilot heartbeat, the queue, running workers and agent processes, the model pool and the last lines of each active task log."""
import json
import re
import subprocess
import time
from pathlib import Path

OPS = Path("D:/Projects/_SIR/ops")
now = time.time()


def load(p):
    try:
        return json.loads(Path(p).read_text(encoding="utf-8"))
    except Exception:
        return {}


st = load(OPS / "autopilot_state.json")
print(f"autopilot heartbeat: {int((now - st.get('last_tick', 0)) / 60)} min ago (must be under 6)")
queue = load(OPS / "AUTOPILOT_QUEUE.json") or []
print("\nQUEUE")
for t in queue:
    if not t.get("done"):
        rs = st.get("runners", {}).get(t["name"], {})
        print(f"  open  {t['name']:18} {t['folder']}  runner pid {rs.get('pid', '-')}")
print(f"  done  {sum(1 for t in queue if t.get('done'))} tasks")
print("\nMODEL POOL (scripts/cli_pool.py)")
print(subprocess.run(["python", "D:/Projects/_SIR/scripts/cli_pool.py", "status"], capture_output=True, text=True).stdout)
out = subprocess.run(["powershell", "-NoProfile", "-Command",
    "Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -match 'kilo run|opencode run|devin.exe\"? -p|cli-run2' } | ForEach-Object { '{0} {1}' -f $_.ProcessId, $_.CommandLine.Substring(0,[Math]::Min(120,$_.CommandLine.Length)) }"],
    capture_output=True, text=True).stdout
print("RUNNING AGENT PROCESSES\n" + (out or "  none\n"))
for t in queue:
    if t.get("done"):
        continue
    log = OPS / "agy-runs" / f"cli-{t['name']}.log"
    if log.exists():
        text = log.read_text(encoding="utf-8", errors="ignore")
        rounds = re.findall(r"=== round \d+ [^\n]*", text)[-3:]
        print(f"LOG {t['name']} (last write {int((now - log.stat().st_mtime) / 60)} min ago)")
        for r in rounds:
            print("  " + r[:120])
