"""Run one Antigravity CLI worker on a written brief.

Usage: python agy-worker.py <name> <brief-file> <cwd> [timeout-seconds]
Writes the reply to D:/Projects/_SIR/ops/agy-runs/<name>.md and exits with agy's code.
The model id gemini-3.8-flash-high already carries the thinking level, so no --effort flag is passed.
"""

import subprocess, sys, pathlib, datetime

RUNS = pathlib.Path("D:/Projects/_SIR/ops/agy-runs")
PREAMBLE = (
    "You are a SIR worker for the SIR Manager. Read D:/Projects/AGENTS.md and "
    "D:/Projects/_SIR/standard/23-premium-code-bar.md first. Follow the brief exactly, edit only the files it allows, "
    "run its done-when commands, fix until green, commit nothing unless the brief says so, and end with a reply of at most "
    "15 lines: what changed, files, commands with results, anything unclear. No placeholders, no invented data. "
    "AHome and Habiba material never leaves local systems.\n\nBRIEF:\n"
)


def main() -> int:
    if len(sys.argv) < 4:
        print(__doc__)
        return 2
    name, brief, cwd = sys.argv[1], pathlib.Path(sys.argv[2]), sys.argv[3]
    timeout = int(sys.argv[4]) if len(sys.argv) > 4 else 1500
    RUNS.mkdir(parents=True, exist_ok=True)
    prompt = PREAMBLE + brief.read_text(encoding="utf-8")
    out = RUNS / (name + ".md")
    started = datetime.datetime.now().isoformat(timespec="seconds")
    proc = subprocess.run(
        [
            "agy",
            "--print",
            prompt,
            "--model",
            "gemini-3.8-flash-high",
            "--print-timeout",
            str(timeout) + "s",
            "--add-dir",
            cwd,
        ],
        cwd=cwd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    out.write_text(
        f"# agy run {name}\nstarted {started}, exit {proc.returncode}, cwd {cwd}\n\n## reply\n{proc.stdout}\n\n## stderr\n{proc.stderr[-2000:]}\n",
        encoding="utf-8",
    )
    return proc.returncode


if __name__ == "__main__":
    sys.exit(main())
