# Inventory: SIR Content Creation Studio (2026-10-29, scout, read-only, tests not run)

**What:** offline-first AI video studio for Shorts and long-form (Electron + FastAPI on 127.0.0.1:5000 + Remotion). Repo `sirahmed8/sir-content-creation-studio`, main clean, last commit 850652f (2026-10-26), 29 remote branches.
**Stack:** Python 3.10 pin vs CI 3.11 vs .venv 3.13.11 (mismatch); Remotion 4, React 18.2; vanilla JS UI; Firebase Hosting site `sir-content-creation-studio` (URL not verified).
**Business ops:** no ByteVibeHQ or "SIR Media" spec; ByteVibe appears only in demo props and legal text; no social publishing code.
**Tests/CI:** 120 test files; CI runs lint and test on Ubuntu (not run here). Electron binary not found in root node_modules.

## Scores (0-5)
| Area | Score | Evidence |
|---|---|---|
| Architecture | 3 | clear app/engine split, Remotion renderer |
| Code quality | 2 | version drift, generic root agent files |
| Security | 1 | personal state tracked; no server-side token check |
| UX/design | 2 | vanilla JS UI |
| Performance | 2 | not measured |
| Completeness | 3 | broad feature set |
| Store readiness | 1 | unsigned installer, stale dist |

## Red flags
1. Personal state tracked in git: `.studio_user_profile.json` (email, name, owner flag), `.studio_cloud_sync.json` (uid), `.studio_pro.json`, `studio_app/data/studio.db`, `out/audio/*.mp3`.
2. No server-side Firebase ID-token verification (0 hits for verify_id_token / firebase_admin); owner gating via OWNER_EMAILS/OWNER_UIDS/is_owner in 6 files.
3. `.env` (ignored, not tracked) holds about 40 provider key names. SECRETS.md lists 18 `curl-auth-header` hits under `.agents`/`.claude` skills, not yet checked for real secrets.
4. Installer unsigned; `dist/` Setup 1.0.0.exe dated 2026-10-04, older than the last source commit.
5. No "Launching Soon" payment fallback (0 hits) though payment SDK names appear in 5 files.
6. Start Menu .lnk targets a stale path `D:\Projects\Content creation\dist\win-unpacked\`.
7. Root AGENTS/CLAUDE/GEMINI.md are identical generic directives, not project context. LICENSE is 34 KB while package.json says MIT (unchecked).

## Upgrade size: M. Top 5 fixes
1. Untrack personal state and studio.db; purge history (S).
2. Verify Firebase ID tokens server-side before owner/pro gating (M).
3. Add a "Launching Soon" checkout fallback (S).
4. Align the Python version, fix the stale .lnk, rebuild dist (S).
5. Check the LICENSE file; unsigned installer stays unsigned until earnings allow a certificate (M, no budget).
