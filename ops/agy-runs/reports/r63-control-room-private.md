# r63-control-room-private — worker report (2026-11-12, devin / SWE-2 Flash)

## Situation found

The task was already `done` on the board and `cancelled` in `ops/AUTOPILOT_QUEUE.json`:
the owner decided at 2026-11-12 (commit `d0946fd`, "Control Room private on Tailscale only,
public Pages site deleted") that there is NO public site. `ops/DASHBOARD_URL.txt` line 2 now
reads `https://ahmed.tail9e9aa7.ts.net/ (Tailscale only, private)`. The brief's item 1
(Pages Function + Basic auth) and item 2 (password to Ahmed) are therefore obsolete; the
privacy goal is met by network-level isolation instead. What was genuinely unfinished:
the privacy audit report did not exist, nobody had verified the Tailscale serving path
end to end, the owner had never been sent the new URL, and the checklist had no proof.

## What I did, with proof

### 1. Verified the Tailscale-only serving path

`tailscale serve status` (real output):

```
https://ahmed.tail9e9aa7.ts.net:3300 (tailnet only) -> http://127.0.0.1:3300
https://ahmed.tail9e9aa7.ts.net:3456 (tailnet only) -> http://127.0.0.1:3456
https://ahmed.tail9e9aa7.ts.net        (tailnet only) -> http://127.0.0.1:8899
https://ahmed.tail9e9aa7.ts.net:8765 (tailnet only) -> http://127.0.0.1:8765
https://ahmed.tail9e9aa7.ts.net:8899 (tailnet only) -> http://127.0.0.1:8899
```

`tailscale funnel status` shows the same entries, all `tailnet only` — no public funnel.
`tailscale ip -4` = `100.85.112.10`; MagicDNS name `ahmed.tail9e9aa7.ts.net` is in use.

Server-side (`scripts/serve-control-room.py`): binds `127.0.0.1:8899` only; `ALLOWED_HOSTS`
(line 36) accepts only loopback + the ts.net name; static allow-list (line ~300) serves only
`dashboard.html`, `favicon.ico`, `favicon.svg`, `manifest.json`, `health.json`.

Live curl proof:

- `http://127.0.0.1:8899/dashboard.html` -> 200
- `http://127.0.0.1:8899/OWNER_ACTIONS.md` -> 404
- `https://ahmed.tail9e9aa7.ts.net/OWNER_ACTIONS.md` -> 404
- `https://ahmed.tail9e9aa7.ts.net/` -> 302 -> `/dashboard.html` -> 200 (75,609 bytes served = `ops/public/dashboard.html`)
- `https://sir-control-room-0dce50.pages.dev/` -> `000` (public site deleted/unreachable)
- `/health.json` -> healthy, pid 26608, `last_refresh_ok: true`

### 2. Privacy audit of the served page — written to `ops/reports/control-room-private-report.md`

Scanned the exact served file `ops/public/dashboard.html`:

- Emails: none. Phones: none (`1794511813` is `generated_epoch`). `habiba`: 0 matches.
- Secrets: no key values, tokens, bot tokens, chat ids, or recovery codes. Only `*_KEY`
  match is JS constant `VIEW_KEY` (nav map) — false positive. Owner-action feed embeds
  titles only, no values.
- Chat content / messages / photos: none.
- `AHome`: product and task/round names only; the repo row is `"private": true` and the
  generator limits it to commit date + CI state. No AHome personal data or Habiba material.
- No `localhost`/`127.0.0.1` links anywhere in the dashboard (grep count 0 in artifact,
  `ops/dashboard.html`, `ops/public/dashboard.html`, template) — brief item 3 is obsolete;
  the local services are already exposed tailnet-only via `tailscale serve` (:3300/:3456/:8765).

### 3. Owner notification

`ops/bus/telegram-outbox.md` and `ops/bus/ahmed-telegram.md` had no ts.net message, so I
sent the new private URL once via `node scripts/deliver/send-telegram.mjs` —
`sent text message_id=687`. Message (Arabic, rule-12 format) gives the URL, says Tailscale
must be on, says the old public link was deleted, ends with the one action needed.
Logged in `ops/bus/telegram-outbox.md`.

### 4. Bus lines and checkpoint

- `ops/bus/team.md`: DONE line appended.
- `ops/bus/sir-hq.md`: full summary line appended.
- `.sir/CHECKPOINT.md`: worker note appended (below, in the commit).

### 5. Verification run

`python plans/generate_dashboard.py` -> `generated ops/artifact/control-room.html
(75573 bytes, 1b0851f8) at 2026-11-12 21:32` — the same generator the scheduled task runs;
mirrors `ops/dashboard.html` and `ops/public/dashboard.html` rewritten atomically.

CI: `ops/ci-quota-exhausted.flag` exists (GitHub Actions minutes exhausted until ~2026-12-01),
so per WORKER_PREAMBLE rule 18 "CI green" is replaced by local verification — done above
(docs/ops-only change; generator run is the relevant check and it passed).

## Checklist status (brief items)

1. Pages Function Basic auth + 401/200 proof — OBSOLETE, cancelled by owner; public site
   deleted (curl 000). Privacy now enforced by Tailscale tailnet-only serving (proven above).
2. Password to Ahmed — OBSOLETE (no password exists or is needed); equivalent action done:
   private URL sent once on Telegram (message_id=687).
3. Tailscale links for local services — OBSOLETE: dashboard contains zero localhost links;
   services already reachable tailnet-only via `tailscale serve` (:3300 Study, :3456 Jobs,
   :8765 Laptop Manager, :8899/root Control Room).
4. Privacy audit + report — DONE: `ops/reports/control-room-private-report.md`.

## Commits

See `git log` — this round's commit contains the two report files, bus lines, checkpoint
note, and the regenerated dashboard mirrors.

## Still open / recommendations

- None blocking. If Tailscale ever adds other users to the tailnet, re-run the content audit
  in `ops/reports/control-room-private-report.md`.
- `ops/ci-quota-exhausted.flag` still present; per an earlier worker note it may be stale —
  HQ to review when Actions quota resets (~2026-12-01).
