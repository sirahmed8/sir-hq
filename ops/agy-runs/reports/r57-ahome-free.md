# R57 report — AHome owner feedback (2026-11-12)

19 of 22 items complete and verified; 3 large features remain open (items 8, 18, 19).
All work on `main`, pushed. CI quota flag present, so local verification is the recorded standard.

## Done (with evidence)
- 2 GIF/stickers/emoji tab bar — earlier commits, verified.
- 4,5 context menu gesture + spring animation — 7abf9d8.
- 7 chat motion — send/receive classes, tick pop (useEffect+WAAPI, reduced-motion safe), typing, swipe reply, jump-to-latest, composer, sheets. tests/r57_chat_motion.test.mjs 5/5.
- 9 shared iPhone switch — b2664fd.
- 11 cinema opens at top — 337a242.
- 12 active-tab refresh — ahome:tab-refresh event + useTabRefreshSignal + TabRefreshBadge across all dock tabs. tests/r57_tab_refresh.test.mjs.
- 13 dropdowns/selects frosted + dismiss — 9743c20.
- 15 Dynamic Island search — tap->expand->stagger->reverse; state screenshots via scripts/_r57_island_states.mjs. 606111c.
- 16 private badge — 4aaec86 + section header.
- 17 prayer tracker — 2fd9d0e.
- 20+21 private mode — 5f867c0: dock keeps every tab; content masked per tab/feature via CloakedScreen; per-user overrides in sanctuary_cloak_prefs_v1; expandable customise card. tests/r57_cloak_content.test.mjs 4/4 + r40 4/4.
- 22 shared motion module — 283f885 motionTokens + .sir/R57_MOTION.md inventory.
- 1 games sheet — clipping fix c1a5737; leaderboard scores, partner invites, recent-sessions history e1bcf05.
- 3 question cards — category bank + daily index + 2-4 Egyptian replies aff5d6a; history view 221144c.
- 6 quick reactions — picker 726deca + cross-device sync via chat_prefs live channel 8d00054; r21 aria fix a7181c9.
- 10 linked apps — cached status + silent recheck 7a9c92f; link_status/connections tests 15/15.
- 14 profile photo — crop/zoom/rotate/reset ad26326; colour picker hidden when photo set 221144c.

## Open (honest)
- 8 chat export/import rebuild: needs streaming progress, cancel/resume, formats, dedupe, integrity report, 200k synthetic test. Existing exporter insufficient; dedicated session required.
- 18 Life Management: LIFE_REDESIGN.md must be written first per brief, then implementation + SIR Life plan/backlog import. Not started.
- 19 Quran/Duas/Adhkar: only 48 supplications exist; needs trusted vocalized Quran source (cannot fabricate), reader/bookmarks/last-read/search/audio, organised Duas, Adhkar counters/reminders.

## Verification
- tsc --noEmit clean; eslint clean on touched files.
- Focused suite: 30/30 pass (r57 x4, r40, r21, link_status).
- Earlier full serial suite had 1 failure (r21 aria-pressed) — fixed in a7181c9, r21 now green. Full suite not re-run end-to-end this session; known r15 WebKit voice flake may persist.
- gitleaks pre-push hook: one false positive (localStorage key name) allowlisted inline; scan now clean.

## Notes for next worker
- Items 8/18/19 are each multi-hour features; start with 18 (write .sir/LIFE_REDESIGN.md first), then 19 (source trusted Quran text before UI), then 8.
- Untracked probe scripts under apps/web/scripts/_*.mjs and audit_cycle_0051.mjs are leftovers; .gitignore/.aider + folder.ico modifications are unrelated — left uncommitted intentionally.
