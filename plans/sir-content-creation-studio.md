# PLAN: SIR Content Creation Studio
Status: planned, not started. Wave 3. Replaces: SIR Content Creation Studio v1 (with the SIR Media idea and ByteVibeHQ publishing). Read `_SIR/NEXT.md` and `_SIR/plans/MASTER_REBUILD_PLAN.md` first.

## 0. THIS IS A MERGE PROJECT (read first)
The old projects below were physically moved into this folder (`legacy/`, or `materials/` for study) with their complete code, git history, structure and assets. Many projects with many features are being merged into this ONE new product so one agent can finish it end to end.
- SIR Content Creation Studio (v1)
Your job: read `_SIR/ops/inventory/` for each source, then port everything of value into the new clean structure (apps/, packages/) with professional, high quality code and clean architecture; fully set up and configured; tested; deployed to Cloudflare; pushed to the private repo; in production mode (real env vars by name, real domain or pages.dev, monitoring, backups). Never edit `legacy/` except to read. When M6 is complete, move every `legacy/*` folder to `D:/Projects/old projects/` and record it in the checkpoint.

## 1. Mission and audience
Offline-first AI video studio for Shorts/Reels/TikTok and long form, plus scheduled publishing for ByteVibeHQ's accounts. Audience: Ahmed first, then creators.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Content Creation Studio` |
| GitHub (private) | `sirahmed8/sir-content-creation-studio` |
| Firebase project / OAuth app name | `sir-content-studio` / "SIR Content Creation Studio" |
| Cloudflare project | `sir-content-creation-studio` (`sir-content-creation-studio.pages.dev` until a domain is affordable) |
| App ids | `app.sir.sir-content-creation-studio` (Android, iOS, Windows) |
| Platforms | Windows desktop (Electron) + local engine (Python FastAPI, Remotion) + web dashboard |
| Money | Free local editing; Pro for cloud render queue and scheduler (EGP); Launching Soon fallback |

## 3. Why rebuild (evidence from the Phase 3 inventories)
- No server-side token check (owner gating by env in 6 files), personal state files tracked in git (profile, uid, pro flag, studio.db), unsigned stale installer, Python 3.10/3.11/3.13 mismatch, CI failing.
- No Launching Soon fallback; payment SDK names scattered in 5 files.

## 4. What to port from the old project
- Engine: transcript, captions, reframing, b-roll, sound effects pipeline, Remotion templates, 120 test files (keep the good ones).
- UI flows for project, timeline, export.

## 5. Screens and entities
**Screens:** Projects, Import, Transcript editor, Timeline, Captions, Templates, Export queue, Scheduler (ByteVibeHQ calendar), Settings, Owner dashboard, Help
**Entities:** Project, Asset, Transcript, Caption, Template, RenderJob, ScheduledPost, Account (official API tokens stored server-side)
**UX rules:** Every screen implements the 5 states: first use, loading skeleton matching the final layout, empty (one clear action), error (human message + Retry), populated (paginated or virtualized, fine with 1,000+ items). Arabic RTL (CSS logical properties) + English + Simplified Chinese + Hindi; light, dark, system and high-contrast themes; keyboard shortcuts; 320 px to 4K; zoom 80%-200%; spring motion with a reduced-motion path; WCAG 2.2 AA. Own colour seed and icon; the same Profile and Settings screens as every SIR product.

## 6. AI at the core
Flagship: AI clip finder + caption writer. Providers via ai-proxy; local Whisper/Ollama for private media.

## 7. Security checklist (all must pass)
- Owner/admin only from a server-verified Firebase ID token (JWKS) plus OWNER_EMAILS / OWNER_UIDS; email path needs email_verified; fail closed when unset (SIR Platform `owner-auth`).
- Every webhook: HMAC over the raw body with the timestamp inside the signed payload, timing-safe compare, idempotent activation (SIR Platform `signed-webhook`).
- No AI key, token or secret in any client bundle or git; AI only through the server proxy with per-user quota; owner unmetered (SIR Platform `ai-proxy`).
- Sessions in HttpOnly + Secure + SameSite=Strict cookies, never localStorage. Rate limits on login/register/reset. Input validated with zod at every boundary.
- Firestore/D1 rules deny by default, per-user/per-tenant claims, tested in the emulator. CSP with nonces, no unsafe-eval.
- gitleaks in CI and pre-commit; dependency audit; licence audit (no GPL/AGPL in proprietary code).
- Personal state never in git; Python version pinned once; installer signed when possible; social tokens only server-side; no X website scripting (official APIs/schedulers only).

## 8. Milestones
### M0 Foundations
- [ ] Create the folder from `plans/MASTER_REBUILD_PLAN.md` naming rules; `git init`, private GitHub repo `sirahmed8/sir-content-creation-studio`.
- [ ] `.sir/` file set (project.yml, CHECKPOINT.md, BOARD.md) from `standard/project-templates.md`; AGENTS/CLAUDE/GEMINI from `standard/agent-files.md`.
- [ ] New Firebase project `sir-content-studio` (Auth Google, Firestore) and Cloudflare project; OAuth app name "SIR Content Creation Studio", logo, support email.
- [ ] Login brand check: sign in with Google in a real browser; the screen must not show a Firebase project id; screenshot saved in `.sir/evidence/`.
- [ ] CI: typecheck, lint, test, build, gitleaks on every push; first green run.
### M1 Core slice
- [ ] Local engine health endpoint, project create/open, transcript from a sample clip, tests for each.
### M2 Parity with the old project
- [ ] Captions, reframing, export; scheduler for Instagram/TikTok/Facebook/Reddit via official APIs; calendar with 24-hour veto window.
### M3 Security, legal, billing
- [ ] Security checklist above is green with tests (forged cookie, unsigned webhook, unverified email, cross-tenant read all fail).
- [ ] Legal pack generated from what the product really collects; cookie banner with equal Reject; account and data deletion flow.
- [ ] Billing via SIR Platform with the "Subscriptions Launching Soon" fallback and email capture; activates when gateway keys are added.
### M4 AI
- [ ] Clip finder and caption writer with eval clips; hashtag and title helper.
### M5 Quality sweep
- [ ] 5 states on every screen, 4 locales complete (no missing keys), 4 themes, a11y audit, Lighthouse budgets, e2e for the critical journeys, screenshots of each at 390 px and 1280 px in LTR and RTL.
### M6 Release and retirement
- [ ] Rebuilt installer, update channel, retire v1 folder.

## 9. Risks and open decisions
- Platform API approvals take time (owner accounts); keep drafts-only mode.
- GPU/disk limits on Ahmed's laptop: render budgets and cleanup.

## 10. How any chat continues this project
Read this file, then `.sir/CHECKPOINT.md`, then work the first unchecked box in section 8. Tick boxes only with evidence (command output or screenshot path). After each box update the checkpoint and commit. Never ask Ahmed; if blocked by a permission, write the single command in `NEXT.md` and continue with the next box.
