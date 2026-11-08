"""Turn a brief into the exact text an operator types into a new Antigravity chat.

Usage: python agy-task.py <name> <brief-file> <cwd>
Writes D:/Projects/_SIR/ops/briefs/<name>.prompt.txt (the full prompt the chat reads) and prints its path.
The prompt ends with the report path and the completion command, so the manager is woken by the done marker (agy-watch.sh).
"""

import sys, pathlib

OUT = pathlib.Path("D:/Projects/_SIR/ops/briefs")
HEAD = (
    "You are a SIR worker for the SIR Manager. First read D:/Projects/AGENTS.md and "
    "D:/Projects/_SIR/standard/23-premium-code-bar.md. Work only in {cwd}. Follow the brief exactly, edit only the files "
    "it allows, run its done-when commands and fix until green. Write premium, current code: no placeholders, no invented "
    "data, all UI states. AHome and Habiba material never leaves local systems. Commit nothing unless the brief says so.\n\n"
    "BRIEF:\n"
)
TAIL = (
    "\n\nREPORT AND SIGNAL (always, even on failure or when blocked):\n"
    "1. Write your full report (everything you did and found, with file paths, commands and their real output, screenshots you took, "
    "what is unsure, what you recommend next; no shortening) to D:/Projects/_SIR/ops/agy-runs/reports/{name}.md\n"
    '2. Then use your terminal tool to run exactly: python D:/Projects/_SIR/scripts/agy-done.py {name} <ok|fail|blocked> "<one line: result>"\n'
    "3. Your final reply may be short; the report file is what the manager reads."
)


def main() -> int:
    if len(sys.argv) < 4:
        print(__doc__)
        return 2
    name, brief, cwd = sys.argv[1], pathlib.Path(sys.argv[2]), sys.argv[3]
    OUT.mkdir(parents=True, exist_ok=True)
    p = OUT / (name + ".prompt.txt")
    p.write_text(
        HEAD.format(cwd=cwd)
        + brief.read_text(encoding="utf-8")
        + TAIL.format(name=name),
        encoding="utf-8",
    )
    print(p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
