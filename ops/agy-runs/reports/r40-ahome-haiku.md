# r40 AHome report (haiku builder, brief R10: r38-ahome-haiku-prompt, 2026-11-12)

Local verification only (GitHub Actions quota flag). Commits pushed straight to main. Evidence: `AHome/.sir/evidence/r40-*.txt`.

## Done (commit id, what, how checked)

| Item | Commit | What changed | Checked |
|---|---|---|---|
| 1 Friends mode hides private screens | d634413 | Root cause: the cloak only masked some cards; the tab renderer and dock never read it. Now today, timeline, life, notes, calendar, dates, pulse, memories, ai_studio and corner show a neutral screen; the dock hides them. Chat, arcade and settings stay usable so the flag can be turned off. | `tests/r40_cloak_hides_private_tabs.test.mjs` (4 pass). Not checked on a phone screen. |
| 6 No presence dot while hidden | 213c199 | Partner header dot and island presence dot removed while cloaked. The page no longer forces partnerOnline to true. | `tests/r40_cloak_no_presence_dot.test.mjs` (3 pass). |
| 2 Apple-style switches | b9ae4e6 | Track 51x31, knob 27 px, 2 px inset, travel 20 px (JS and CSS share it), spring slide, 44 px tap target, RTL flip, role=switch kept. | `tests/r40_switch_geometry.test.mjs` (4 pass). Not checked on a phone screen. |
| 3 Profile without nickname | e461ce3 | Nickname removed from form, model and sheet. The empty sheet says "Habiba has not created her profile yet" (or the Arabic form) and never says "on this device". While names are masked, the sentence uses no name. Old saved profiles still load. | `tests/r40_profile_no_nickname.test.mjs`, updated `tests/r38_profile_model.test.mjs` (11 pass). |
| 4 Voice bar edges | 68d4b67 | Root cause of the clipping: the shell corner radius is 16 px, but the chat bar had 12 px side inset and the AI bar 8 px. Both now have 16 px. AI shell no longer uses transition-all. | `tests/r40_voice_bar_edges.test.mjs` (3 pass). Not checked on a phone screen. |
| 5 No scrollbar in chat and AI lists | dd49444 | `scrollbar-none` on the chat message list and the AI chat log (touch and wheel still scroll). | `tests/r40_chat_scrollbar_hidden.test.mjs` (3 pass). |
| 7 Dependabot (partly) | 1b9fbea | Root package.json overrides: @grpc/grpc-js 1.14.7 and uuid 11.1.1. Lock entries for the stale nested copies in apps/web were corrected. | `npm audit`: 20 findings to 8; high 4 to 0. |

Full local verification after the last commit: `tsc --noEmit` exit 0; lint exit 0 (0 errors, 112 pre-existing warnings); serial test suite 1000 tests, 999 pass, 1 fails (see below).

## Not done or partly done, and why

- **Item 4, r15 voice flake (still open).** `tests/r15_reply_voice.test.mjs` fails intermittently: the layer reads opacity 0 when the browser does not paint in time. Measured on the same machine: baseline 4 of 6 runs failed; with my frame-independent entrance attempt also 4 of 6. I reverted that attempt, because it did not change the rate. A probe shows the layer reaches opacity 1 in normal runs, and in headless WebKit recording is "unsupported" so the error bar stays open. Root cause not yet confirmed.
- **Item 7, remaining npm audit findings (8, all moderate).** typescript-eslint dev chain (minimatch 10.2.6): a scoped override needs a registry fetch of minimatch 11.0.1, not done this round. node-forge 1.4.2: fix 1.4.3 was published 2026-11-04, which is under the two-week age rule until 2026-11-18.
- **Item 8, games and audit loop (not started).** The WebGL layer for the other 3D games, per-game pause and levels, high-score chips, and the 10-defect audit at 320/390/768/1280 need more time than this round had. Nothing was marked done for it.
- **Screen checks.** Items 1, 2, 4 and 5 were checked by unit or static tests only. Nothing here was seen on a phone screen in this round.

## Notes for the owner
- A stray `apps/web/package-lock.json` exists outside git from an earlier `npm install` run inside apps/web. A deny rule covers it, so I did not touch it. It can be removed by you.
- The truth-or-dare game prompt still uses the word "nickname" in an Arabic game question. It is game content, not the profile, so I kept it.
