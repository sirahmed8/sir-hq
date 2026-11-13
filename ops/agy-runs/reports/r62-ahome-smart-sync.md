# r62-ahome-smart-sync — final report (2026-11-12, Devin continuation)

## Scope

Brief: `D:/Projects/_SIR/ops/briefs/r62-ahome-smart-sync.prompt.txt` — smart sync for
TickTick / Google Tasks / Xiaomi ICS / voice reminders into classified sections, sync log,
owner metrics, tests incl. a 5,000-item replay, performance evidence, premium bilingual UI.

This session continued where the previous Devin session stopped (quota cut). The backend and
the web panel were already committed; this round repaired a broken tree, finished
verification, and closed the task.

## What changed this round (all pushed to main)

| Commit | What |
|---|---|
| `7d7a503` | feat(connections): smart sync backend — classification, organize, sync log, metrics (previous session) |
| `d6914df` | feat(connections): classified items panel, sync log and owner metrics in settings (previous session) |
| `4b2ecfc` | fix(chat-menu): a tap outside the message menu closes it again — **real bug repair** |
| `4c2a98c` | fix(tests): cloak module resolves under `node --test`; corner assertion matches the r57 cloak design |
| `89e1c7a` | feat(dev): `/dev/sync-panel` harness page + `_r62_sync_panel_shots.mjs` evidence script |
| `4efe3fc` | test(r15): mute audio + 15s settle budgets for the voice-recorder layer (known flake hardening) |

### Repairs found and fixed (tree was broken on arrival)

1. **`privacy_cloak.test.mjs` crashed the suite** — `src/lib/privacyCloak.ts` imported
   `@/lib/privacyCloakTabs`, an alias `node --test` cannot resolve
   (`ERR_MODULE_NOT_FOUND`). Changed to the relative `./privacyCloakTabs.ts` specifier used by
   the other lib modules. Verified: cloak tests 16/16 pass.
2. **`habiba_corner_architecture.test.mjs` corner 2 failed** — it asserted the pre-r57 rule
   `currentUser === "habiba" && !isCloaked`. r57 (commit `5f867c0`) intentionally reversed that:
   tabs stay visible while cloaked, only content is masked. Updated the assertion to the new
   invariant (corner gated on viewer only, `BottomNavBar` must not reference `isCloaked`).
3. **Real app bug: message context menu could not be dismissed by outside tap.**
   `ChatActionSheet.tsx` checked `e.target === overlayRef.current`, but the tap lands on the
   backdrop child (`absolute inset-0 bg-black/55`), never the overlay — so the guard was dead
   code since `7abf9d8` (19:40 today, after the last green run). Reproduced with a Playwright
   probe (`elementFromPoint(50,50)` = backdrop div; menu stayed open after click and after
   touch tap). Fixed by checking whether the pointer went down *inside* the sheet
   (`sheetRef.current.contains(target)`) instead. Verified: `r15_context_menu` passes.
4. **Port 3000 served a stale production build** (stamp 04:06, before ~10 commits) — caused 7
   WebKit test failures that looked like regressions. Rebuilt via the sanctioned
   `scripts/web-build.ps1 -Restart`; all browser tests pass on the fresh build.
5. **r15 voice-recorder flake hardened** — added `--mute-audio` + `speechSynthesis` stub
   (worker rule 11 compliance) and raised the opacity settle budget 6s→15s in both directions.

## Verification (real output)

- **Web serial suite (the gate):** `node --test --test-concurrency=1 tests/*.test.mjs`
  → `tests 1041, pass 1040, fail 0, skipped 1`, exit 0.
  Evidence: `.sir/evidence/r62/tests-serial-final3.txt` (also `tests-serial-final.txt` shows
  the intermediate state 1039/1041 with only the known voice flake).
- **Backend:** `./.venv/Scripts/python.exe -m pytest tests/test_conn_classify.py
  tests/test_conn_recur.py tests/test_conn_organize.py tests/test_conn_sync_log.py
  tests/test_conn_replay.py -q` → `24 passed in 22.69s`. Previous session: full local-core
  suite `1056 passed in 115.67s` at commit `7d7a503`.
