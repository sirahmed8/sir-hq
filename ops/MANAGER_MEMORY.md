# MANAGER MEMORY (what the manager learned; newest at the top; prune stale lines)
Read this after MANAGER_STATE.md. Facts live in one file: link, do not copy.

## About Ahmed (owner, CEO)
- Wants results not plans; never asked questions unless it is truly his decision. Sets direction, expects the manager to decide, hire, fix.
- Academic integrity is a hard line: prepare him, never solve graded work to submit (he asked for "answer checking" and "parallel worked examples": that is the allowed form).
- Prefers cheap models/low usage waste: Haiku for browsing, scripts and local models for bulk (`USAGE_POLICY.md`).
- Private: AHome and anything about Habiba never leaves local systems.

## AgentsRoom mechanics (verified 2026-11-08)
- Saved agents (builder, study-coach, automation-engineer, ...) are Antigravity Gemini 3.8 Flash high. `assignments_create` to an offline agent starts its console by itself (mail wakes it); `agents_resume` then answers "already live". Do not spawn.
- Do not send the same brief twice; use `assignments_list` nextAction.
- Two agents share the name "pm" (this seat and a spare). Address by id.
- SIR Autonomy bridge WORKS (2026-11-08): `cd D:\Projects\_SIR	ools\sir-autonomy && .venv\Scripts\python.exe sir_ctl.py browser tabs|open|navigate|snapshot|click|eval|close` drives Ahmed's real Chrome (system python lacks Pillow; use the .venv). Tab lists contain auth codes in URLs: never paste them anywhere. Moodle was signed out on 2026-11-08 (owner action logged). AgentsRoom-Browser and chrome-devtools MCP are separate signed-out profiles.
- AgentsRoom-Chrome MCP: HTTP 403 for non-owner consoles. Use another browser route.

## Workspace facts
- `ops/READ_LOG.md` header defines the line format. Hook scripts live in `_SIR/scripts/memory/`. Zero-byte `.sir` files were found in SIR Negm Furniture (BENCHMARK, BOARD, DESIGN, PLATFORMS, PRODUCTION, QUALITY).
- Study schedule: SCHEDULE.md in SIR Study (SAD 09/11, OR 10/11, Human Rights 12/11, Business Admin 15/11, HCI 18/11, Electronics 19/11; Data Structures was 08/11).

## Mistakes and fixes
- (none yet this week)

## Mistakes and lessons (2026-11-08)
- Briefs for any worker that reads ops/ or bus files and writes reports must say up front: AHome and Habiba lines must never reach generated output, evidence, repos or Telegram (add a planted-string test). I omitted it for SIR Life and the first build leaked them. Workers' own 'tests pass' is not evidence: always have a different agent review.
- Gemini Flash workers fix the reported line only and miss sister code paths (SIR Life privacy leak survived 3 rounds). After the second RETURN on the same class of defect, hand the root-cause fix to a sonnet builder and ask for a single chokepoint plus a test that enumerates every sender; never accept 'tests pass' without a reviewer planting strings.
- NEVER agents_send to '*': it queues mail to all ~31 saved agents and the app tries to open a background console for every offline one (usage burn, breaks max-3 rule). I did it once at 08:00 for the Telegram rule; closed all offline recipients with agents_close (each returned sessionEnded:false = no session had started yet). Broadcast by file (AGENTS.md) or send to the named live agents only.
