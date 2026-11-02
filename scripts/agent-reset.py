"""Reset agent CLIs to the SIR setup (Ahmed, 2026-11-02).

Stage config: back up each tool's global instruction file, then replace it with a short pointer to
D:/Projects/AGENTS.md and the premium bar. The master directive text (same as Claude's global
CLAUDE.md) is kept in _SIR/standard/00-master-directive.md so nothing is lost.
Stage codex-history: MOVE (never delete) Codex chat history to the backup folder.
Stage agy-history: MOVE Antigravity conversations and brain; needs Antigravity closed and enough free space on D:.

Usage: python agent-reset.py config | codex-history | agy-history
"""
import os, shutil, sys, datetime, subprocess

HOME = os.path.expanduser("~")
DAY = datetime.date.today().isoformat()
BACKUP = rf"D:\Projects\Backups\agent-history-{DAY}"
STD = r"D:\Projects\_SIR\standard"
MASTER = os.path.join(STD, "00-master-directive.md")

POINTER = """# Global rules ({tool})

Everything binding for this machine lives in the workspace, not in this file.

1. Read `D:\\Projects\\AGENTS.md` (workspace laws) and `D:\\Projects\\_SIR\\NEXT.md` at the start of every session.
2. In a project folder read that project's `AGENTS.md`, then `.sir/CHECKPOINT.md`, and continue from "Next step". "continue" means exactly this. Never redo finished work. Update the checkpoint after every finished step.
3. Code quality floor: `D:\\Projects\\_SIR\\standard\\23-premium-code-bar.md`. Weak-model playbook: `D:\\Projects\\_SIR\\plans\\WEAK_MODEL_PLAYBOOK.md`. Usage rules: `D:\\Projects\\_SIR\\plans\\USAGE_POLICY.md`.
4. Master production directive (full text): `D:\\Projects\\_SIR\\standard\\00-master-directive.md`. Its rules apply to every project.
5. No pull requests: commit and push straight to `main` once verify passes. Never delete `legacy\\`. AHome and Habiba data never leave AHome.
"""


def say(m):
    print(m, flush=True)


def backup_file(path, tag):
    if os.path.isfile(path):
        os.makedirs(os.path.join(BACKUP, "config"), exist_ok=True)
        dest = os.path.join(BACKUP, "config", tag)
        if not os.path.exists(dest):
            shutil.copy2(path, dest)


def config():
    codex_md = os.path.join(HOME, ".codex", "AGENTS.md")
    if not os.path.exists(MASTER):
        shutil.copy2(codex_md, MASTER)
        say("saved master directive -> " + MASTER)
    targets = {
        "codex": codex_md,
        "opencode": os.path.join(HOME, ".config", "opencode", "AGENTS.md"),
        "kilo": os.path.join(HOME, ".config", "kilo", "AGENTS.md"),
        "gemini": os.path.join(HOME, ".gemini", "GEMINI.md"),
    }
    for tool, path in targets.items():
        backup_file(path, f"{tool}-{os.path.basename(path)}")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(POINTER.format(tool=tool))
        say(f"pointer written: {path}")
    # the Gemini/Antigravity rules file named by the old GEMINI.md
    rules = os.path.join(HOME, ".gemini", "config", "GEMINI.md")
    backup_file(rules, "gemini-config-GEMINI.md")
    if os.path.isfile(rules):
        with open(rules, "w", encoding="utf-8", newline="\n") as f:
            f.write(POINTER.format(tool="antigravity"))
        say(f"pointer written: {rules}")


def move(src, rel):
    if not os.path.exists(src):
        return
    dest = os.path.join(BACKUP, rel)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    shutil.move(src, dest)
    say(f"moved {src} -> {dest}")


def codex_history():
    busy = subprocess.run(["tasklist"], capture_output=True, text=True).stdout.lower()
    if "codex.exe" in busy:
        say("Codex is running: close it first"); return
    base = os.path.join(HOME, ".codex")
    for name in ("sessions", "archived_sessions", "session_index.jsonl", "dictation-history", "transcription-history.jsonl"):
        move(os.path.join(base, name), os.path.join("codex", name))
    for name in os.listdir(base):
        if name.startswith(("state_5.sqlite", "thread_history_1.sqlite", "logs_2.sqlite", "goals_1.sqlite", "queue_1.sqlite")):
            move(os.path.join(base, name), os.path.join("codex", "db", name))
    os.makedirs(os.path.join(base, "sessions"), exist_ok=True)


def agy_history():
    busy = subprocess.run(["tasklist"], capture_output=True, text=True).stdout.lower()
    if "antigravity.exe" in busy:
        say("Antigravity is running: close it first"); return
    base = os.path.join(HOME, ".gemini", "antigravity")
    need = sum(os.path.getsize(os.path.join(r, f)) for d in ("conversations", "brain", "annotations")
               for r, _, fs in os.walk(os.path.join(base, d)) for f in fs)
    free = shutil.disk_usage("D:\\").free
    if free < need + 1.5 * 2**30:
        say(f"not enough space on D: need {need/2**30:.1f} GB + 1.5 GB reserve, free {free/2**30:.1f} GB"); return
    for name in ("conversations", "brain", "annotations", "conversation_summaries.db", "conversation_summaries.db-shm",
                 "conversation_summaries.db-wal", "agyhub_summaries_proto.pb"):
        move(os.path.join(base, name), os.path.join("antigravity", name))
    for name in ("conversations", "brain", "annotations"):
        os.makedirs(os.path.join(base, name), exist_ok=True)


if __name__ == "__main__":
    stage = sys.argv[1] if len(sys.argv) > 1 else ""
    {"config": config, "codex-history": codex_history, "agy-history": agy_history}.get(stage, lambda: say(__doc__))()
