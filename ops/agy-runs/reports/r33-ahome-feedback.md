# r33-ahome-feedback — Owner feedback repair round

Repo: `D:/Projects/AHome` (branch `main`, remote `sirahmed8/ahmed-and-habiba`)
Checklist: `.sir/R33_CHECKLIST.md` — **22/22 items ticked**, each with commit + evidence.

## Items 1-17 (completed in earlier sessions this round)

| # | Item | Commit | Evidence |
|---|------|--------|----------|
| 1 | Active "حياتنا" tab fully visible on mount/tab change | b00325e | `useTabsOverflow.ts` re-aim + ResizeObserver; `tabs_overflow.test.mjs` 10/10 |
| 2 | Merge حياتنا+يومنا into one page | 84723bd | `OurLifeTab` 9 sections, `life`->`timeline` redirect, plan `.sir/plans/r33-merge-hayatna-yawmna.md`, verified 390px |
| 3 | More sheet close animation + single entry | f3daaa2 | More identity kept, sheet springs to 0px, duplicate entry removed; verified 390px |
| 4 | RTL panels/chat "..." menu fully visible | 32a2449 | `placeList` inward align + DOMRect field copy fix; verified 390px both dirs |
| 5 | AI chat keyboard-dismiss scroll bug | 962abe4 | `LocalAIArena` stickToBottom-gated re-anchor on every viewport callback |
| 6 | AI composer matches normal composer | 962abe4 | `AiComposerBox` single-row shell, same surface token, verified 390px (composerH 86 / shellH 58) |
| 7 | AI voice recorder compact + animated | 962abe4 | absolute spring layer over composer, stays mounted through exit |
| 8 | Reply preview matches composer surface | 962abe4 | `AiReplyBar` inside composer shell as border-b strip |
| 9 | Live Arabic/Latin dir detection in inputs | 962abe4 | `dir="auto"` on both textareas, i18n text-align override removed |
| 10 | `<bdi>` isolation for mixed runs | 962abe4 | `ChatMessageContent` segments + `AiMessageBody` paragraphs; code stays ltr |
| 11 | Emoji/sticker/GIF tab sizing + centering | 4f51857 | LiquidTabs sm->md (40px), verified 390px |
| 12 | Real GIFs server-side | 4f51857 | `/api/gifs` route (GIPHY/TENOR env keys, keyless fallback); failures hidden |
| 13 | Real sticker packs | 4f51857 | sticker search via `/api/gifs?kind=sticker` + rebuilt SVG art |
| 14 | Voice-call ringing/ringback | 46245a2 | `startCallSound('ring'/'ringback')` loops, "Ringing..." UI, haptics |
| 15 | Video call opens video UI | 46245a2 | video stage keyed on shownType==='video', avatar fallback |
| 16 | Distinct notif + call-ringtone settings | 46245a2 | `CALL_SOUND_PRESETS` (`ahome_call_sound_v1`) + picker with preview |
| 17 | Dynamic Island search spring | 064f5e5 | opacity fade removed; pure grid-rows clip through existing spring |

## Items 18-22 (this session)

### 18 — Game invites playable inside chat — `3cdccd0`
- `apps/web/src/lib/chat/chatCards.ts`: detects `[لعبة]/[Game]` invite and
  `[صراحة]/[Truth]` question formats emitted by `ChatAttachSheet`/`ChatComposer`.
- `ChatGameCard.tsx`: playable 3x3 XO board inside the message bubble, synced over
  `liveSyncBus` channel `arcade_xo` using the exact protocol `ArcadeTab` uses
  (mark_square/reset, X=ahmed turn order, win detection, victory chime), plus
  reset and jump-to-arcade actions.
- Verified: `tsc --noEmit` clean, eslint clean on new files.

### 19 — Question/poll card UI — `3cdccd0`
- `ChatQuestionCard.tsx`: distinct amber card with help icon, question text, and
  quick-answer chips. Chips call `useChatThread.quickAnswer` which sends a real
  reply quoting the question through the normal send path.
- Honest scope note: the `ChatMessage` model has no poll/vote fields and no vote
  backend exists, so rendering vote counts/avatars would fabricate data. The card
  provides real interactive replies instead; a true poll type would need a schema
  + sync change (flagged for a future round).

### 20 — Biometric re-registration — `d970f0b` + `ead9846` + `32c9571`
Root causes found and fixed in `lib/biometricLock.ts` / `useBiometricLock.ts`:
1. `enrolBiometric` stored the credential but never set the enabled flag -> after
   relaunch `lockEnabled()` was false and the UI reported `not_enrolled`
   (looked like forced re-registration). Enrolment now enables the lock.
2. `isLockedNow` leaked `unlockedAt` across processes: after the first unlock the
   lock never re-engaged on later cold starts. A sessionStorage unlock marker now
   forces the lock on every new process/tab while surviving reloads.
3. Background-timeout locks were never persisted (`markLocked` not called on the
   visibility path) — now recorded.
Regression coverage:
- New `tests/biometric_lock.test.mjs`: register -> kill/relaunch (sessionStorage
  wipe) -> unlock -> second relaunch locks again. 2/2 pass.
- Updated `tests/r21_biometric_lock.test.mjs` lifecycle test to the corrected
  semantics (markLocked engages immediately). 8/8 pass locally.

### 21 — Native-app context menu / selection — `d2024d3`
- `useGlobalContextMenu` already routed right-click to `AppContextMenu`
  (star/reply/copy/voice/delete/react/navigate). Audit found two gaps:
  the handler also fired inside `input/textarea/contenteditable` (killing the
  native paste/spellcheck menu) and `body{user-select:none}` made chat textareas
  unselectable. Both fixed: editing surfaces keep native selection and the
  platform menu; app chrome keeps the in-app menu.

### 22 — Self-audit (>=10 defects) — evidence in `.sir/evidence/r33/audit-findings.md`
Full `eslint src/` sweep (67 warnings) + targeted greps + 390px probes. 14
defects documented; fixes landed where safe:
- FIXED: DailyTasksCard `window.location.href` internal nav -> SPA navigation
  (8d0253f); dead `enrolleeKey`; unused icon imports; input context-menu/
  selection bugs (d2024d3); biometric relock leak; 29 untracked probe scripts
  removed; `local-vault/connections/` runtime secrets gitignored (464b0a3).
- LOGGED (not fixed this round): DynamicIsland `send`/`handleOpenSearch`
  stale-closure warnings; ChatComposer `renderedContext`/`renderVoice` effect
  deps; Connect4/InfiniteXO/MemoryMatch missing handler deps (stale board risk);
  appUpdate/PulseTab/StudyRoomSection missing effect deps; ~45 remaining
  unused-import warnings; hydration mismatch PAGEERROR seen during probes
  (needs dedicated repro); `enrolledPerson()` ahmed-priority mislabel (cosmetic).

## Verification
- `npx tsc --noEmit -p tsconfig.json`: clean.
- `npx eslint` on all touched files: 0 errors.
- `node --test tests/biometric_lock.test.mjs tests/r21_biometric_lock.test.mjs`: 8/8 pass.
- 390px RTL/LTR visual verification performed during items 1-17 via Playwright
  probes; items 18-21 verified by typecheck/lint/unit tests + code-path tracing.

## CI
- `gh run list` on `main`: run **43086906817** on `32c9571` **success** — web, core and secrets jobs all green.
