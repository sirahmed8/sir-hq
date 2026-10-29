# Inventory: SIR Optimizer (2026-10-29, read-only scout)
## What it is
Windows performance suite (RAM compaction, GPU shader purge, Lenovo Fn+Q power sync, 87-point health check, installer) plus a Next.js site (PulseTools-Web). Audience: Windows 10/11 x64 users, mainly Lenovo laptop owners. Pricing in EGP and USD (Pro 249 EGP/mo, 1,999 EGP/yr per AISupportChat.tsx system prompt).
## Build and run
- `tsc --noEmit` in PulseTools-Web (scratch tsbuildinfo): exit 0.
- No `.next`; `out/` exists on disk (gitignored). No build run.
- Live: https://sir-optimizer.vercel.app returned 200. https://siroptimizer.com returned no response (curl 000) from this sandbox.
- .NET apps target net8.0-windows; dotnet SDK 10.0.403 present. Not built.
## Stack
Next.js ^16.2.11, React ^19.2.8, Tailwind 3.4, framer-motion 12, Firebase 12 (Auth, Firestore, RTDB, Analytics), TypeScript ^5.7. PowerShell engine scripts. Firebase hosting site `sir-optimizer`, public dir `out`.
## Repo health
- Remote github.com/sirahmed8/sir-optimizer, branch main in sync. Branches: main, pre-sir-snapshot.
- Last commit 9e0dff5 (2026-10-26). 29 commits. Working tree clean. No stash.
- 268 tracked files. Tracked binaries: .exe and .zip in PulseTools-Web/public/downloads and apps/*/bin, though .gitignore lists both.
- Nested `public_repo/.git` inside the repo.
## Structure and platforms
apps/ (4 .NET GUI apps + PS engines), PulseTools-Web/ (site), LenovoPowerSync/, bin/ (shipped exes), scripts/ (VBS/BAT launchers), tests/. Windows x64 only; web portal in any browser.
## Data and auth
- Firestore (users, waitlist, transactions, metrics) and RTDB; rules in firestore.rules and database.rules.json.
- localStorage holds user profile, AI quota, AI metrics, waitlist, transactions (cloudStore.ts).
- Firebase Google sign-in (authContext.tsx). Owner = client-side email match with hardcoded fallback (authContext.tsx:28, :62). Any user can flip `isOwner` via toggleOPMode (authContext.tsx:145-155), which syncs to Firestore.
## AI usage
- Client calls Gemini and OpenRouter directly with NEXT_PUBLIC_* keys (AISupportChat.tsx:169-208).
- Server route POST /api/chat (route.ts:68-187): CORS `*`, no auth, no rate limit, no owner check.
- 5/day free quota is localStorage only (cloudStore.ts:182-212).
## Legal and icons
- /privacy, /terms, /refunds, /cookies pages exist. Refunds has no cancellation or auto-renew terms. Privacy has no sub-processor list or DPA mention.
- Analytics initialised without consent gate (lib/firebase.ts:37).
- public/icons holds 5 near-duplicate icon sets.
## Tests, CI, docs
tests/Run-AllTests.ps1 plus 6 Verify-*.ps1 scripts. No .github, no CI. README badge claims 87/87 (not verified). Docs: README, ARCHITECTURE, CHANGELOG, 4 policy docs, EULA.
## Desktop launchers
C:\Users\a7med\Desktop\SIR Optimizer\ holds 9 .lnk files: SIR Optimizer, SIR Optimizer Installer, SIR Optimizer Web Portal (target has no "Optimizer" keyword match), SIR Doctor, SIR Health Doctor, SIR Installer, SIR PowerSync, Start/Stop Showcase Site.
## Secrets (presence only)
- PulseTools-Web/.env.local and .env.production exist on disk, untracked. Contain Gemini, OpenRouter and Firebase keys. Values not read.
- Commit a1612cf ("remove .env.production") shows it was tracked in history. Treat values as exposed; rotate.
## Scores (0-5)
- Architecture 2: two stacks, localStorage-backed business logic.
- Code quality 2: Math.random IDs, silent `.catch(() => {})`, 3 em-dashes in src.
- Security 1: public keys in bundle, open /api/chat, client-side owner bypass, `users` readable by anyone.
- UX/design 3: bilingual EN/AR, theme, command palette.
- Performance 3: Next 16; not measured.
- Completeness 2: owner page writes simulated transactions with random emails (owner/page.tsx:93-100).
- Store readiness 1: tracked binaries, no refund/DPA coverage, no CI.
## Red flags
1. Gemini and OpenRouter keys in client bundle (AISupportChat.tsx:169-170).
2. Unauthenticated /api/chat with CORS `*` (route.ts:51-66).
3. Self-grant OP mode bypasses paywall and AI quota (authContext.tsx:145-155, featureFlags.ts:50).
4. Simulated payments written to real `transactions` (owner/page.tsx:93-100; OwnerFloatingBar.tsx:23-30).
5. Firestore `users` and `metrics` readable by anyone (firestore.rules:8, :31).
6. .env values in git history (a1612cf).
## Overlap
SIR Controller, SIR AI: no shared code seen. Laptop manager and PowerSync both cover Lenovo power/thermal scope; verify before merging. PORTFOLIO.md line 23.
## Upgrade size: L
1. Rotate keys; move AI calls server-side behind auth and rate limit.
2. Server-verify owner via Firebase custom claims; remove toggleOPMode and hardcoded email.
3. Remove simulate-payment buttons and mock writes.
4. Tighten Firestore/RTDB rules.
5. Move binaries to GitHub Releases; add CI for tsc and Verify scripts.
## Business ops
Partly: waitlist, transaction log and EGP pricing exist. No payment provider keys (Paymob/Fawry), no CRM, no real revenue data; owner analytics are simulated.
