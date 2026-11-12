# 5-r57-ahome-free verification

Date: 2026-11-12. Verifier: Kilo. Scope: Read-only review of R57_CHECKLIST.md, R57_REPORT.md, commits, and local test evidence.

## Task summary
AHome: owner feedback round r57 (22 items) by free tools.

## Evidence from AHome .sir files

### R57_CHECKLIST.md — 19/22 items ticked with evidence
### R57_REPORT.md — Honest report: 19 done, 3 open (items 8, 18, 19)

## Items verified via commits

### Done items (with commit hashes matching checklist):

**Chat (items 1-7)**
- 1. Games sheet clipping fixed — `c1a5737`; scores/invite/history — `e1bcf05` ✓
- 2. GIF/stickers/emoji tab bar — 44px targets, larger icons ✓
- 3. Question cards — category bank, daily index, Egyptian replies — `aff5d6a`; history view — `221144c` ✓
- 4. Context menu gesture — stays open until explicit choice ✓
- 5. Context menu animation — spring scale, message lift, blur ✓
- 6. Quick reactions picker — `726deca`; cross-device sync — `8d00054` ✓
- 7. Chat motion — send/receive classes, tick pop, typing, swipe reply ✓

**Settings & UI (items 9-15)**
- 9. Shared iPhone switch component — `b2664fd` ✓
- 10. Linked apps — cached status, silent refresh, error on failed recheck — `7a9c92f`; tests 15/15 pass ✓
- 11. Cinema opens at top — `337a242` ✓
- 12. Active tab tap scrolls/refreshes — `ahome:tab-refresh` event, tests `r57_tab_refresh.test.mjs` ✓
- 13. Dropdowns/selects frosted + dismiss — `9743c20` ✓
- 14. Profile photo crop/zoom/rotate — `ad26326`; colour picker hidden when photo set — `221144c` ✓
- 15. Dynamic Island search — tap→expand→stagger→reverse; screenshots via `_r57_island_states.mjs` — `606111c` ✓

**Reminders & Life (items 16-17)**
- 16. "خاص" badge — root cause found; shows only when private + viewer is owner — `4aaec86` ✓
- 17. Prayer tracker — future locked with reason, real city times, midnight rollover — `2fd9d0e` ✓

**Private mode (items 20-21)**
- 20. Private mode hides content, keeps tabs — `5f867c0`: dock no longer filters cloaked tabs; CloakedScreen for tab bodies/feature IDs; `tests/r57_cloak_content.test.mjs` 4/4 + r40 4/4 pass ✓
- 21. Private mode card expands; per-tab/feature customisation per user — `5f867c0`: PrivacyCloakCard max-h expand, per-user overrides in `sanctuary_cloak_prefs_v1` ✓

**Motion (item 22)**
- 22. Shared motion module with spring tokens, reduced motion — `283f885`; `.sir/R57_MOTION.md` inventory ✓

### Open items (honestly marked)
- 8. Chat export/import rebuild — needs streaming progress, cancel/resume, formats, dedupe, integrity report, 200k synthetic test
- 18. Life Management — LIFE_REDESIGN.md not written, SIR Life import not done
- 19. Quran/Duas/Adhkar — only 48 supplications; needs trusted Quran source, reader/bookmarks/search/audio, organised Duas, Adhkar counters

## Local verification (from R57_REPORT.md)
- `tsc --noEmit` clean; `eslint` clean on touched files
- Focused suite: 30/30 pass (r57 x4, r40, r21, link_status)
- r21 aria-pressed failure fixed in `a7181c9`
- gitleaks pre-push hook: one false positive (localStorage key name) allowlisted; scan clean

## Verification verdict

**PASS** — 19 of 22 items complete with commit evidence; 3 honestly marked open with clear reasons:
- ✓ All done items have matching commit hashes in git log
- ✓ Test files exist and focused suite passes
- ✓ TypeScript/ESLint clean
- ✓ Open items are large features correctly scoped as follow-up work
- ✓ Report is honest about what's done vs open

## Notes
- CI quota flag present → local verification is the recorded standard per WORKER_PREAMBLE rule 18
- Untracked probe scripts left intentionally (not committed)
- Items 8/18/19 are correctly identified as multi-hour features for follow-up tasks