- **Types:** `npx tsc --noEmit -p tsconfig.json` → exit 0, no errors.
- **Lint:** `npx eslint` on all touched files → 0 errors (1 pre-existing unused-var warning).
- **Build:** `scripts/web-build.ps1 -Restart` → `web build done`, daemon restarted by watchdog,
  `.sir/web-build.stamp` updated; `curl :3000/dev/sync-panel` → 200.
- **Screenshots (synthetic intercepted payloads, no private data):**
  `.sir/evidence/r62/sync-panel-{populated,expanded,empty,error}-390-{ar,en}.png` — 8 shots,
  populated/expanded/empty/error states at 390px in Arabic and English, taken against the real
  component through `/dev/sync-panel` with `/v1/connections/*` route interception.
- **CI:** `ops/ci-quota-exhausted.flag` exists → per worker rule 18 the gate is full local
  verification (above), not GitHub Actions. `gh run list` shows prior runs failing in ~4s
  (quota, zero steps).

## Brief checklist status

1. Sync engine backend (scheduled + on-demand, idempotent, incremental, batched, backoff,
   conflicts, deletes, two-way) — done earlier (`conn_engine`, `conn_registry`,
   `run_scheduler`); hardened with O(n) adopt index + sync log (`7d7a503`).
2. Smart classification AR+EN rules → AI fallback → visible reason → one-tap correction that
   teaches rules — done (`domain/conn_classify.py`, `conn_class_rules`,
   `POST /items/{id}/section`).
3. Ordering/grouping, cross-provider duplicate flags, RRULE normalisation, timezone —
   done (`domain/conn_organize.py`, `conn_recur.py`, `conn_ics.py`).
4. Status model — already existed (`warmConnectionStatuses` at app start, cached linked-apps
   page, plain-word errors + retry); unchanged.
5. Sync log page + owner metrics — done (`GET /sync-log`, `GET /metrics`,
   `ConnectionsSyncPanel` in settings, AR/EN, all 5 states).
6. Tests for every rule + 5,000-item replay — done (`test_conn_classify/recur/organize/
   sync_log/replay`; replay: 21.6s first sync, 5,200 live items).
7. Performance — O(n) merge via hash index; items endpoint paginated; UI never blocks
   (cached statuses, lazy panel load).

Design doc: `.sir/SMART_SYNC_DESIGN.md` (written before coding per rule 20).

## Environment incidents handled

- **C: hit 0 bytes free mid-round** (ENOSPC killed the first `web-build.ps1` run). Freed
  `npm-cache/_cacache` (~0.6GB), cleared old `%TEMP%` files, reinstalled Playwright browsers
  (`chromium_headless_shell-1254`, `webkit-2388`, `winldd-1007`) which had been removed —
  likely by the concurrent `r67-c-drive-space` cleanup. Builds were run with
  `TMP=/d/tmp-win TEMP=/d/tmp-win npm_config_cache=/d/tmp-npm` so npm/node temp writes go to D:.
  **C: still showed ~0 MB free at end of round** — flagging for the owner/next round; the
  dedicated disk-space worker is on it.
- A second worker (`devin-r57free`) is concurrently active on AHome (lock
  `ops/locks/AHome.lock`); all pushes were clean fast-forwards, no conflicts.

## Still open / honest limits

- `r15_reply_voice` remains an environment-sensitive flake under full-suite machine load
  (documented OPEN since r40). It passed the final full serial run (1040/1041) and 3/3
  isolated runs after hardening; earlier full runs failed it twice. Root cause per r40
  notes: headless WebKit paint/rAF starvation, not an app defect.
- Real Whisper transcription is still unverified end-to-end (needs the PC core + mic;
  unchanged from r38 note).
- Uncommitted and intentionally left: `.gitignore` (`.aider*` line, another tool's),
  `apps/web/next-env.d.ts` (auto-generated, flips with dev/build), `folder.ico` (binary
  change from another process). None are mine.
- `.sir/` is gitignored — CHECKPOINT.md updated locally, not committed (by design).

## Recommendation

- Owner/next round: keep an eye on C: free space; if it hits 0 again, builds/tests will fail
  with ENOSPC. Consider moving `ms-playwright` and npm cache to D: permanently.
- The context-menu outside-tap bug (`7abf9d8`) shows gesture-handlers deserve a regression
  test that exercises the real backdrop element, not just the overlay — the current test now
  covers it and caught this class of bug.
