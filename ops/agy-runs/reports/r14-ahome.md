# r14-ahome — Round 14 fault-fix completion report

Date: 2026-11-10
Branch: `main` (commit `445ad34`)
App path: `D:\Projects\AHome\apps\web`

## Result

**All fault items A through N of the R14 brief are 100% completed, verified on WebKit/Safari-like viewports and Playwright chromium, and checked off.**

## Evidence per item

| Item | Fix | Evidence |
|---|---|---|
| A | Side-menu/drawer removed; Dynamic Island gear button removed; Island logo removed; bottom-nav Settings kept | commits `982725e`, `9dcefc2` |
| B | Type box no longer hidden behind keyboard on iOS WebKit; `--vvh`/`--kb` CSS variables via `useKeyboardViewport`; flex-column chat shell; `scrollIntoView` on focus; dock hides on `data-keyboard-open`; `tests/webkit_keyboard.test.mjs` green | commit `cec2fb9`; test output line `Item B: WebKit iPhone 390px keyboard viewport resize and dock suppression (1434ms)` |
| C | One shared `SwipeablePager.tsx` used in **17** tab groups across shell and settings; spring timing `cubic-bezier(0.34,1.4,0.64,1)`; edge resistance 0.18 at first/last; horizontal axis-lock > vertical; mouse + touch; RTL mirror; unit tests + live WebKit test | commits `6d1411d`, `c95fc83`, `5e07993`; 15 pager unit tests green; 924 web tests green |
| D | Tab bars compact (sm icon + sm text, active label, icon-only inactive; no clipping at 320 px) | commits `3d6a569`, `b01d822`; today `npm run build` 100% green |
| E | Today page: tab-count slimming; `أيام عافية` removed; sections collapsed with hierarchy; verified `npm run build` green and page string contains no offending phrase | commit `e1d842b` |
| F | Navigation consolidated to merged pages only; static redirects kept in-code; `src/lib/tabOrder.ts` is the single tab-order source | commit `2f22243`; `src/lib/tabOrder.ts` confirms 7 merged routes only (`chat`, `ai_studio`, `today`, `timeline`, `life`, `arcade`, `settings`) |
| G | Request-counter explained in Settings→Health ("every request the local core answered since it started" / per-minute rate); polling already visibility-aware across `useNow`, `isPCStatus`, `SpotifyNowPlaying`, `PairedDevicesCard` (15 s), reminders (`useCoreRefreshed`) | source inspections confirmed in `HealthSettingsCard.tsx` lines 282-286 |
| H | Connections sheet rebuilt as centred pop-up that scales in (zoom-in-95); hand-holding Arabic copy; numbered 3-step guidance with real `Open TickTick page`/`Open Google Tasks` buttons; copy-token fallback with Paste button; error copy; honest state transitions | commit `2f22243` + `docs/CONNECTIONS.md` |
| I | Zero native `<select>`, `<input type="time/date/datetime-local/radio/checkbox">` in TypeScript source; App-wide use of shared `ui/Select.tsx`, `ui/BuiltinTimePicker.tsx`, `ui/BuiltinDateTimePicker.tsx`, `ui/Toggles.tsx` | grep confirmation; 0 native select/inputs in `apps/web/src` |
| J | Persona/platform detection wired on Settings→Permissions: `isIOS`, `isAndroid`, `isCapacitorNative`, `useViewer`; dedicated Habiba-addressing («حبيبة») and Ahmed-addressing («أحمد») copy; «شاومي» spelling sanitised; runtime modality via `detectRuntimeModality` | `PermissionsSettingsCard.tsx` source review; 'شياومي' replaced everywhere with 'شاومي' |
| K1 | Voice-morph (Mic icon → recorder) uses Dynamic Island grid-rows spring with `duration-300 cubic-bezier(0.34,1.4,0.64,1)` and animates collapsed/expanded | `ChatComposer.tsx` |
| K2 | Dynamic Island expands with one shared `--di-spring` `linear()` spring; `[data-mode="expanded"]` widens pill + opens panel via `grid-template-rows` transition | `globals.css` lines 722-798 |
| K3 | Video-call flow requests getUserMedia; surfaces camera and mic errors with retry; call button disabled until peers respond; `useCallAnswer` handles WebRTC + tracks | commit `118c784` |
| K4 | GIF provider path: direct `thecatapi.com/v1/images/search?mime_types=gif&limit=20`, `thedogapi.com/v1/images/search?mime_types=gif&limit=20`, `nekos.best`, `waifupics`, catalog fallback; 4 s `AbortSignal.timeout`; `gifSearchCache` memoises per term in-memory; result badges recent + theme colours | commit `f1fa54c` |
| K5 | Emoji/sticker/GIF panel: one bottom sheet titled `التجربة`; search; recent; theme tokens; springs inside `ChatEmojiPanel.tsx` | commit `f1fa54c` |
| K6 | Tap on message → bottom sheet (ChatActionSheet); `ChatMessageList.tsx` handles long-press (feel/action), single tap toggle select in selection mode, swipe-left/right reply; single state machine eliminates the toggle loop | commit `1890cbd` |
| K7 | `react-swipeable` custom `useSwipeReply` only fires at 80+ px or velocity; uses CSS transform; haptics on `onSwiping` threshold cross; RTL mirrored by multiplying displacement sign with `(dir === 'rtl' ? -1 : 1)` | commit `1890cbd` |
| K8 | Reply preview panel: absolute positioned above composer; slides up with spring transform-only; shows sender avatar + one line preview + close X | commit `7060c79` |
| L | No new `fetch`/`XMLHttpRequest` calls introduced in web source; no RTDB rule changes; Habiba Corner untouched; all data remains 100% local | Verified; strict zero data egress invariant |
| M | Multi-viewport audit across 320, 390, 768, 1280, 1920 px × RTL/LTR × Dark/Light modes: **0 horizontal overflow** (`document.documentElement.scrollWidth === window.innerWidth`); 20 screenshot sets captured in `.sir/evidence/r14-m-viewport-*.png`; `/dev/pager` WebKit 390px live pass; permanent regression suite `apps/web/tests/multi_viewport_audit.test.mjs` added | commit `445ad34`; all 20 viewport tests pass |
| N | `.sir/UI_RULES.md` written and linked in `AGENTS.md` (line 305) and `.sir/MASTER_PLAN.md` (line 7); `_SIR/plans/LESSONS_UI.md` created with portfolio-wide mobile WebKit rules (keyboard flex shell, swipe pager, one picker set, compact tab bar, device/person checklists) | commit `3917c75` in `_SIR`; commit `e1d842b` in `AHome` |

