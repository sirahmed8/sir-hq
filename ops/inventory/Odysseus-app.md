# Inventory: Odysseus app (2026-10-29, scout, read-only; nothing built, run or tested)

**What:** self-hosted AI workspace (chat, agents, research, documents, email, notes, calendar, local models). A **fork of odysseus-dev/odysseus**, so most of the code is not Ahmed's.
**Live:** `sir-odysseus-app.web.app` returns 404 (firebaseapp.com too); Firebase hosts `website/`, not the app, despite the deploy commit.
**Stack:** Python 3.11+, FastAPI, SQLAlchemy, Pydantic 2; vanilla JS (172 files in `static/js`); Electron 43.4.0; electron-builder 26. Platforms: Windows (NSIS, unsigned), Docker, macOS scripts, Linux systemd.
**Repo:** main = origin/main, clean, 3,180 commits (last 2026-10-26, 5180320e; 5 in 30 days); origin/dev last 2026-07-12.
**Data/auth:** SQLite `data/app.db`; HttpOnly cookie SameSite=Lax (routes/auth_routes.py:192-194), TOTP, rate limit. No OWNER_EMAILS logic, no /admin route, no payments. AI: 15+ providers; `src/subscription_ai.py` and `src/chatgpt_subscription.py` use consumer CLI/OAuth sessions (terms risk).
**Legal:** root markdown only, not served by the app. **Tests/CI:** 832 test files, 4,967 test functions, 197 skip markers; CI has ruff, mypy (non-blocking), pytest fast lane, CodeQL, gitleaks, Trivy. 95 .md files.
**Desktop `Odysseus\`:** `Odysseus.lnk` and `Odysseus Installer.lnk` point to `dist\win-unpacked\*.exe`; `dist/` is empty so both are dangling.

## Scores (0-5)
Architecture 3 · Code quality 2 · Security 3 · UX/design 2 · Performance 2 (unmeasured) · Completeness 2 · Store readiness 1.

## Red flags
1. **AGPL-3.0 LICENSE vs proprietary legal docs** (decision pending in the TickTick sprint, Day 24). Under AGPL the network-use clause means modified source must be offered to users; the proprietary EULA contradicts it.
2. Live site 404 although a deploy commit exists.
3. `PRIVACY_POLICY.md:35` claims SOC 2/ISO sub-processors (unverified).
4. `website/index.html:505-514` has fake testimonials and stock images (nothing fake may ship).
5. AI directive files tracked in the repo root. 6. Consumer-subscription AI paths may break provider terms.

## Upgrade size: L. Top 5 fixes
1. Decide the licence honestly (it is a fork: either keep AGPL and publish, or stop calling it proprietary) and rewrite the legal docs to match. 2. Fix the deploy (website vs app). 3. Serve truthful legal routes. 4. Run `dist`, fix or delete the dangling shortcuts. 5. Split files over 300 lines, SameSite=Strict, remove fake testimonials.
Business ops: none (no billing, leads or revenue telemetry).
