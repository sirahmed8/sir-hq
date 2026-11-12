"""Per-project round labels for the owner: AHome R1..R7, Jobs R1..R12 (instead of global numbers like r46).
Rounds are R1.. in queue order per project, self-audits A1.., CI fixes F1... Writes ops/ROUND_LABELS.md and ops/round_labels.json."""
import json
import re
import time
from pathlib import Path

import nowindow  # noqa: F401

ROOT = Path("D:/Projects/_SIR")
SHORT = {"AHome": "AHome", "SIR Jobs": "Jobs", "SIR Study": "Study", "SIR Laptop Manager": "Laptop",
         "SIR AI": "SIR AI", "SIR Portfolio": "Portfolio", "_SIR": "HQ"}


def verification(name: str) -> str:
    f = ROOT / "ops" / "verifications" / f"{name}.md"
    if not f.exists():
        return "not verified"
    m = re.search(r"Overall:\s*(PASS|FAIL)", f.read_text(encoding="utf-8", errors="ignore"))
    return m.group(1) if m else "not verified"


def main() -> None:
    q = json.loads((ROOT / "ops" / "AUTOPILOT_QUEUE.json").read_text(encoding="utf-8"))
    tasks = q if isinstance(q, list) else q.get("tasks", q)
    counters: dict = {}
    rows = []
    for t in tasks:
        proj = SHORT.get(t["folder"].rstrip("/").split("/")[-1], t["folder"].rstrip("/").split("/")[-1])
        kind = "A" if t["name"].startswith("audit-") else "F" if t["name"].startswith("ci-") or t["name"].endswith("-fix1") else "R"
        counters[(proj, kind)] = counters.get((proj, kind), 0) + 1
        label = f"{proj} {kind}{counters[(proj, kind)]}"
        state = "done by worker" if t.get("done") else "open"
        rows.append({"label": label, "task": t["name"], "title": t.get("title", ""), "state": state,
                     "verified": verification(t["name"]) if t.get("done") else ""})
    (ROOT / "ops" / "round_labels.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    lines = [f"# Round labels (generated {time.strftime('%Y-%m-%d %H:%M')})", "",
             "R = round, A = self-audit, F = fix. Numbers restart per project. The old global task id is in the second column.", "",
             "| Label | Task id | State | Verified | Title |", "|---|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r['label']} | {r['task']} | {r['state']} | {r['verified']} | {r['title'][:70]} |")
    (ROOT / "ops" / "ROUND_LABELS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    summary = {}
    for r in rows:
        proj, kind_n = r["label"].rsplit(" ", 1)
        if kind_n.startswith("R"):
            s = summary.setdefault(proj, {"R": 0, "done": 0, "PASS": 0, "FAIL": 0})
            s["R"] += 1
            s["done"] += r["state"] != "open"
            s["PASS"] += r["verified"] == "PASS"
            s["FAIL"] += r["verified"] == "FAIL"
    for proj, s in summary.items():
        print(f"{proj}: R1-R{s['R']} ({s['done']} done by workers, {s['PASS']} verified PASS, {s['FAIL']} FAIL)")


if __name__ == "__main__":
    main()
