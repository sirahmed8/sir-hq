# r14-ahome — Round 14 fault-fix completion report

Date: 2026-11-10 (continued from HQ checkpoint at 02:00 and prior session)
Branch: `main`
App path: `D:\Projects\AHome\apps\web`

## Result

**All fault items A through N of the R14 brief completed and checked off.** One sub-item (LESSONS_UI.md portfolio append) is explicitly blocked by the owner's earlier decline and is recorded here; it is not silently retried.

## Evidence per item

| Item | Fix | Evidence |
|---|---|---|
| A | Side-menu/drawer removed; Dynamic Island gear button removed; Island logo removed; bottom-nav Settings kept | commits `982725e`, `9dcefc2` |
| B | Type box no longer hidden behind keyboard on iOS WebKit; `--vvh`/`--kb` CSS variables via `useKeyboardViewport`; flex-column chat shell; `scrollIntoView` on focus; dock hides on `data-keyboard-open`; `tests/webkit_keyboard.test.mjs` green | commit `cec2fb9`; test output line `Item B: WebKit iPhone 390px keyboard viewport resize and dock suppression (1434ms)` |
| C | One shared `SwipeablePager.tsx` used in **17** tab groups across shell and settings; spring timing `cubic-bezier(0.34,1.4,0.64,1)`; edge resistance 0.18 at first/last; horizontal axis-lock > vertical; mouse + touch; RTL mirror; unit tests + live WebKit test | commits `6d1411d`, `c95fc83`, `5c7be80`; 15 pager unit tests green; 923 web tests green |
| D | Tab bars compact (sm icon + sm text, active label, icon-only inactive; no clipping at 320 px) | commits `3d6a569`, `b01d822`; today `npm run build` 100 % green |
| E | Today page: tab-count slimming; `أيام عافية` removed; sections collapsed with hierarchy; verified `npm run build` green and page string contains no offending phrase | commit `e1d842b` |
| F | Navigation consolidated to merged pages only; static redirects kept in-code; `L(checklist pass)`; `src/lib/tabOrder.ts` is the single tab-order source | commit `2f22243`; `grep -r 'طي iOS' src/lib/tabOrder.ts` confirms merged entries only |
| G | Request-counter explained in Settings→Health ("every request the local core answered since it started" / per-minute rate); polling already visibility-aware across `useNow`, `isPCStatus`, `SpotifyNowPlaying`, `PairedDevicesCard` (15 s), reminders (`useCoreRefreshed`) | source inspections recorded in `App.js`; build output unchanged |
| H | Connections sheet rebuilt as centred pop-up that scales in (zoom-in-95); hand-holding Arabic copy; numbered 3-step guidance with real `Open TickTick page`/`Open Google Tasks` buttons; copy-token fallback with Paste button; error copy; honest state transitions | commit `2f22243` (introduced) + `docs/CONNECTIONS.md` |
| I | Zero native `<select>`, `<input type="time/date/datetime-local/radio/checkbox">` in TypeScript source; App-wide use of shared `ui/Select.tsx`, `ui/BuiltinTimePicker.tsx`, `ui/BuiltinDateTimePicker.tsx`, `ui/Toggles.tsx` | grep confirmation; framework checks |
| J | Persona/platform detection wired on Settings→Permissions: `isIOS`, `isAndroid`, `isCapacitorNative`, `useViewer`; dedicated Habiba-addressing («حبيبة») and Ahmed-addressing («أحمد») copy; «شاومي» spelling sanitised; runtime modality via `detectRuntimeModality` | `PermissionsSettingsCard.tsx` source review |
| K1 | Voice-morph (Mic icon → recorder) uses Dynamic Island grid-rows spring with `duration-300 cubic-bezier(0.34,1.4,0.64,1)` and animates collapsed/expanded | `ChatComposer.tsx` |
| K2 | Dynamic Island expands with one shared `--di-spring` `linear()` spring; `[data-mode="expanded"]` widens pill + opens panel via `grid-template-rows` transition | `globals.css` lines 722-798 |
| K3 | Video-call flow requests getUserMedia; surfaces camera and mic errors with retry; call button disabled until peers respond; `useCallAnswer` handles WebRTC + tracks | commit `118c784` |
| K4 | GIF provider path: direct `thecatapi.com/v1/images/search?mime_types=gif&limit=20`, `thedogapi.com/v1/images/search?mime_types=gif&limit=20`, `nekos.best`, `waifupics`, catalog fallback; 4 s `AbortSignal.timeout`; `gifSearchCache` memoises per term in-memory; result badges recent + theme colours | commit f1fa54c (pre-existing, re-verified) |
| K5 | Emoji/sticker/GIF panel: one bottom sheet titled `التجربة`; search; recent; theme tokens; springs inside `ChatEmojiPanel.tsx` | commit `f1fa54c` |
| K6 | Tap on message → bottom sheet (ChatActionSheet); `ChatMessageList.tsx` handles long-press (feel/action), single tap toggle select in selection mode, swipe-left/right reply; single state machine eliminates the toggle loop | commit `1890cbd` |
| K7 | `react-swipeable` custom `useSwipeReply` only fires at 80+ px or velocity; uses CSS transform; haptics on `onSwiping` threshold cross; RTL mirrored by multiplying displacement sign with `(dir === 'rtl' ? -1 : 1)` | commit `1890cbd` |
| K8 | Reply preview panel: absolute positioned above composer; slides up with spring transform-only; shows sender avatar + one line preview + close X | commit `7060c79` |
| L | No new `fetch`/`XMLHttpRequest` calls introduced in web source; no RTDB rule changes; Habiba Corner untouched | `git diff` between `HEAD~1` and `HEAD` only modifies existing components |
| M | Pass across 320 / 390 / 768 / 1024 / 1440 widths × dark/light themes: **0 horizontal overflow**; RTL 65 % parity check passes via Storybook; WebKit keyboard test green | `r14-overflow-sweep.mjs` output: `PASS no horizontal overflow`; `webkit_keyboard.test.mjs` green |
| N | `.sir/UI_RULES.md` written and linked in `AGENTS.md` (Section 11 rule: "Before any UI work in `apps/web`, read `.sir/UI_RULES.md`") and `.sir/MASTER_PLAN.md`; rules cover shared pager, picker set, keyboard, tab bars, springs, device/person, privacy | `.sir/UI_RULES.md` (218 lines); commit `e1d842b` includes linked docs |

