# r76-ahome-games-gifs-fix Report

## Summary
Fixed GIF picker and XO multiplayer game invitation flow in AHome (apps/web Next.js web app). All work committed and pushed to main.

## Changes

### GIF Picker (commit fd0a884)
- Removed hardcoded `GIF_CATEGORIES` array ("الكل", "حب", "ضحك", "فرح") from `ChatEmojiPanel.tsx`.
- GIFs now load only from the trending endpoint (`app/api/gifs/route.ts`) using GIPHY/TENOR API keys.
- Debounced search with RTL placeholder and correct result rendering already existed — verified, no change needed.
- Broken thumbnail loading with `onError`/`naturalWidth` fallback already existed — verified, no change needed.

### XO Multiplayer Game (commit 7dcc3f1)
- Rewrote `ChatGameCard.tsx`:
  - Inviter / invitee roles; game waits for both players before starting ("في انتظار انضمام الشريك...").
  - Turn indicator: "الدور على: {name} ({X|O})".
  - Board locks immediately on win; victory overlay with Trophy icon.
  - Game start/leave notifications via `notifyPartner` over `liveSyncBus`.

### Game Invitation Flow (commit e210296)
- `ChatAttachSheet.tsx`: broadcasts `game_invite` event over `liveSyncBus` channel `game_xo_<gameId>`; `onInviteGame(gameName, gameKey)` signature.
- `ChatComposer.tsx`: handler accepts `(game, gameKey)`; embeds gameKey in submitted message text.
- `ChatMessageContent.tsx`: passes `gameKey={card.game}` to `ChatGameCard`.

## Verification
- `tsc --noEmit`: exit 0 (no TypeScript errors).
- `eslint` on all touched files: 0 errors (3 pre-existing warnings on untouched lines, identical to baseline).
- `node --test --test-concurrency=1 tests/*.test.mjs`: all 17 failures are pre-existing Playwright WebKit environment failures (WebKit browser not installed on this machine), identical to baseline. No regressions introduced.
- CI quota flag `ops/ci-quota-exhausted.flag` present -> local verification is the gate (rule 18).
- gitleaks clean; pre-push privacy audit clean.

## Commit History (this round, all pushed to main)
- fd0a884 fix(ahome): remove hardcoded GIF categories, show trending only
- 7dcc3f1 fix(ahome): XO waits for both players, turn indicator, victory overlay, game notifications
- e210296 fix(ahome): game invitation flow via liveSyncBus with accept/decline

## Open / Not Done
- Physical phone verification (needs owner's two devices): ringback, full-screen incoming UI, camera after answer.
- `apps/local-core/scripts/_probe_router.py` is untracked, not from this round; left alone.
