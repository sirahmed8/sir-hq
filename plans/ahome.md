# PLAN: AHome (private, Wave 1)
Audited 2026-11-10 by the plans audit. Exempt from every commercial item (no subscription, marketing, SEO, store launch, public analytics, public legal pages, portfolio listing). It gets top quality, privacy and reliability.
Rule for this file: the AHome folder's own `.sir/MASTER_PLAN.md` and `.sir/TASKS.md` are the working task list; this file is the outside summary. Nothing private (names tied to private facts, messages, notes, photos, calendar) is ever copied here, into briefs, into artifacts or into outside AI providers.

## 1. Purpose (plain words)
AHome is the private home app of two people. It holds a shared calendar, notes, dates, reminders and a local AI assistant, and talks to them through a phone page and a Telegram bot. It runs on Ahmed's own computer. It is never public and never sold.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\AHome` (the name stays; the folder is improved in place) |
| GitHub (private) | `sirahmed8/ahmed-and-habiba-sanctuary` |
| App id | `app.sir.ahome` |
| Platforms (built, unverified) | local core (FastAPI, `apps/local-core`), web app (`apps/web`, Next.js), Windows daemons (`infra-daemons`), Electron and Tauri desktop shells, Capacitor Android shell, an APK at `D:\Projects\AHome-v1.0.0.apk` |
| Skipped on purpose | iOS store build, macOS, Linux, TV, watch, car, extension (private two-user app; iOS is by PWA install, see `docs/IOS_INSTALL.md`) |
| Money | none |

## 3. Current state (read from folder and PORTFOLIO.md, not re-verified by this audit)
Truth rule: nothing below is "working" until a reviewer runs it today.
- Built, unverified: local core with `auth`, `core`, `domain`, `presentation` layers and about 40 test files; Telegram gateway modules (`telegram_*.py`); Firebase bridge, relay and sweep; web push delivery; `doctor.py` health command; `snapshot.py` and `snapshot_prune.py` backups; privacy audit script (`scripts/privacy-audit.mjs`); bundle budget script; game-mode and watchdog scripts; packages `crypto-e2ee`, `dynamic-engine`, `sanctuary-mcp`, `shared-types`; adversarial, e2e and stress test folders; docs `THREAT_MODEL.md`, `RUNBOOK.md`, `PRIVACY_CHECK.md`, `PAIRING.md`.
- Claimed in PORTFOLIO.md (2026-11-08): 303 commits, 52 of 79 tasks done, two-way sync for Google Tasks, TickTick and ICS, Telegram contact spoof hardening, unsafe-eval dropped from the CSP, "dual deploy live (Vercel + Firebase)". All built, unverified.
- Older text in this plan said "planned, not started". That was wrong and is removed.
- Service account key file in the folder root is git-ignored (checked by name: ignored by `.gitignore` line 73, not tracked).
- Not started or not proven: restore drill evidence in `.sir/evidence/`, encrypted-backup restore test, passkey login, device allow-list proof, 80 to 200 percent zoom and 320 px audit, Chinese and Hindi text review.

## 4. Privacy and security rules (all must be proven by a test or a command)
1. Local core binds to 127.0.0.1 only. Test: `netstat` shows no other bind; a request from another interface fails.
2. Every route needs a valid session. Test: an unauthenticated request returns 401 on every route listed by the router (generated test, not hand-written).
3. Two named accounts only. Passkey (WebAuthn) or strong password plus TOTP. Cookies HttpOnly, Secure, SameSite=Strict. Rate limit and lockout. No token in localStorage.
4. Phones reach the core only through a private tunnel with its own identity check (Cloudflare Access limited to the two accounts, or Tailscale; check current free terms first, source needed: "(unsourced, verify)").
5. The hosted web copy (Vercel and Firebase Hosting, per PORTFOLIO.md) must show no data without login and must hold no secrets or private text in its static build. Test: `scripts/smoke-hosted.ps1` plus a grep of the `out/` folder for private strings. Default decision: if this cannot be proven, take the hosted copy down and use the tunnel only.
6. Secrets only in Windows Credential Manager or an untracked `.env` outside git. gitleaks clean in CI and pre-commit. Keys that were in history are rotated, then history is purged (M6).
7. Private content goes only to local models (Ollama). No outside AI provider, no log, no artifact, no repo, no dashboard gets message text, notes, calendar or photos. The dashboard may show counts and status only.
8. Every destructive action has a dry run and an undo (quarantine). Data folder snapshot and restore drill saved in `.sir/evidence/`.
9. Input validated at every boundary (pydantic or zod). File paths and subprocess arguments never built from raw input.
10. Backups are encrypted, kept in `D:\Projects\Backups`, and one restore is tested.

## 5. Shared pieces
AHome shares nothing with other products and consumes nothing from the shared kit. It may reuse only the design tokens idea (own copy). No data flows to or from any other project. The Telegram bot is AHome's own bot; Ahmed's report bot for other products is separate.

