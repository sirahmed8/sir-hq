# Inventory: SIR ModPack and SIR Mods for GTA V (2026-10-29, scout, read-only; nothing built, run or tested; shortcut targets not verified)

## SIR ModPack (`sirahmed8/SIR-ModPack`, PUBLIC, main, 9 commits, clean; 16.9 GB on disk)
Minecraft 26.2 launcher, installer and server manager. Ships `SIR_Apps_Suite.zip` (4 exe/ico, 120 MB; sha256 in manifest.json). Stack: PyInstaller specs, pywebview, Next 16 in `website-next/` (gitignored, so the site is untracked). Tests: `tests/` (37 entries) + `tests_e2e/test_e2e_suite.py`; no CI. Licence: custom "SIR Platform License" (not OSI). `development/PrismLauncher-develop` (GPL-3, gitignored).
Red flags: `EULA.md:19-21` describes ASM transforms of the Minecraft base JAR on the user's machine (EULA/redistribution risk, Mojang/Microsoft disclaimers present); `QA_CERTIFICATION.md` says "100% PASS, zero bugs" with no reproducible output; "144+ FPS" has no benchmark; README says "Verified & Signed" with no evidence (nothing fake: remove or prove); two `accounts.json` files were tracked in history, later untracked (commit fe08271; history rewritten 2026-10-29 and a backup bundle kept).
Scores: architecture 3, code 2, security 2, UX 2, performance 1, completeness 2, store 1.

## SIR Mods for GTA V (`sirahmed8/sir-mods-for-gta-v`, main, 10 commits, clean)
Closed-source GTA V mod suite: Electron installer (Electron 34), Next 16 portal (`web-portal`), mod manifest, AI NPC server (`LosSantosAliveServer`, @google/genai, ws). 7 test suites, 28 top-level tests vs README's "79"; no CI.
- **CRITICAL: forgeable admin.** `proxy.ts:14-44` only checks the cookie is 20+ chars or a Bearer header exists; the cookie is set from client JS (`app/admin/login/page.tsx:35`) as `sirmods_admin_<uid>_<ts>`; admin routes (`app/api/admin/subscriptions`, `inquiries`) have no auth check of their own. Anyone can set a cookie and read/modify subscriptions and inquiries.
- Tracked `.env` files (names only): `LosSantosAliveServer/.env`, `mod-distribution/staged/LosSantosAliveServer/.env`, `web-portal/.env.production`.
- Tracked third-party DLLs with no licence files: ScriptHookV (Alexander Blade, manifest.json:192-203), MinHook, dinput8, about 87 script DLLs; redistribution rights unverified. EULA says not for GTA Online.
- Desktop: 6 .lnk incl. duplicates (Oct 4 and Oct 26 names).
Scores: architecture 3, code 2, **security 0**, UX 3, performance 2, completeness 2, store 1.

## Merge assessment: not one repo now
Same owner and audience, but separate launcher, installer and portal; different licences (custom vs "Proprietary") and different game-EULA risk. Shared pieces to extract later: auth, legal templates, icons, admin guard. Fix the GTA V admin auth first (Wave 0), then decide on a shared hub. Upgrade size: ModPack L (legal), GTA V L.
