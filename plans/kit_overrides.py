"""Overrides applied on top of kit_products_a/b after Ahmed's 2026-11-01 decisions. generate_kit.py calls apply(DATA)."""

SHARED = (
    "Keep owner-auth, signed-webhook, billing fallback (Launching Soon), ai-proxy, legal pack and design tokens/UI in separate internal packages (`packages/*`) with their own tests and READMEs, "
    "because the shared kit is built last by extracting and unifying them; write each reusable piece into `D:/Projects/_SIR/old projects/SIR Platform-plans-from-SIR/sir-platform-bus.md` when it is done"
)


def add(d, slug, ms, text):
    d[slug].setdefault("tasks", {}).setdefault(ms, []).append(text)


def apply(D):
    # automations
    D["sir-study"]["modules"] += [
        "guides: one HTML study guide per subject, start to final, regenerated on every new upload",
        "portal-reader: read-only digest of uploads, deadlines, quiz and assignment dates through Ahmed's own signed-in Chrome",
        "practice: mock quizzes in the real format, explained answers, weak-topic tracking, 15/30/60 minute plans",
    ]
    add(
        D,
        "sir-study",
        "M1",
        "Per-subject study guide: one HTML file per subject (`guides/<subject>.html`) built from the lectures start to final: lesson summaries, key terms, worked examples, flashcards, self-test questions with answers, formula or code sheets, an exam map; regenerated on every new upload so it is always current",
    )
    add(
        D,
        "sir-study",
        "M1",
        "Portal reader (read-only): Ahmed signs in to https://elearning.oi.edu.eg once in Chrome (agents never type his password); the agent reads new uploads, deadlines and quiz and assignment dates into the plan and the guides",
    )
    add(
        D,
        "sir-study",
        "M2",
        "Practice mode: mock quizzes in the real quiz format built from the lectures and past material, every answer explained, weak topics tracked, daily plan sized to 15, 30 or 60 minutes that covers the next quiz and assignment first",
    )
    add(
        D,
        "sir-study",
        "M2",
        "Assignment help: explain what is asked, show a worked example with different numbers, give hints in steps; Ahmed writes the final answer (agents never submit or complete graded work or mark it done)",
    )
    D["sir-laptop-manager"]["modules"] += [
        "look: Windhawk mods and scripts Ahmed already downloaded, improved and extended so Windows looks and feels like macOS (menu bar, dock, rounded corners, blur, motion, icons, fonts with licence check), always with a restore point"
    ]
    add(
        D,
        "sir-laptop-manager",
        "M0",
        "Find the Windhawk mods and scripts Ahmed already downloaded (Windhawk folders, Downloads, Documents), inventory each one, review safety and licence",
    )
    add(
        D,
        "sir-laptop-manager",
        "M1",
        "Make every downloaded Windhawk mod and script 100x better: fix, tidy, configure, document, and add a one-click restore script (`restore-look.ps1`) before changing anything; verify each with screenshots through computer use",
    )
    add(
        D,
        "sir-laptop-manager",
        "M2",
        "Write new Windhawk mods and scripts that make the laptop look like macOS and look better overall (menu bar, dock, window chrome, animations, wallpaper and icon sets, blur, sounds); use computer use to check every change on screen; keep each mod small, tested and reversible",
    )
    add(
        D,
        "sir-ai",
        "M0",
        "Odysseus reference: `legacy/Odysseus app` is an AGPL upstream-derived AI workspace moved here on 2026-11-01; read it for ideas (chat, agents, research, documents, mail, notes, calendar) and benchmark against it; never copy its code into SIR AI",
    )
    # friend's project
    D["sir-negm-furniture"]["modules"] += [
        "handoff: HANDOFF.md, docs/CLIENT_SETUP.md, FRIEND_AGENT_PROMPT.md and docs/AGENT_PLAYBOOK.md so the friend's own AI agent (Antigravity, Gemini high) can build, set up and host everything on the friend's accounts"
    ]
    add(
        D,
        "sir-negm-furniture",
        "M0",
        "No accounts for this project are created by Ahmed: no Firebase, Cloudflare or GitHub organization. The repo `sir-negm-furniture` (private) is the delivery channel; the friend pulls it and creates his own accounts with the agent's help",
    )
    add(
        D,
        "sir-negm-furniture",
        "M0",
        "Complete the handoff pack in the repo (HANDOFF.md, docs/CLIENT_SETUP.md, FRIEND_AGENT_PROMPT.md, docs/AGENT_PLAYBOOK.md) and keep it current as the plan improves; write for a weaker model: short explicit steps, checklists, exact commands, verification after every step",
    )
    # shared concerns before Platform
    for s in (
        "sir-education-hub",
        "sir-hagoozat",
        "sir-business",
        "sir-content-creation-studio",
        "sir-ai",
        "sir-life",
        "sir-modpack",
        "sir-mods-for-gta-v",
        "sir-controller",
    ):
        add(D, s, "M0", SHARED)
    add(
        D,
        "sir-portfolio",
        "M0",
        "Built last on purpose: show only finished products with real status, real screenshots and real links; collect them from `ops/PORTFOLIO.md` and each product's `.sir/status.json`",
    )
