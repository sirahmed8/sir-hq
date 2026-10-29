# Inventory: SIR AI (D:\Projects\SIR AI)
Scan date 2026-10-29. Read-only on the project. Secrets masked; only presence noted.
## What it is / who
Private local AI assistant: FastAPI server (web/, core/), Electron HUD (app/), Firebase-hosted portal (web/static, sir-ai-official.web.app), Telegram and WhatsApp bridges, C# installer/launcher. Owner: Ahmed. License: package.json says Proprietary, app/package.json says Commercial, no LICENSE file.
## Build / run
- Python 3.11.15 venv (.venv). fastapi 0.141.1, pydantic 2.13.5, uvicorn 0.53.0.
- Missing from venv vs requirements.txt: telethon, pyautogui, google.oauth2, cv2, aiortc, chromadb, PySide6.
- AST parse of 137 tracked .py files: 0 syntax errors.
- pytest --collect-only: 207 tests collected, no errors. Full run NOT done. README claims 104/104 (unverified).
- Electron 34.2 (app/package.json). Icon path app/assets/icon.ico exists.
## Repo health
- origin github.com/sirahmed8/SIR-AI; branch main = origin/main = eb4dff0 (2026-10-26). Clean tree, 0 stashes, 0 worktrees. Extra branch pre-sir-snapshot at same commit.
- 433 tracked files. .git 78 MB, mostly data/models blob 73 MB tracked.
- Nested repo public_repo (origin SIR-AI-Public, 4576e6b 2026-10-26).
- Tracked binaries at root: SIR AI.exe, SIR AI Setup.exe, Jarvis.dll, JarvisSetup.dll.
- No .github/ workflows, no CI.
## Structure
web/ (routes, server.py, static), core/ (73 files: security, billing, connectors, memory), app/ (Electron), telegram/ and bridges/telegram_gateway/ (duplicate: poller.py and bot.py identical, commands.py differs), installer/, launcher/, autonomous/, engine/, tests/ (47 files), docs/, config/, data/.
Files over 300 lines: 10 (telegram/poller.py 750, commands.py 728, data/repository.py 395).
## Data layer / auth / AI
- SQLite (data/*.db, gitignored), chromadb vector store (not installed), YAML/JSON config.
- Auth: Google ID token -> HttpOnly cookie, SameSite=lax (web/routes/auth_routes.py:102-103).
- Owner telemetry trusts client header/cookie: web/routes/owner_routes.py:40-50 (x-owner-email header or sir_user_email cookie, falls back to owner email). Spoofable.
- Session tokens in localStorage: web/static/auth-popup.html:205-206 (jarvis_auth_token, sir_session_token).
- No TOTP, zxcvbn or HIBP code found (0 hits). Rate limiting exists in web/server.py and core/security/gateway_security.py, not confirmed on auth routes.
- AI keys: .env has no GEMINI/OPENAI/ANTHROPIC/GROQ/Stripe/Paymob keys (presence check). Providers referenced in code: gemini, openai, anthropic, groq, ollama, deepseek.
- Secrets: .env exists, untracked, gitignored. Firebase web apiKey literal in client JS (app/js/auth.js:15, web/static/js/dashboard.js:265, landing.js:8) and as a code fallback in core/security/auth_manager.py:80,120. Value not printed. A test fixture key-shaped string at tests/test_codex_gateway.py:14 (value not printed).
## Legal and icons
- Routes /privacy /terms /cookies /refund(s) exist (web/routes/static_routes.py:129-150).
- Root PRIVACY_POLICY.md:28 has AI-training prohibition and :34-35 sub-processor list claiming SOC 2 Type II and ISO 27001. Served web/static/privacy.html has neither section (0 hits). Claim unverified.
- No reject-all control found in web/static/cookies.html.
- No DPA document found.
- Icons: app/assets/icons (4 .ico), web/static/icons (5), root icon.ico and favicon.ico.
## Business ops coverage
CRM 10 files, calendar 9, WhatsApp 9, tiktok 4, job 4, invoice 3, instagram 3, facebook 5. No LinkedIn. YouTube only in 3 non-core files. Videos and social are partly covered by connectors; jobs and company ops are thin.
## Desktop launchers (verified via .lnk strings)
- Desktop folder "SIR AI": SIR AI.lnk and SIR AI Standalone.lnk -> D:\Projects\SIR AI\SIR AI.exe; SIR AI Setup.lnk -> SIR AI Setup.exe; Stop SIR AI Server.lnk -> stop_server.vbs; SIR AI Web Portal.lnk target not resolved.
- Startup "OurSanctuary Daemon Stack.lnk" runs D:\Projects\AHome\infra-daemons (description says SIR AI). Not SIR AI code.
## Scores (0-5)
- Architecture 3: layered folders, but duplicated telegram trees and 750-line files.
- Code quality 3: parses clean; 10 files over 300 lines.
- Security 1: spoofable owner check, localStorage tokens, no 2FA, no HIBP, literal key fallback.
- UX/design 2: not reviewed in browser.
- Performance 2: 73 MB model blob in git.
- Completeness 2: optional deps missing in venv; tests not run.
- Store readiness 1: mixed license, unverified certification claims, unsigned status not checked.
## Red flags
1. Owner telemetry auth bypass via header/cookie (owner_routes.py:40-50).
2. Tokens in localStorage (auth-popup.html:205-206).
3. Literal Firebase key fallback (auth_manager.py:80,120).
4. Unsupported SOC 2 and ISO claim (PRIVACY_POLICY.md:35).
5. Served privacy page omits root policy sections.
6. Personal profile tracked: config/user_profile.yaml differs from example (values not printed).
7. Model blob 73 MB in git history.
## Overlap
PORTFOLIO lists SIR AI, SIR Controller, SIR Optimizer, Laptop manager. Not read in depth. Overlap likely in telemetry and personal-ops code; verify before merging.
## Upgrade size: L
Top 5 fixes:
1. Server-side owner check (signed session, not header). S.
2. Move session tokens to HttpOnly cookies only. M.
3. Remove literal Firebase key fallback; restrict key in GCP. S.
4. Correct privacy claims; publish DPA and sub-processor list. S.
5. Untrack model blob and user_profile.yaml; dedupe telegram trees. M.
## Not verified
Live site not fetched. Electron not run. Full pytest not run. Installer signature not checked (PowerShell module load failed).
