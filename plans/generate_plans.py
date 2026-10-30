"""Builds plans/<slug>.md for every product from plans/products.py data plus the common sections below.
Run: python D:/Projects/_SIR/plans/generate_plans.py
Also writes the plan into <folder>/.sir/PLAN.md when the NEW folder already exists and is empty of code.
"""
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from products import PRODUCTS  # noqa: E402

PROJECTS = "D:/Projects"

COMMON_SECURITY = """- Owner/admin only from a server-verified Firebase ID token (JWKS) plus OWNER_EMAILS / OWNER_UIDS; email path needs email_verified; fail closed when unset (SIR Platform `owner-auth`).
- Every webhook: HMAC over the raw body with the timestamp inside the signed payload, timing-safe compare, idempotent activation (SIR Platform `signed-webhook`).
- No AI key, token or secret in any client bundle or git; AI only through the server proxy with per-user quota; owner unmetered (SIR Platform `ai-proxy`).
- Sessions in HttpOnly + Secure + SameSite=Strict cookies, never localStorage. Rate limits on login/register/reset. Input validated with zod at every boundary.
- Firestore/D1 rules deny by default, per-user/per-tenant claims, tested in the emulator. CSP with nonces, no unsafe-eval.
- gitleaks in CI and pre-commit; dependency audit; licence audit (no GPL/AGPL in proprietary code)."""

COMMON_UX = """Every screen implements the 5 states: first use, loading skeleton matching the final layout, empty (one clear action), error (human message + Retry), populated (paginated or virtualized, fine with 1,000+ items). Arabic RTL (CSS logical properties) + English + Simplified Chinese + Hindi; light, dark, system and high-contrast themes; keyboard shortcuts; 320 px to 4K; zoom 80%-200%; spring motion with a reduced-motion path; WCAG 2.2 AA. Own colour seed and icon; the same Profile and Settings screens as every SIR product."""

MILESTONES = """### M0 Foundations
- [ ] Create the folder from `plans/MASTER_REBUILD_PLAN.md` naming rules; `git init`, private GitHub repo `sirahmed8/{repo}`.
- [ ] `.sir/` file set (project.yml, CHECKPOINT.md, BOARD.md) from `standard/project-templates.md`; AGENTS/CLAUDE/GEMINI from `standard/agent-files.md`.
- [ ] New Firebase project `{firebase}` (Auth Google, Firestore) and Cloudflare project; OAuth app name "{display}", logo, support email.
- [ ] Login brand check: sign in with Google in a real browser; the screen must not show a Firebase project id; screenshot saved in `.sir/evidence/`.
- [ ] CI: typecheck, lint, test, build, gitleaks on every push; first green run.
### M1 Core slice
{m1}
### M2 Parity with the old project
{m2}
### M3 Security, legal, billing
- [ ] Security checklist above is green with tests (forged cookie, unsigned webhook, unverified email, cross-tenant read all fail).
- [ ] Legal pack generated from what the product really collects; cookie banner with equal Reject; account and data deletion flow.
- [ ] Billing via SIR Platform with the "Subscriptions Launching Soon" fallback and email capture; activates when gateway keys are added.
### M4 AI
{m4}
### M5 Quality sweep
- [ ] 5 states on every screen, 4 locales complete (no missing keys), 4 themes, a11y audit, Lighthouse budgets, e2e for the critical journeys, screenshots of each at 390 px and 1280 px in LTR and RTL.
### M6 Release and retirement
{m6}"""

