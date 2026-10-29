# SIR Controller: Phase 3.1 inventory (2026-10-29) (read-only; no builds; no secret values printed)

## What it is and who it is for
Windows gamepad translator (x360ce fork): maps DS4, DualSense, Joy-Con, Pro, wheels to virtual Xbox 360 pads via ViGEmBus. Includes a setup installer (profiles into game folders) and a Next.js web portal (web/) with EN/AR pricing, waitlist, /owner page. Audience: PC gamers (README.MD top). EULA.md names SIR Systems LLC.

## Build, run, live URL
- Not built this session. Evidence only: bin/Release, Installer/bin/Release, Tests/bin/Release exist; Tests/TestResults has 3 runs dated 2026-10-26; commit 0420cf6 claims 298/298 MSTest pass.
- Web: web/out present (static build); web/tests = 2 files, 7 test() calls, not run.
- Live URL https://sircontroller.app: curl from this machine returned exit 6 (DNS failure). Not reachable at check time.

## Stack
- App: WinForms WinExe, .NET Framework 4.6.2 (x360ce.csproj), Windows only, no MSIX found. Engine, Installer, Tests: net462 (MSTest).
- Web: Next.js 16.2.11, React 19.2.8, TypeScript ^5.7.3, Tailwind 3.4.17, firebase ^12.16.0, framer-motion ^12.42.2 (web/package.json).
- CI: .github/workflows/build.yml, windows-latest, dotnet 10.0.x. Builds Engine, App, Installer; runs tests excluding ui-interactive. Web not in CI.

## Repo health
- origin github.com/sirahmed8/SIR-Controller. Branches: main (= origin/main, 0 ahead/0 behind at last fetch), pre-sir-snapshot (same commit 0420cf6). No stash, worktree clean, 9 commits, last 2026-10-26 20:09 +0300.
- .git is 121 MB; about 20 binaries tracked (Resources/*.dll, *.exe, *.zip, web/public/downloads/*). Ignored locally: Share/, public_repo/, GameFiles/.

## Structure
- Root: x360ce.csproj (MainForm.cs 2148 lines), Engine/ (410 files, vendored JocysCom), Installer/, Tests/ (236 files), Common/, Controls/, Forms/, Resources/, Presets/, scripts/, docs/, web/ (61 tracked), .github/.
- Root has AGENTS.md, CLAUDE.md, GEMINI.md: three identical 20912-byte copies of the global directive. No project-specific agent rules.
- web/src layers: core, data, domain, presentation, app. Routes: /, /pricing, /privacy, /terms, /refunds, /cookies, /downloads, /owner, /thank-you; api/chat, api/webhook.

## Platforms, data, auth
- Data: desktop uses ini/xml presets and gz resource DBs. Common/CloudClient.cs (260 lines) has no hardcoded host. Web: no Firestore or SQLite call found in web/src/data, domain, core.
- Auth: web Firebase SDK listed. Owner check is client-side (web/src/domain/auth.ts:7-10). No httpOnly cookie code found.

## AI usage, legal, icons
- AI: api/chat/route.ts calls Gemini 1.5 Flash when GEMINI_API_KEY is set, else local fallback. OPENAI_API_KEY is in .env.example only.
- Legal routes: web/src/app/{privacy,terms,refunds,cookies}/page.tsx. Root has PRIVACY_POLICY.md, TERMS_OF_SERVICE.md, REFUND_POLICY.md, COOKIE_POLICY.md, EULA.md; docs/ has copies (drift risk). Grep: 2 hits for sub-processor, DPA, SOC 2 or no-training terms; not reviewed further.
- Icons: app.ico, icon.ico, installer.ico, stop.ico. README calls installer.ico "AI-generated"; provenance and license unverified.

## Tests, docs, launchers
- Tests: MSTest (Tests/x360ce.Tests.csproj); Run-Tests.ps1:73 excludes ui-interactive. Web tests are not in CI.
- Docs: README.MD, ARCHITECTURE.md, CHANGELOG.md, SECURITY.md, llms.txt, docs/ (24 files). No .sir/CHECKPOINT.md; root continuation_checkpoint.md dated Oct 6.
- Desktop folder "SIR Controller" has shortcuts matching this project: App, Setup, SIR Setup (Auto-Installer), Stop SIR Cloud Web. README's "Start SIR Cloud Web" and "Rebuild Latest Binaries" did not match. Not in Start Menu.

## Scores (0-5)
- Architecture 2: WinForms god-form MainForm.cs (2148 lines); web layering is clean.
- Code quality 2: 5 TODO lines in C#; 8267-line generated designer file; 0 mock hits in web/src.
- Security 1: unsigned webhook returns success (webhook/route.ts:43); client-side owner gate; Gemini key in URL (chat/route.ts:31).
- UX/design 3: EN/AR and RTL present, cookie consent, waitlist modal (WaitlistModal.tsx:110). Not screenshot-tested.
- Performance 2: README claims 1000 Hz and 0.98 ms; no benchmark found.
- Completeness 2: payments not wired; analytics, refunds, GDPR requests in localStorage.
- Store readiness 1: LGPL vs EULA conflict; live URL unreachable; tracked binaries.

## Red flags
1. Webhook accepts any POST and returns status success (route.ts:43). Header used only as idempotency key (line 9). No signature check.
2. Owner gate is client-side. Hardcoded fallback owner email in web/src/core/constants.ts:7 (value not printed). Env name is OWNER_EMAIL, not OWNER_EMAILS or OWNER_UIDS.
3. Refund and GDPR requests saved only to localStorage (refunds/page.tsx:26-38; privacy/page.tsx:42-51).
4. Owner analytics read localStorage (data/analytics-store.ts:85). Not real telemetry.
5. Gemini key sent in URL query (chat/route.ts:31). Leaks into logs and proxies.
6. Chat fallback hardcodes tokensUsed 42 (chat/route.ts:77).
7. License: Documents/License.txt is LGPL-3.0; EULA.md grants a revocable license with no profit redistribution; docs/EULA.md says LGPL prevails for licensed code. Needs counsel review.
8. Secrets: git grep for key patterns (excluding .md and .resx) found no hits. web/.env.example names keys only. No web/.env present.

## Overlap, business ops, upgrade
- SIR Optimizer: README Setup Auto-Optimizer (game scan, profile deploy) overlaps Installer/SetupEngine*.cs.
- Laptop manager: Common/HardwareOptimizer.cs:19 (hardware tuning). Compare before any merge.
- SIR AI: web chatbot calls Gemini directly (chat/route.ts).
- Business ops: partial. Pricing, legal pages, waitlist. No invoicing, tax, CRM, support queue; payments not wired.
- Upgrade size: L for web (auth, data, payments, legal execution). M for desktop-only fixes.

## Top 5 fixes
1. Verify webhook signatures (Stripe, Paymob HMAC); return 401 on failure; persist entitlements server-side.
2. Server-side owner and entitlement checks via verified Firebase ID token; OWNER_EMAILS and OWNER_UIDS from env; remove hardcoded fallback.
3. Move refund, GDPR deletion, quota and analytics from localStorage to Firestore or SQLite via API routes.
4. Send Gemini key in x-goog-api-key header; enforce quota on the server.
5. Decide license path (LGPL vs EULA) with counsel; untrack binaries; record third-party licenses (ViGEmBus, HidGuardian, SharpDX, NetZ, DXTweak).
