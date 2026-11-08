"""Handoff projects go to someone else: no Ahmed-specific paths, tools or rules in the files they pull."""

import io
import os
import re
import shutil

NL = chr(10)
FILES = (
    ".sir/TASKS.md",
    ".sir/BOARD.md",
    ".sir/PLAN.md",
    ".sir/ARCHITECTURE.md",
    ".sir/PRODUCTION.md",
    ".sir/QUALITY.md",
    ".sir/DESIGN.md",
    ".sir/BENCHMARK.md",
    ".sir/PLATFORMS.md",
    ".sir/project.yml",
)


def sanitize(s):
    s = NL.join(
        ln
        for ln in s.split(NL)
        if "Wire the Desktop shortcuts" not in ln and "Desktop/SIR Projects" not in ln
    )
    s = re.sub(r"owner: [a-z-]+", "owner: agent", s)
    s = s.replace(
        "Read `_SIR/NEXT.md` and `_SIR/plans/MASTER_REBUILD_PLAN.md` first.",
        "Read `HANDOFF.md` first.",
    )
    s = s.replace("created by Ahmed ", "pre-created ")
    s = s.replace(
        "Ahmed's repo access is kept or removed as the friend decides",
        "the previous maintainer's repo access is kept or removed as the owner decides",
    )
    s = s.replace("Ahmed Alaa (@sirahmed8)", "the project owner")
    s = s.replace(
        "Never ask Ahmed; if blocked by a permission, write the single command in `NEXT.md` and continue with the next box.",
        "If something needs the owner, write the single remaining step in the checkpoint and continue with the next task.",
    )
    s = s.replace("Ahmed", "the previous maintainer")
    s = s.replace(
        "the SIR Platform `ai-proxy` (or local models for private apps)",
        "a server-side AI proxy",
    )
    s = re.sub(r" \((?:SIR Platform )?`[a-z-]+`\)", "", s)
    s = s.replace("SIR Platform", "the shared kit").replace(" (module 22)", "")
    s = re.sub(
        r"\n- Owner/admin only from a server-verified Firebase ID token[^\n]*",
        "\n- Owner and admin checks happen only on the server.",
        s,
    )
    s = s.replace(
        "Read this file, then `.sir/CHECKPOINT.md`",
        "Read `HANDOFF.md`, this file, then `.sir/CHECKPOINT.md`",
    )
    s = re.sub(
        r"## 0\. THIS IS A MERGE PROJECT.*?(?=\n## 1\.)",
        "## 0. Handoff project\nThe earlier version of the site is in `reference-source/` (read-only reference). Port everything of value into a clean new structure with premium code, then set it up and host it on the owner's own accounts (`docs/CLIENT_SETUP.md`).\n",
        s,
        flags=re.S,
    )
    return s


def client_cleanup(folder, p, w, here):
    tpl = (
        io.open(os.path.join(here, "client_agents_template.md"), encoding="utf-8")
        .read()
        .replace("{display}", p["display"])
    )
    w(os.path.join(folder, "AGENTS.md"), tpl)
    w(
        os.path.join(folder, "GEMINI.md"),
        "See AGENTS.md. Follow it and docs/AGENT_PLAYBOOK.md for every task.",
    )
    for rel in (".claude", "prompts", ".sir/TEAM.md", ".sir/TOOLKIT.md", ".sir/inbox"):
        path = os.path.join(folder, rel)
        if os.path.isdir(path):
            shutil.rmtree(path, ignore_errors=True)
        elif os.path.isfile(path):
            os.remove(path)
    for rel in FILES:
        fp = os.path.join(folder, rel)
        if os.path.isfile(fp):
            io.open(fp, "w", encoding="utf-8", newline=NL).write(
                sanitize(io.open(fp, encoding="utf-8").read())
            )
    w(
        os.path.join(folder, ".sir", "CHECKPOINT.md"),
        "# CHECKPOINT: "
        + p["display"]
        + NL
        + "Handoff pack ready. Next step: read HANDOFF.md, then follow FRIEND_AGENT_PROMPT.md (analyse, improve the plan, build task by task).",
    )