## 6. Screens, entities, UX
Screens: Today, Calendar, Notes, Dates, Reminders, Assistant, Settings, Profile. Entities: Person (2), Event, Note, Reminder, Message, Device.
Every screen has five states (first use, skeleton, empty with one action, error with Retry, populated with 1,000+ items). Arabic RTL (logical CSS) and English first; Chinese and Hindi only if the owner still wants them (default: keep them, lowest priority). Light, dark, system, high contrast. 320 px to 4K, zoom 80 to 200 percent, spring motion with reduced-motion path, WCAG 2.2 AA, 44 px touch targets. Own logo (`project icon.jpg` exists) used for favicon, PWA icon and top bar.

## 7. AI (local only)
Ollama models in `D:\Projects\AI_Models_Hub`. Features: ask over notes and dates, reminder wording, Telegram assistant, voice (`eval_voice.py`). Eval set lives in `docs/ai_eval`. Fallback chain is local model A, local model B, plain rule-based answer; never an outside provider. A kill switch setting turns the assistant off. Quota: none (two users). Support assistant: not needed (the two users are the owners).

## 8. Milestones with exit checks
| M | Goal | Exit check |
|---|---|---|
| M0 | Foundations: layout, secrets outside git, threat model, restore drill, one verify command | `scripts/doctor.py` prints green; `.sir/evidence/restore-drill.md` exists with a real restore output; gitleaks exit 0 |
| M1 | Core slice stable under the supervisor | `ahome-service-supervisor.ps1` keeps port 8090 up after a kill test (screenshot of restart log) |
| M2 | Parity with old project on the new UI | every screen in section 6 opens at 390 px and 1440 px (screenshots saved in `.sir/evidence/`) |
| M3 | Security and reliability | tests for rules 1 to 10 pass; brute force locks out; path traversal blocked |
| M4 | Local AI | eval run in `docs/ai_eval` scores recorded; delete control removes a note from the index (test) |
| M5 | Quality sweep | five states on every screen; axe or manual a11y report; bundle budget script green; 320 px and 200 percent zoom screenshots |
| M6 | Rotation and cleanup | keys rotated, history purge done, no AHome entry in any public list (grep of `SIR Portfolio` and dashboards for the name) |

## 9. Next 10 tasks (each under 2 hours)
1. Run the existing tests for `apps/local-core` and write the real pass/fail count into `.sir/evidence/tests-2026-11-10.md`. Check: file has the command and output.
2. Add a generated test that lists every router path and asserts 401 without a session. Files: `apps/local-core/tests/test_auth_all_routes.py`. Check: test passes; a deliberately open route makes it fail.
3. Run `scripts/snapshot.py`, then restore into a temp folder and compare file hashes. Files: `.sir/evidence/restore-drill.md`. Check: hashes equal.
4. Run `scripts/privacy-audit.mjs` and the hosted smoke check; record what the hosted copy exposes. Check: report says "no private strings in out/".
5. Decide the hosted copy: keep with proof or take down (default in section 4.5). Files: `docs/PRIVACY_CHECK.md`. Check: decision written with the proof.
6. Passkey login ADR then first endpoint. Files: `docs/adr/auth-passkey.md`, `apps/local-core/auth/`. Check: register and login test with a virtual authenticator.
7. Device allow-list: a phone not on the list gets 403. Files: `apps/local-core/auth/`, `docs/PAIRING.md`. Check: pytest case.
8. Five-state audit of Today and Reminders screens at 390 px, fix gaps. Files: `apps/web` screens. Check: 5 screenshots per screen.
9. Zoom and RTL audit of Calendar at 200 percent and 320 px. Check: no horizontal scroll (`document.documentElement.scrollWidth <= innerWidth` in a script).
10. Rotate the Telegram, Firebase and Gemini keys listed in `docs/ENV.md`; gitleaks on history. Check: old keys return 401 from their APIs; new keys only in Credential Manager.

## 10. Risks and open questions (default decisions, agents never ask)
- Hosted copy may leak data: default is take it down if unproven.
- Tunnel free-tier terms may change: default is Tailscale, fall back to Cloudflare Access.
- Tauri, Electron and Capacitor shells triple the maintenance: default is keep Electron and the PWA as the supported pair, mark the others "frozen, unverified".
- Private AI quality on a laptop is limited: default is smaller local models with the rule-based fallback.

## 11. Only the owner can do
Sign in to Google, Telegram and Firebase when a token expires; approve passkey registration on his devices; type any secret into a form; decide anything that speaks as him to Habiba.

## 12. How any chat continues
Read `.sir/CHECKPOINT.md`, then this file, then do the first task in section 9 that has no evidence file. Never read vault, message, note or photo content to do a task; use counts and test fixtures.
