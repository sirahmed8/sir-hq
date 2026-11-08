"""Create ops/briefs/loop-<slug>.md and its prompt for each project from plans/PERPETUAL_LOOP.md.

Usage: python make-loop-briefs.py [lens-number]
Writes the brief files and runs agy-task.py for each so the prompts are ready to type into new chats.
"""

import pathlib, subprocess, sys

LENSES = [
    "pixel-level polish",
    "motion and animation",
    "UX friction",
    "the five UI states",
    "accessibility",
    "responsiveness and zoom",
    "copy and bilingual correctness",
    "security and privacy",
    "performance",
    "code quality and tests",
    "data integrity and offline",
    "benchmark against the best apps",
]
PROJECTS = {
    "ahome": (
        "D:/Projects/AHome",
        "Private app of Ahmed and Habiba. Use dummy data only; never copy personal text into code, tests, logs or reports; local models for any AI feature; nothing deployed or pushed by you.",
    ),
    "study": (
        "D:/Projects/SIR Study",
        "Study aids only (guides, practice, hints). Never solve graded assignments or quizzes. Next exams: SAD 09/11, OR 10/11 (Cairo). Check every guide opens and reads well on a phone.",
    ),
    "jobs": (
        "D:/Projects/SIR Jobs",
        "Real paid work only: every link live, no scams, eligible from Egypt, honest skills, drafts never sent (sending speaks as the owner).",
    ),
    "laptop": (
        "D:/Projects/SIR Laptop Manager",
        "Never change system or security settings; restore point and dry run first; Windhawk mods are inventoried and improved in a copy before anything is installed.",
    ),
}
BASE = pathlib.Path("D:/Projects/_SIR")


def main() -> int:
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    lens = LENSES[n % len(LENSES)]
    (BASE / "ops/briefs").mkdir(parents=True, exist_ok=True)
    for slug, (cwd, rule) in PROJECTS.items():
        text = (
            "Use all your skills and tools: plan, sub-agents for independent parts, browser and computer-use tools to see the real result.\n\n"
            f"Task: run the perpetual improvement loop on {cwd}. Read D:/Projects/_SIR/plans/PERPETUAL_LOOP.md completely first and follow it exactly.\n"
            f"This cycle's main lens: {lens}. Still look at everything else you notice on the way.\n"
            f"Project rule: {rule}\n"
            "You are a real senior engineer and designer, not an instruction follower. Find problems nobody told you about and fix them at the root, "
            "with a test and a before/after screenshot. Do not stop early: only the usage limit, three finished cycles, or a true blocker ends your work. "
            "Commit locally in small commits; do not push.\n"
            f"Done when: cycle report written with a 'Found without being told' section, checkpoint and TASKS.md updated, next lens named.\n"
        )
        b = BASE / f"ops/briefs/loop-{slug}.md"
        b.write_text(text, encoding="utf-8")
        subprocess.run(
            [
                sys.executable,
                str(BASE / "scripts/agy-task.py"),
                f"loop-{slug}-{n}",
                str(b),
                cwd,
            ],
            check=True,
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
