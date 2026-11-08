import io
import re

SIR = "D:/Projects/_SIR"

state = """## State of the folders (2026-10-30, after the merge)
- D:/Projects now holds ONLY: the SIR product folders, AHome (private, own name), AI_Models_Hub (model store), Android and Backups (you moved them in), old projects, _SIR, and the three auto-read rule files AGENTS.md / CLAUDE.md / GEMINI.md (Claude, Codex and Gemini read these automatically in every chat started in D:/Projects, so they stay).
- Every old project lives INSIDE its new product as legacy/: SIR Hagoozat (Hagoozat Elite, 11Players, EGFootball5) · SIR Business (Restaurant, Market, Pharmacy, Library) · SIR Controller (v1, Optimizer) · SIR Laptop Manager (Laptop manager, agent suite) · SIR Obour Hub (Obour Academic Hub) · SIR AI (SIR AI v1, SIR Tele Gateway) · SIR Portfolio (sirahmed8 profile repo) · SIR Jobs (Jobs data) · SIR Content Creation Studio, SIR ModPack, SIR Mods for GTA V, SIR Negm Furniture, SIR Odysseus (their v1). SIR Study holds the old Obour Institute study folder in materials/ and the Moodle scripts in _quarantine/.
- AHome is NOT a SIR product: private project of Ahmed and Habiba, keeps its name, services run from D:/Projects/AHome (port 8090 verified), plan in AHome/.sir/PLAN.md.
- One empty leftover: D:/Projects/Laptop manager (an empty shell; Ahmed's open Laptop manager chat sits in it; it disappears when that chat is closed or any agent can delete it then).
- Old SIR AI app and SIR PowerSync were stopped at Ahmed's request. A duplicate whisper cache is in AI_Models_Hub/_whisper_duplicate_from_restore.
- INCIDENT (fixed, nothing lost): a bug in merge-legacy.ps1 moved parts of D:/Projects into a legacy folder; restored with scripts/restore-misplaced.ps1 + restore-finish.ps1; the bug is fixed (a missing alias no longer resolves to the Projects folder).
- Handy: scripts/who-holds.ps1 lists the programs that keep a folder from moving (agents run it themselves; Ahmed never has to look).
- GitHub: new private repos created for most products; old repos get renamed sir-legacy-* and archived by scripts/github-organize.ps1 AFTER the 5 PRs are merged; then re-run github-create-new-repos.ps1 for Content Creation Studio, Controller, ModPack, GTA mods.
"""

s = io.open(SIR + "/NEXT.md", encoding="utf-8").read()
a = s.index("## State of the folders")
b = s.index("## Next, in this order")
s = s[:a] + state + "\n" + s[b:]
a = s.index("## Only Ahmed can do")
only = """## Only Ahmed can do (the agents already prepared the command)
1. Make the AI logos: pwsh -NoProfile -File D:/Projects/_SIR/scripts/generate-icons-agy.ps1 (the safety check blocks agents from launching agy; icons are temporary letters until you run it).
2. Merge the 5 security fixes: pwsh -NoProfile -File D:/Projects/_SIR/scripts/merge-approved-prs.ps1 (the safety check blocks agents from merging). Agents then run github-organize.
3. Accounts and decisions only you can do: move passwords out of the TickTick notes into a password manager; change the Moodle password; be logged in to Google AI Studio and OpenRouter in Chrome when asked; decide the company/publisher entity SIR for the stores.
Everything else (finding locks, stopping old programs, moving folders, fixing scripts) is done by the agents themselves.
"""
s = s[:a] + only
io.open(SIR + "/NEXT.md", "w", encoding="utf-8", newline="\n").write(s)

p = SIR + "/ops/HQ_CHECKPOINT.md"
c = io.open(p, encoding="utf-8").read()
add = (
    "**00000. 2026-10-30 FINAL MERGE STATE: read NEXT.md ('State of the folders'). All old projects are inside their new SIR product as legacy/; AHome is separate and keeps its name; "
    "Quarantine, START_HERE copy and mission zip are inside Projects/_SIR; Android and Backups were moved by Ahmed into D:/Projects (env vars and docs repointed). "
    "Exact next steps: (1) agents: key rotation in Chrome, fix failing Actions, github-organize after Ahmed runs merge-approved-prs.ps1; (2) SIR Platform M0; (3) per plans/TIMELINE.md. "
    "Open: icons are letters until Ahmed runs generate-icons-agy.ps1; empty Laptop manager shell. Re-read: NEXT.md, plans/MASTER_REBUILD_PLAN.md, plans/AGENT_PROTOCOL.md, plans/PROGRESS.md.**\n"
)
c = c.replace("## Next step\n", "## Next step\n" + add, 1)
io.open(p, "w", encoding="utf-8", newline="\n").write(c)
io.open(SIR + "/ops/MISSION_LOG.md", "a", encoding="utf-8", newline="\n").write(
    "- 2026-10-30 late · HQ · Final merge pass: Laptop manager (+.git) into SIR Laptop Manager, SIR AI v1 + SIR Tele Gateway into SIR AI/legacy, AHome restored to its own folder (not a SIR product) with daemons repointed and verified, SIR Home plan folder retired, D:/Quarantine, START_HERE copy and mission zip moved into Projects/_SIR, Android SDK variables and doc paths repointed after Ahmed moved D:/Android and D:/Backups into D:/Projects. Used who-holds.ps1 to find what locks folders (Claude Desktop git helpers and tool servers of an open chat).\n"
)
print("state written")