LOCAL = {"ahome", "sir-jobs", "sir-study", "sir-laptop-manager"}   # private or internal tools: no Firebase login, no billing, no public hosting
LOCAL_SECURITY = """- Data stays on Ahmed's machine; nothing about the people involved goes to any outside AI provider, repo, log or artifact (AHome: everything about Habiba stays private).
- Secrets only in Windows Credential Manager or an untracked `.env` outside git; gitleaks clean in CI and pre-commit; licence audit.
- Login is required on every surface, never optional: two named accounts only, passkey (WebAuthn) or a strong password plus TOTP, sessions in HttpOnly + Secure + SameSite=Strict cookies, rate limit and lockout, server-side check on every route, a device allow-list for phones. An unauthenticated request gets 401 (tested). Anyone who finds the address still sees nothing.
- Local server binds to 127.0.0.1 only; any phone access goes through the private tunnel with auth; no public ingress; threat model written and tested.
- Every destructive action has a dry run and an undo (quarantine); data directory snapshot and restore drill recorded before the first change.
- Input validated at every boundary (pydantic or zod); subprocess and file paths never built from raw input."""
LOCAL_MILESTONES = """### M0 Foundations
- [ ] Create the folder from `plans/MASTER_REBUILD_PLAN.md` naming rules; `git init`, private GitHub repo `sirahmed8/{repo}`.
- [ ] `.sir/` file set (project.yml, CHECKPOINT.md, BOARD.md) from `standard/project-templates.md`; AGENTS/CLAUDE/GEMINI from `standard/agent-files.md`.
- [ ] Data and secrets layout: data directory and `.env` outside git, backup copy to `D:/Projects/Backups`, snapshot and restore drill saved in `.sir/evidence/`.
- [ ] Threat model and privacy data map (what may leave the machine: nothing private) written in `docs/`.
- [ ] Authentication design: two named accounts, passkey or password plus TOTP, sessions, lockout, device allow-list, phone access only through a private tunnel with its own identity check (Cloudflare Access limited to the two accounts, or Tailscale; verify current terms first); written as an ADR before any code.
- [ ] Local verify: lint, typecheck, tests, gitleaks in one command and in CI; first green run.
### M1 Core slice
{m1}
### M2 Parity with the old project
{m2}
### M3 Security and reliability
- [ ] Security checklist above is green with tests (no public bind, no route answers without a valid session, brute force locks out, bad input, path traversal, secret scan).
- [ ] Backup, restore and rollback runbook tested once; `doctor` command prints health in one screen.
- [ ] Dry-run and undo for every destructive action, tested.
### M4 AI
{m4}
### M5 Quality sweep
- [ ] Every screen or command has first-use, loading, empty, error and populated states; Arabic and English text correct; keyboard use complete; accessibility checked where there is a UI; performance budget recorded.
### M6 Release and retirement
{m6}"""


MERGE = {
    "sir-hagoozat": ["Hagoozat Elite", "11Players", "EGFootball5"],
    "sir-business": ["SIR Restaurant", "SIR Market", "SIR Pharmacy", "SIR Library"],
    "sir-controller": ["SIR Controller (v1)", "SIR Optimizer"],
    "sir-laptop-manager": ["antigravity-agent-suite", "Laptop manager (moves in when replaced)"],
    "sir-obour-hub": ["Obour Academic Hub"],
    "sir-study": ["materials/obour-year2-term1 (the old Obour Institute study folder)"],
    "sir-negm-furniture": ["Negm Furniture"], "sir-odysseus": ["Odysseus app"],
    "sir-content-creation-studio": ["SIR Content Creation Studio (v1)"], "sir-modpack": ["SIR ModPack (v1)"],
    "sir-mods-for-gta-v": ["SIR Mods for GTA V (v1)"], "sir-ai": ["SIR AI (v1)"],
    "sir-jobs": ["Jobs (data moves in when imported)"],
}


def merge_block(p):
    src = MERGE.get(p["slug"])
    if not src:
        return ""
    items = chr(10).join("- " + x for x in src)
    return f"""## 0. THIS IS A MERGE PROJECT (read first)
The old projects below were physically moved into this folder (`legacy/`, or `materials/` for study) with their complete code, git history, structure and assets. Many projects with many features are being merged into this ONE new product so one agent can finish it end to end.
{items}
Your job: read `_SIR/ops/inventory/` for each source, then port everything of value into the new clean structure (apps/, packages/) with professional, high quality code and clean architecture; fully set up and configured; tested; deployed to Cloudflare; pushed to the private repo; in production mode (real env vars by name, real domain or pages.dev, monitoring, backups). Never edit `legacy/` except to read. When M6 is complete, move every `legacy/*` folder to `D:/Projects/old projects/` and record it in the checkpoint.

"""
    return ""