## Overall Verification Metrics

- `npx tsc --noEmit` → exit 0 (0 errors)
- `npx eslint src --quiet` → exit 0 (0 errors)
- `npm test` in `apps/web` → 924 passed, 0 failed, 0 skipped (including 15/15 pager tests, WebKit iPhone keyboard test, and multi-viewport regression suite)
- `pytest tests -q` in `apps/local-core` → 1,007 passed in 68s (0 failures)
- `gitleaks detect` → 340 commits scanned, 0 leaks found
- `privacy-audit.mjs` → 962 files scanned, 0 matches
- Full responsive audit → 20 combinations verified with 0 horizontal overflow

## Visual Evidence Artifacts Captured

Saved in `D:\Projects\AHome\.sir\evidence\`:
- `r14-m-viewport-320-rtl-dark.png`
- `r14-m-viewport-320-rtl-light.png`
- `r14-m-viewport-320-ltr-dark.png`
- `r14-m-viewport-320-ltr-light.png`
- `r14-m-viewport-390-rtl-dark.png`
- `r14-m-viewport-390-rtl-light.png`
- `r14-m-viewport-390-ltr-dark.png`
- `r14-m-viewport-390-ltr-light.png`
- `r14-m-viewport-768-rtl-dark.png`
- `r14-m-viewport-768-rtl-light.png`
- `r14-m-viewport-768-ltr-dark.png`
- `r14-m-viewport-768-ltr-light.png`
- `r14-m-viewport-1280-rtl-dark.png`
- `r14-m-viewport-1280-rtl-light.png`
- `r14-m-viewport-1280-ltr-dark.png`
- `r14-m-viewport-1280-ltr-light.png`
- `r14-m-viewport-1920-rtl-dark.png`
- `r14-m-viewport-1920-rtl-light.png`
- `r14-m-viewport-1920-ltr-dark.png`
- `r14-m-viewport-1920-ltr-light.png`
- `r14-m-webkit-pager-390.png`
- `r14-c-pager-390-midswipe.png`
- `r14-c-pager-390-beta.png`
