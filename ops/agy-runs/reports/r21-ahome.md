# r21-ahome report — 2026-11-11 (Devin continuation)

## What this round did

Picked up at checkpoint "item 12 partial; items 13, 14, 15, Part B open". Most of that work already existed in commits; this round verified it, closed the real gap in item 14, ran the missing audit cycle, and ticked the checklist.

### Item 14 — Telegram owner format (the only real code gap)

- `infra-daemons/telegram_format.py` already had `owner_message`, `is_question`, `question_keyboard`; `telegram_api.send_message` already attached yes/no quick-reply keyboards to every question and `telegram_reminders` handled `qr:` taps. But `owner_message` was dead code — proactive notifications were never formatted.
- Added `owner_notice(text, needed)` which normalises an already-built notification: first line stays the title, middle lines become facts capped at `MAX_FACT_LINES` (5), a trailing "المطلوب منك" line the caller wrote is preserved, otherwise the given CTA or `CTA_NONE` is appended.
- Wired it into `infra-daemons/telegram_gateway_bot.py` for all three proactive payload kinds: `agenda_briefing`, `telegram_full_text` reminders, and the short reminder fallback. Reminder pushes now end with "أنجز التذكير أو أجّله من الأزرار بالأسفل" and keep their action keyboards.
- Left `scripts/notify_owner.py` unchanged on purpose: its test asserts the exact single-line minimal alert (service name + state + time, nothing else) — a deliberate no-extra-data security choice, already one fact.
- Extended `apps/web/tests/r21_telegram_format.test.mjs` with a test asserting `owner_notice` exists and the gateway bot actually calls it.
- Commit `fc5b1d2`, pushed to main.

### Item 12 — verified complete (no new code needed)

- PKCE: `apps/local-core/data/connections_pkce.py`, `domain/connections_pkce.py`, `data/connections_oauth_client.py`; start binds verifier to pending state (`tests/test_connections_api.py::test_oauth_start_binds_the_authorize_challenge_to_the_stored_verifier`).
- Tokens: `data/conn_tokens.py` seals per-person/provider tokens AES-256-GCM via `core/vault_crypto` into the vault dir — never localStorage, never git, never sent to the browser.
- Two-way sync: `data/conn_engine.py` pull/push phases with outbox (`conn_push`); `test_connections_sync.py` covers it.
- UI: `ConnectionsSettingsCard.tsx` has not_linked / linking / linked(+account name) / error states, per-provider sync-now, Sync All, disconnect (unlink), failed-ops retry banner, and `missingClientIdMessage` naming `TICKTICK_CLIENT_ID` / `GOOGLE_TASKS_CLIENT_ID`.
- Hosted finish: `apps/web/src/app/api/integrations/[provider]/callback/route.ts` (with `google-tasks` hyphen alias) redirects to `/connections/callback`, which POSTs code+state to the local core `/v1/connections/{provider}/oauth/complete` — OAuth secrets stay on the PC, nothing needed in Vercel env.
- Env: `apps/local-core/.env` contains TICKTICK_*/GOOGLE_TASKS_* (sourced from `_local/ahome-oauth.env`, gitignored, never printed).
- Calendar import: `data/conn_google_calendar.py::import_calendar_events` pulls the owner's own Google Calendar into real PlanItems with yearly recurrence for birthdays — exposed via `importGoogleCalendarEvents` in `connectionsApi.ts` and a button in `ConnectionsSettingsCard`.
- `pytest tests/test_connections_api.py tests/test_connections_sync.py -x -q` → **35 passed**.

### Items 13 and 15 — verified complete

- Item 13: `FreeImportTools.tsx` + `IcsTools.tsx` mounted in `CalendarTab.tsx`/`DatesTab.tsx`; file import with per-row preview; Google Calendar import through the linked account; `shared` flag covers "add a date for the other person"; provider status table with built vs needs-owner-ids steps in `.sir/plans/r21-integrations.md`.
- Item 15: `src/lib/us/freeImport.ts` handles Arabic-Indic/Persian digits, dd/mm/yyyy, dd-mm-yy, ISO, English + Arabic month names, bullets, `|`/`;`/tab separators, mixed ar/en, JSON rows; every row schema-validated via `isPlanItem`; preview shows accepted/fixed/rejected+reason before save; `r21_free_import.test.mjs` covers 33 messy fixtures + JSON + rejection reasons — all pass.

### Part B — three clean cycles

- The previous model's uncommitted edit removed `/connections/callback` from `ROUTES` in `apps/web/scripts/r21_cycle_audit.mjs`. Investigation showed cycle 1's 48 findings were all `unreachable` HTTP 404s because the dev server was stale; all routes now return 200, so I restored the route to the sweep (file now matches HEAD — nothing to commit).
- Ran the audit myself: `node scripts/r21_cycle_audit.mjs 4` against the live dev server on :3001 → **0 defects** (`.sir/cycles/r21-cycle-4.json`), now including `/connections/callback`.
- Cycles 2 and 3 JSONs are both `[]`. Three consecutive clean cycles (2, 3, 4) at 390/320/768 px × ar/en × light/dark × WebKit+Chromium.
- `.sir/DEFECTS.md` updated: O1–O5 marked FIXED with their resolving commits, cycle log section added. `.sir/R21_CHECKLIST.md` fully ticked with proof per line.

### Housekeeping

- Deleted stray `cookies.txt` at repo root — a curl Netscape cookie jar containing a localhost `ahome_session` token (untracked test artifact).
- `.sir/` is gitignored, so DEFECTS/cycles/checkpoint updates stay local as intended.

## Commands run (real output)

- `pytest tests/test_connections_api.py tests/test_connections_sync.py -x -q` → `35 passed in 2.86s`
- `node --test tests/r21_*.test.mjs` (in apps/web) → `tests 25, pass 25, fail 0`
- `node scripts/r21_cycle_audit.mjs 4` → `cycle 4: 0 defects -> .sir/cycles/r21-cycle-4.json`
- `python -m py_compile telegram_format.py telegram_gateway_bot.py telegram_api.py` → OK; manual `owner_notice` check caps 9 facts to 5 + CTA.
- `curl` route probe on :3001 → `/`, `/changelog`, `/privacy`, `/docs/ios`, `/connections/callback`, `/dev/screens` all 200.
- `gh run list --limit 3` → latest: `completed success verify main push 42973302375` on `fc5b1d2`.

## Still open / notes for the owner

- Real TickTick/Google account linking can only be exercised on his devices; OAuth ids are already in `apps/local-core/.env`.
- Providers needing owner registration (Microsoft To Do, Apple CalDAV/ICS, Notion, Drive metadata) are listed with exact steps in `.sir/plans/r21-integrations.md`.
- `notify_owner.py` alert format intentionally minimal; if HQ wants the full title/facts/CTA shape there too, its test needs updating first.
- Conversational bot replies are not wrapped in `owner_notice` (they are answers, not reports); questions among them still get quick-reply buttons automatically.