def build(p):
    ctx = dict(p)
    ctx["m1"] = "\n".join(f"- [ ] {t}" for t in p["m1"])
    ctx["m2"] = "\n".join(f"- [ ] {t}" for t in p["m2"])
    ctx["m4"] = "\n".join(f"- [ ] {t}" for t in p["m4"])
    ctx["m6"] = "\n".join(f"- [ ] {t}" for t in p["m6"])
    ms = (LOCAL_MILESTONES if p["slug"] in LOCAL else MILESTONES).format(**ctx)
    folder = os.path.join(PROJECTS, p["folder"])
    cfg = os.path.join(folder, ".git", "config")
    if os.path.isfile(cfg) and 'remote "origin"' in io.open(cfg, encoding="utf-8", errors="ignore").read():
        ms = ms.replace("- [ ] Create the folder", "- [x] Create the folder", 1)
    if os.path.isfile(os.path.join(folder, ".sir", "CHECKPOINT.md")) and os.path.isfile(os.path.join(folder, "AGENTS.md")):
        ms = ms.replace("- [ ] `.sir/` file set", "- [x] `.sir/` file set", 1)
    return f"""# PLAN: {p['display']}
Status: planned, not started. Wave {p['wave']}. Replaces: {p['replaces']}. Read `_SIR/NEXT.md` and `_SIR/plans/MASTER_REBUILD_PLAN.md` first.

{merge_block(p)}## 1. Mission and audience
{p['mission']}

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\\Projects\\{p['folder']}` |
| GitHub (private) | `sirahmed8/{p['repo']}` |
| Firebase project / OAuth app name | `{p['firebase']}` / "{p['display']}" |
| Cloudflare project | `{p['repo']}` (`{p['repo']}.pages.dev` until a domain is affordable) |
| App ids | `app.sir.{p['slug']}` (Android, iOS, Windows) |
| Platforms | {p['platforms']} |
| Money | {p['money']} |

## 3. Why rebuild (evidence from the Phase 3 inventories)
{p['why']}

## 4. What to port from the old project
{p['port']}

## 5. Screens and entities
**Screens:** {p['screens']}
**Entities:** {p['entities']}
**UX rules:** {COMMON_UX}

## 6. AI at the core
{p['ai']}

## 7. Security checklist (all must pass)
{LOCAL_SECURITY if p["slug"] in LOCAL else COMMON_SECURITY}
{p['security_extra']}

## 8. Milestones
{ms}

## 9. Risks and open decisions
{p['risks']}

## 10. How any chat continues this project
Read this file, then `.sir/CHECKPOINT.md`, then work the first unchecked box in section 8. Tick boxes only with evidence (command output or screenshot path). After each box update the checkpoint and commit. Never ask Ahmed; if blocked by a permission, write the single command in `NEXT.md` and continue with the next box.
"""


def main():
    os.makedirs(HERE, exist_ok=True)
    for p in PRODUCTS:
        text = build(p)
        with open(os.path.join(HERE, p["slug"] + ".md"), "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        sir = os.path.join(PROJECTS, p["folder"], ".sir")
        if os.path.isdir(sir):
            with open(os.path.join(sir, "PLAN.md"), "w", encoding="utf-8", newline="\n") as f:
                f.write(text)
    rows = []
    tot_d = tot_n = 0
    for p in sorted(PRODUCTS, key=lambda x: (x["wave"], x["slug"])):
        t = io.open(os.path.join(HERE, p["slug"] + ".md"), encoding="utf-8").read()
        d, n = t.count("- [x]"), t.count("- [x]") + t.count("- [ ]")
        tot_d += d
        tot_n += n
        rows.append("| %s | wave %s | %d / %d | %d%% | `plans/%s.md` |" % (p["display"], p["wave"], d, n, round(100 * d / max(n, 1)), p["slug"]))
    nl = chr(10)
    head = "# PROGRESS (generated by plans/generate_plans.py from the checkboxes in every plan; re-run after ticking)" + nl + nl
    head += "Overall: %d / %d boxes (%d%%). Boxes are ticked only with evidence." % (tot_d, tot_n, round(100 * tot_d / max(tot_n, 1))) + nl + nl
    head += "| Product | Wave | Boxes done | % | Plan |" + nl + "|---|---|---|---|---|" + nl
    io.open(os.path.join(HERE, "PROGRESS.md"), "w", encoding="utf-8", newline=nl).write(head + nl.join(rows) + nl)
    print(len(PRODUCTS), "plans written")


if __name__ == "__main__":
    main()
