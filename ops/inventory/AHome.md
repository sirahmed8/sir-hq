# AHome inventory (Phase 3.1)

Scanned 2026-10-29, read-only. No installs or builds run. Local files and git only; no web fetches.

## What it is, who for
Private couple app for Ahmed and Habiba: chat, reminders, study, arcade, memories, local AI companion. Business ops (videos, social, jobs, company): not covered.

## Build, run, deploy
- Web: Next.js in apps/web. Last build passed per checkpoint (not re-run). Vercel. Live URL in config: https://ahmed-and-private.vercel.app (200 not yet confirmed).
- Local core: FastAPI on 127.0.0.1:8090, Python 3.14.2 venv in apps/local-core/.venv.
- Firebase Hosting: redirect-only (firebase-redirect/).

## Stack (declared)
- Web: next ^16.4.3, react ^19.3.1, firebase ^13.1.0, firebase-admin ^13.10.0, tailwindcss ^3.4.17, typescript ^7.0.2.
- Local core: fastapi >=0.115 <1.0, uvicorn, edge-tts 7.x, firebase-admin 7.x, pytest 8.x (dev).

## Repo health
- Remote origin: GitHub sirahmed8/ahmed-and-habiba-sanctuary. Visibility not checked (needs a GitHub API call); confirm it is private.
- Branch sir/phase2-ahome-hygiene at be35370 (2026-10-29). Clean tree. 2 commits ahead of origin/main, 0 behind. 0 stashes.
- 291 tracked files. No .github, so no CI.

## Structure and platforms
- apps/web: web PWA, 176 src files. Routes: page.tsx, api/session, api/notify.
- apps/local-core: FastAPI with routers/, services/, one test file.
- apps/desktop-tauri, apps/mobile-capacitor: empty directories.
- packages/: crypto-e2ee, dynamic-engine, shared-types, sanctuary-mcp. ai-fleet, design-system, platform-bridge empty.
- infra-daemons/: PowerShell and Python daemons, Telegram bot, web push, n8n workflow.

## Data, auth, AI
- Data: Firebase RTDB and Firestore (rules in firebase/), local SQLite vault and JSON in local-vault/ (gitignored), browser localStorage (102 refs, no auth token seen), Cloudinary for photos.
- Auth: Firebase Google sign-in. api/session/route.ts:15 verifies the ID token; line 21 sets HttpOnly, SameSite=Strict, Secure in production. api/notify/route.ts:56 verifies the cookie.
- Owner and partner emails are hardcoded in firebase/database.rules.json (lines 3-4, 56-57).
- AI: local Ollama at 127.0.0.1:11434 (qwen models). No live OpenRouter or Gemini call path found; the only hit is a docstring at apps/local-core/services/privacy_sanitizer.py:4.

## Legal, icons, tests, docs, desktop
- Legal: no /privacy or /terms route. Privacy copy is in-app only (PrivacySettings.tsx).
- Icons: public/icon.png and apple-icon.png are 1024x1024; manifest.json declares 192 and 512 for the same file.
- Tests: 93 web tests (node --test; checkpoint says pass, not re-run). Local core: test_assistant_policy.py. Root test_milestone1_verification.py is stale.
- Docs: README.md, ARCHITECTURE.md, walkthrough.md, continuation_checkpoint.md. AGENTS.md, CLAUDE.md, GEMINI.md are identical copies of the global directive. No .sir/CHECKPOINT.md.
- Desktop: no AHome shortcut found. Launchers in infra-daemons/ (launch_sanctuary_stack.vbs, launch_silent_core.vbs).

## Scores (0-5)
- Architecture 3: trust boundaries documented (ARCHITECTURE.md); dev auth boundary still open.
- Code quality 3: lint 0 errors (checkpoint); 10 files over 300 lines; 12 em-dashes in web src.
- Security 2: session cookie correct; provider keys in env files; 4 history commits with key-shaped strings.
- UX/design 3: six tabs, empty states per checkpoint; 5-state coverage not audited.
- Performance 2: not measured; 459-line FocusSoundSynthesizer.tsx; images unoptimized (next.config.ts).
- Completeness 3: 5 production blockers listed in checkpoint.
- Store readiness 1: no Tauri or Capacitor code, no legal routes, no CI.

## Red flags
1. apps/web/.env.local holds GEMINI_API_KEY, OPENROUTER_API_KEY, TELEGRAM_BOT_TOKEN, FIREBASE_PRIVATE_KEY. apps/local-core/.env holds OPENROUTER, GEMINI and TELEGRAM keys. Root ahmed-habiba-1ef3d580b61d.json matches a service-account pattern (gitignored, not opened). None tracked. Values not printed.
2. Git history: 4 commits add key-shaped strings across 6 files. firebaseClient.ts:26 is likely the public Firebase web key. Checkpoint says Telegram and OpenRouter need rotation.
3. NEXT_PUBLIC_GEMINI_API_KEY in apps/web/.env.local: unreferenced, but would be inlined if used.
4. public/_headers (CSP, HSTS) is Netlify or Cloudflare format; Vercel ignores it, and next.config.ts has no headers(). No vercel.json. Verify in dashboard.
5. apps/web/package-lock.json and root lock both parse as JSON. Semantic check needs npm ci (not run).

## Upgrade size
M to production-ready web. L if Tauri or Capacitor wrappers are wanted.

## Top 5 fixes
1. Rotate OpenRouter, Gemini, Telegram keys (owner action); purge the 4 history commits; keep server secrets in Vercel and local env only; delete NEXT_PUBLIC_GEMINI_API_KEY.
2. Move security headers into next.config.ts headers() or vercel.json; drop public/_headers.
3. Replace hardcoded owner emails in RTDB and Firestore rules with custom claims.
4. Add CI (npm test, npm run lint, pytest); delete the stale root test file.
5. Split the 10 over-300-line files; remove 12 em-dashes; fix manifest icon sizes.
