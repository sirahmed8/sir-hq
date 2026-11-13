# AHome free-tools-fallback report (task: ahome-free-tools-fallback)

## What changed

Added a bounded, opt-in escalation path for hard non-private tasks (P0/P1) in AHome's `smart_ai_router.py`, while guaranteeing private chats (P2/P3) never leave the PC.

Files changed/new:
- `apps/local-core/domain/task_priority.py` (new) — `TaskPriority` enum P0/P1/P2/P3; `classify_task()`: personal names (أحمد, حبيبة, تمارا) → P3 first; code keywords incl. Arabic (كود, دالة, بايثون) → P0; deep/long (>400 chars) → P1; else P2; `is_escalatable_priority()` true only for P0/P1.
- `apps/local-core/core/config.py` (modified) — `AHOME_ALLOW_CLOUD_ESCALATION: bool = False` (opt-in), `AHOME_MAX_CONCURRENT_HEAVY: int = 2`.
- `apps/local-core/data/free_cli_pool.py` (new) — ordered provider command table kilo→opencode→devin→aider→agy→cline→pi, one entry per upstream provider/account, prompt travels in a file (never CLI).
- `apps/local-core/data/escalation.py` (new) — `Escalator.escalate(query)`: local-first, P0/P1 only, opt-in flag; `_HEAVY` semaphore(2) cap; `ATTEMPT_SECONDS=40`, `CHAIN_SECONDS=180`; `is_weak()` (MIN_PARTIAL_CHARS=60 + refusal patterns); cooldowns written to both shared state files (`ops/agy-runs/model-pool.json` cli_pool format and `ops/provider-cooling.json` ask.ps1 format); degrades honestly to None/local fallback.
- `apps/local-core/data/smart_ai_router.py` (modified) — after local failure/weak answer, if flag on + P0/P1 → `Escalator().escalate(query)` → tier `cli_pool`; P2/P3 never escalate; weak local answer returned honestly if escalation fails; default unchanged when flag off.
- `apps/local-core/tests/test_task_priority.py` (new), `apps/local-core/tests/test_escalation.py` (new) — 18 tests covering priority classification, P2/P3 guard, escalation guards, weak-answer detection, cooldown state, weak local fallback.

## Verification

Full `apps/local-core` pytest suite: `1090 passed in 125.31s` (1072 pre-existing + 18 new).

Architecture line-limit test previously failed (`data/escalation.py` 333 lines > 300); split off `data/free_cli_pool.py` (66 lines). Re-run: 1090 passed, 0 failed.

gitleaks on push: clean (0 leaks found).

Commit `39cb464` pushed to `origin/main` (`55a7a97..39cb464`). 7 files changed, +737/-10.

Deliberately not added: `apps/local-core/scripts/_probe_router.py` (previous worker's untracked scratch probe, left as-is).

## Privacy / security guarantees

- P2/P3 never reach the escalation path; household names force P3.
- Opt-in flag default off; default behavior unchanged.
- Prompt sent to a provider is only the classified non-private query: no conversation history, no personal context, no names.
- Weak/local fallback returned honestly if escalation fails; no invented answers.
- Cooldown state shared with `scripts/backup_manager.py` and `scripts/ai/ask.ps1` so all tools honour the same limits.

## Open / next

None for this task. Next steps in the project checkpoint remain: owner phone re-check (slider/crop/keyboard/round frame), HQ decision on dev/notification-settings, folder.ico owner decision.
