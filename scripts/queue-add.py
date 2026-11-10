"""Add a task to the autopilot queue. Usage: python queue-add.py <name> <brief.md> <project-folder> "<title>"
Builds ops/briefs/<name>.prompt.txt with agy-task.py and appends the task to ops/AUTOPILOT_QUEUE.json (skips a name already queued).
The autopilot (hq_autopilot.py) then gives it to the free CLI agents when its turn comes. Never queue AHome private content."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path("D:/Projects/_SIR")
QUEUE = ROOT / "ops" / "AUTOPILOT_QUEUE.json"


def main() -> int:
    if len(sys.argv) < 5:
        print(__doc__)
        return 2
    name, brief, folder, title = sys.argv[1:5]
    if not Path(brief).exists() or not Path(folder).is_dir():
        print("brief file or project folder not found")
        return 2
    subprocess.run([sys.executable, str(ROOT / "scripts/agy-task.py"), name, brief, folder], check=True)
    queue = json.loads(QUEUE.read_text(encoding="utf-8"))
    if any(t["name"] == name for t in queue):
        print("already queued:", name)
        return 0
    queue.append({"name": name, "folder": folder.replace("\\", "/"), "title": title, "done": False})
    QUEUE.write_text(json.dumps(queue, ensure_ascii=False, indent=2), encoding="utf-8")
    print("queued:", name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
