"""Builds plans/<slug>.md for every product from plans/products.py data plus the common sections below.
Run: python D:/Projects/_SIR/plans/generate_plans.py
Also writes the plan into <folder>/.sir/PLAN.md when the NEW folder already exists and is empty of code.
"""
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


def build(p):
    ctx = dict(p)
    ctx["m1"] = "\n".join(f"- [ ] {t}" for t in p["m1"])
    ctx["m2"] = "\n".join(f"- [ ] {t}" for t in p["m2"])
    ctx["m4"] = "\n".join(f"- [ ] {t}" for t in p["m4"])
    ctx["m6"] = "\n".join(f"- [ ] {t}" for t in p["m6"])
    ms = MILESTONES.format(**ctx)
    return f"""# PLAN: {p['display']}
Status: planned, not started. Wave {p['wave']}. Replaces: {p['replaces']}. Read `_SIR/NEXT.md` and `_SIR/plans/MASTER_REBUILD_PLAN.md` first.

## 1. Mission and audience
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
{COMMON_SECURITY}
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
    print(len(PRODUCTS), "plans written")


if __name__ == "__main__":
    main()
