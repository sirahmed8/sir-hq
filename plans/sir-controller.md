# PLAN: SIR Controller
Status: planned, not started. Wave 3. Replaces: SIR Controller v1 + SIR Optimizer (PulseTools). Read `_SIR/NEXT.md` and `_SIR/plans/MASTER_REBUILD_PLAN.md` first.

## 0. THIS IS A MERGE PROJECT (read first)
The old projects below were physically moved into this folder (`legacy/`, or `materials/` for study) with their complete code, git history, structure and assets. Many projects with many features are being merged into this ONE new product so one agent can finish it end to end.
- SIR Controller (v1)
- SIR Optimizer
Your job: read `_SIR/ops/inventory/` for each source, then port everything of value into the new clean structure (apps/, packages/) with professional, high quality code and clean architecture; fully set up and configured; tested; deployed to Cloudflare; pushed to the private repo; in production mode (real env vars by name, real domain or pages.dev, monitoring, backups). Never edit `legacy/` except to read. When M6 is complete, move every `legacy/*` folder to `D:/Projects/old projects/` and record it in the checkpoint.

## 1. Mission and audience
One Windows app and website for game-controller mapping and PC optimization. Audience: PC gamers in Egypt and the Gulf.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Controller` |
| GitHub (private) | `sirahmed8/sir-controller` |
| Firebase project / OAuth app name | `sir-controller` / "SIR Controller" |
| Cloudflare project | `sir-controller` (`sir-controller.pages.dev` until a domain is affordable) |
| App ids | `app.sir.sir-controller` (Android, iOS, Windows) |
| Platforms | Windows desktop (.NET/WPF existing core; rebuild UI on WinUI 3 or Tauri after a spike) + web portal on Cloudflare |
| Money | Free controller mapping; Pro in EGP for profiles sync and the optimizer suite; Launching Soon fallback |

## 3. Why rebuild (evidence from the Phase 3 inventories)
- Controller: unsigned webhook (stopgap merged), client-side owner gate with hardcoded email, LGPL-3.0 text against a proprietary EULA, about 20 binaries in git, download button pointing at a private repo.
- Optimizer: client could grant itself OP mode, AI keys in the bundle (stopgap merged), simulated owner transactions.
- Both solve the same job; Laptop manager shares hardware code.

## 4. What to port from the old project
- Controller: 298 MSTest cases (keep), mapping engine, installer. Optimizer: tweak catalog (only tweaks that are safe and reversible), PulseTools UI ideas.
- Extract hardware helpers shared with Laptop manager once.

## 5. Screens and entities
**Screens:** Dashboard, Controllers, Profile editor, Test pad, Optimizer scan + reversible tweaks with restore points, Downloads, Pricing, Account, Owner dashboard, Help
**Entities:** Profile, Mapping, Device, Tweak, TweakRun, RestorePoint, Subscription, DownloadRelease
**UX rules:** Every screen implements the 5 states: first use, loading skeleton matching the final layout, empty (one clear action), error (human message + Retry), populated (paginated or virtualized, fine with 1,000+ items). Arabic RTL (CSS logical properties) + English + Simplified Chinese + Hindi; light, dark, system and high-contrast themes; keyboard shortcuts; 320 px to 4K; zoom 80%-200%; spring motion with a reduced-motion path; WCAG 2.2 AA. Own colour seed and icon; the same Profile and Settings screens as every SIR product.

## 6. AI at the core
Flagship: explains each tweak and its risk in plain Arabic/English before applying; assistant grounded in docs.

## 7. Security checklist (all must pass)
- Owner/admin only from a server-verified Firebase ID token (JWKS) plus OWNER_EMAILS / OWNER_UIDS; email path needs email_verified; fail closed when unset (SIR Platform `owner-auth`).
- Every webhook: HMAC over the raw body with the timestamp inside the signed payload, timing-safe compare, idempotent activation (SIR Platform `signed-webhook`).
- No AI key, token or secret in any client bundle or git; AI only through the server proxy with per-user quota; owner unmetered (SIR Platform `ai-proxy`).
- Sessions in HttpOnly + Secure + SameSite=Strict cookies, never localStorage. Rate limits on login/register/reset. Input validated with zod at every boundary.
- Firestore/D1 rules deny by default, per-user/per-tenant claims, tested in the emulator. CSP with nonces, no unsafe-eval.
- gitleaks in CI and pre-commit; dependency audit; licence audit (no GPL/AGPL in proprietary code).
- Every tweak reversible with a recorded restore point; installer and downloads served from public release repo with checksums; licence text matches the real licence.

## 8. Milestones
### M0 Foundations
- [x] Create the folder from `plans/MASTER_REBUILD_PLAN.md` naming rules; `git init`, private GitHub repo `sirahmed8/sir-controller`.
- [x] `.sir/` file set (project.yml, CHECKPOINT.md, BOARD.md) from `standard/project-templates.md`; AGENTS/CLAUDE/GEMINI from `standard/agent-files.md`.
- [ ] New Firebase project `sir-controller` (Auth Google, Firestore) and Cloudflare project; OAuth app name "SIR Controller", logo, support email.
- [ ] Login brand check: sign in with Google in a real browser; the screen must not show a Firebase project id; screenshot saved in `.sir/evidence/`.
- [ ] CI: typecheck, lint, test, build, gitleaks on every push; first green run.
### M1 Core slice
- [ ] Profile load/save + test pad on the existing engine with tests; web portal sign-in brand check.
### M2 Parity with the old project
- [ ] Optimizer tweaks ported with undo; installer; downloads page pointing at real releases.
### M3 Security, legal, billing
- [ ] Security checklist above is green with tests (forged cookie, unsigned webhook, unverified email, cross-tenant read all fail).
- [ ] Legal pack generated from what the product really collects; cookie banner with equal Reject; account and data deletion flow.
- [ ] Billing via SIR Platform with the "Subscriptions Launching Soon" fallback and email capture; activates when gateway keys are added.
### M4 AI
- [ ] Tweak explainer and risk labels from a cited catalog; no performance claims without benchmark output.
### M5 Quality sweep
- [ ] 5 states on every screen, 4 locales complete (no missing keys), 4 themes, a11y audit, Lighthouse budgets, e2e for the critical journeys, screenshots of each at 390 px and 1280 px in LTR and RTL.
### M6 Release and retirement
- [ ] Publish release with checksums; archive SIR Optimizer repo; retire both v1 folders.

## 9. Risks and open decisions
- Licence audit of the mapping engine (LGPL parts) before selling.
- Driver-level tweaks are risky: ship read-only scan first.

## 10. How any chat continues this project
Read this file, then `.sir/CHECKPOINT.md`, then work the first unchecked box in section 8. Tick boxes only with evidence (command output or screenshot path). After each box update the checkpoint and commit. Never ask Ahmed; if blocked by a permission, write the single command in `NEXT.md` and continue with the next box.
