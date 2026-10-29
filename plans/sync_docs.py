r"""One-shot sync of the docs that must agree with each other after the 2026-10-30 reorganization.
Run: python D:/Projects/_SIR/plans/sync_docs.py   (idempotent)
"""
import io
import os
import re

SIR = "D:/Projects/_SIR"
WS = "D:/Projects/AGENTS.md"


def rd(p):
    return io.open(p, encoding="utf-8").read()


def wr(p, t):
    io.open(p, "w", encoding="utf-8", newline="\n").write(t)


# 1. workspace AGENTS.md: portfolio map and laws
t = rd(WS)
start = t.index("## Portfolio map")
end = t.index("## Parallel work and locks")
portfolio = r"""## Portfolio map (everything lives inside `D:\Projects`; create nothing outside it, except the Desktop shortcut folders and `D:\Projects\Backups` for private backups)
Every product is a NEW project whose name starts with SIR. Merged products contain their old projects under `legacy\` (a MERGE project: port everything, then move `legacy\*` to `old projects\` at M6).
SIR Platform (shared kit) · SIR Obour Hub · SIR Hagoozat (+Hagoozat Elite, 11Players, EGFootball5) · SIR Business (+Restaurant, Market, Pharmacy, Library) · SIR Content Creation Studio · SIR Controller (+Optimizer) · SIR AI · SIR Laptop Manager (+agent suite, Laptop manager) · AHome (private home project of Ahmed and Habiba, keeps its own name, not a SIR product) · SIR Jobs (data in `Jobs`) · SIR Study (study folder merged in `materials\`) · SIR Negm Furniture (client brand) · SIR ModPack · SIR Mods for GTA V · SIR Odysseus · SIR Life · SIR Portfolio (Ahmed's public site).
Still at the top level for a reason: `AHome` (its daemons run), `Laptop manager` (runs routines and RAG), `Jobs` (personal data), `SIR AI` and `SIR Optimizer` (apps were running), `Obour Academic Hub` (locked), `AI_Models_Hub` (model store), `sirahmed8` (GitHub profile repo), `old projects`, `_SIR`. The plan for each is `_SIR\plans\<slug>.md`; facts per project: `_SIR/ops/PORTFOLIO.md`.

"""
t = t[:start] + portfolio + t[end:]
if "Create nothing outside" not in t:
    t = t.replace("- No budget:", "- Keep everything inside `D:\\Projects`. Quarantine goes in `<project>\\_quarantine\\` (gitignored), never in a new top-level folder. Icons: every product has a unique icon (agy-generated logo when available) on its folder in `D:\\Projects` and its Desktop folder.\n- No budget:", 1)
wr(WS, t)
wr(SIR + "/core/workspace-AGENTS.md", t)

# 2. old quarantine path in phase files
for root, _, files in os.walk(SIR):
    if ".claude" in root or "plans" in root:
        continue
    for f in files:
        if f.endswith(".md"):
            p = os.path.join(root, f)
            x = rd(p)
            y = x.replace("D:\\Quarantine\\<date>\\", "`<project>\\_quarantine\\<date>\\` (inside D:\\Projects)")
            if y != x:
                wr(p, y)

# 3. START_HERE: add the new files to the program block
s = rd(SIR + "/START_HERE.md")
if "AGENT_PROTOCOL" not in s:
    s = s.replace(
        "Never ask Ahmed; run Tier 0-1 work yourself; keep replies short.",
        "Also read `plans/AGENT_PROTOCOL.md` (how every AI works: read order, clean-architecture contract, folder layout, evidence, what to do when blocked) and `plans/TIMELINE.md` (target dates). Merged products hold their old projects in `legacy\\`: they are MERGE projects. Icons: `scripts/generate-icons-agy.ps1` then `scripts/make-icons-and-desktop.ps1`. Everything lives inside `D:\\Projects`. Never ask Ahmed; run Tier 0-1 work yourself; keep replies short.",
        1,
    )
    wr(SIR + "/START_HERE.md", s)

# 4. REQUIREMENTS: new rows
r = rd(SIR + "/REQUIREMENTS.md")
if "R-100" not in r:
    r = r.rstrip("\n") + r"""
| R-100 | Rebuild every product from the start as a new SIR-named project with its own Firebase and Cloudflare project; old projects may stop working | `plans/MASTER_REBUILD_PLAN.md` | 🔄 | 17 plans + 17 folders created 2026-10-30; no product built yet |
| R-101 | Merge same-idea projects into one folder (old code, git history and structure moved into `legacy\`) so one AI can finish the product; move `legacy\*` to `old projects\` at M6 | `scripts/merge-legacy.ps1`, plans section 0 | 🔄 | 13 old folders merged; SIR Optimizer and Obour Academic Hub locked (re-run script) |
| R-102 | Every plan, prompt and start file lets any AI know what is done, next and how to work | `plans/AGENT_PROTOCOL.md`, `.sir/PLAN.md`, NEXT.md | 🔄 | generated from `plans/products_*.py` |
| R-103 | Unique AI-generated professional icon per product, on the D: folder and the Desktop folder, with open / start dev / stop dev shortcuts | `scripts/generate-icons-agy.ps1`, `make-icons-and-desktop.ps1` | 🔄 | placeholders (monograms) in place; agy launch blocked by the classifier, Ahmed runs the script |
| R-104 | Company/publisher name SIR on stores and accounts | `plans/MASTER_REBUILD_PLAN.md` addendum | ⬜ | needs a legal entity decision (owner) |
| R-105 | Personal portfolio site (SIR Portfolio), best site, no personal info | `plans/sir-portfolio.md` | ⬜ | planned, wave 2 |
| R-106 | Study automation: lectures, deadlines, organization (never graded work) | `plans/sir-study.md` | 🔄 | study folder merged into SIR Study; scripts quarantined in `SIR Study\_quarantine` |
| R-107 | Jobs and money agent | `plans/sir-jobs.md` | ⬜ | planned, wave 4 |
| R-108 | Organize GitHub repos: new private SIR repos, archive (never delete) old ones after the PRs merge | `scripts/github-organize.ps1` | 🔄 | 10 new repos created; archive step waits for the merges |
| R-109 | Nothing created outside D:\Projects | `D:\Projects\AGENTS.md` law | ✅ | quarantine moved into SIR Study |
"""
    wr(SIR + "/REQUIREMENTS.md", r)

# 5. product prompts mention the merge
from_plans = os.path.join(SIR, "plans")
import sys
sys.path.insert(0, from_plans)
from generate_plans import MERGE  # noqa: E402
from products import PRODUCTS  # noqa: E402
for p in PRODUCTS:
    f = os.path.join("D:/Projects", p["folder"], "prompts", "PRODUCT_PROMPT.md")
    if p["slug"] in MERGE and os.path.isfile(f):
        t = rd(f)
        if "MERGE PROJECT" not in t:
            wr(f, t + "\nMERGE PROJECT: the old projects are inside `legacy/` (or `materials/`). Port everything of value into a clean new structure, fully configured, deployed and pushed in production mode, then move `legacy/*` to `D:/Projects/old projects/`. See `.sir/PLAN.md` section 0.\n")
print("docs synced")