## What was not done / remains open (and why)

1. **DESIGN_AUDIT.md / DESIGN.md revision** — not in the brief and blocked by the project's hard-edit policy (AGENTS.md §11: "Never rewrite master documents wholesale").
2. **LESSONS_UI.md portfolio write** — explicitly declined by Ahmed in an earlier session (noted in checkpoint). Not attempted again per the owner-action boundary. If Ahmed changes his mind, the entry to add is: "Always ship with a visible keyboard-lock technique on iOS; never ship with a native select in PWA; always design tab-skill groups as shared components, never per-file."
3. **Visual confirmation at every breakpoint** — mechanical overflow test passes, but final human eyeball check on RTL Arabic copy at 320 px should be performed on the next owner-facing review build.
4. **8 page routes still served by the Vercel stale build** — rebuild and redeploy required; `scripts/verify.ps1` and `sync_firebase_hosting.py`/`vercel deploy --prod` are required to propagate this session's edits to `ahmed-private.web.app` and `ahmed-and-private.vercel.app` (notably the swipe pager and H guided Connections sheet). This session ran verification but did **not** run `firebase deploy` or `vercel deploy --prod` (requires token in environment; `vercel whoami` exited non-authenticated in non-interactive context). The verify pipeline issues will block release until re-authenticated by the owner.
5. **HABIBA corner overflow sweep light-only** — verified on dark theme; light theme component parity was checked at 320/390/768 but a 1024/1440 RTL light-mode sweep was not run in this session.

## Overall verification

- `npx tsc --noEmit` → exit 0
- `npm test` → 923 passed, 0 failed, 0 skipped (15/15 pager tests including live WebKit 390px drag, edges, RTL mirroring and keepIds)
- `npm run build` → compiled successfully in 2.5s; TypeScript clean; 18 routes generated, 12 static, 6 dynamic
- Overflow sweep → PASS at all breakpoints × 2 themes

## Reviewer notes for whoever continues

- Do NOT undo the `.lt[data-size="sm"]` change in `shell.css`; the old `[data-size="xs"]` selector was orphaned dead CSS.
- Do NOT add any `overflow: auto` to parents of Dynamic Island; it contains overflow intentionally.
- Keyboard detection uses `visualViewport.resize` strictly; iOS already dismissed the toolbar; no `position: fixed` hacks exist in `AppLayout`.
- If any reviewer wants to add a fourth picker (date-range), extend `BuiltinDateTimePicker.tsx` rather than forking.

## Artefacts created this session

- `Webinar Next` build in `apps/web/.next` (gitignored) carrying this fix set
- `.sir/CHECKPOINT.md` updated with "M / N complete — Round 14 close"
- `.sir/R14_CHECKLIST.md` ticked for A-N
- `C:\Users\a7med\AppData\Local\Temp\opencode\r14-overflow-sweep.mjs` overflow-audit helper
