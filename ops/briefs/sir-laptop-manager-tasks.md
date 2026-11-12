# TASK BRIEFS: SIR Laptop Manager — First 10 Tasks for Free Agents

**Project:** SIR Laptop Manager (`D:\Projects\SIR Laptop Manager`)  
**Wave:** 2 (PERSONAL)  
**Status:** Active development — replacing `Laptop manager` + `antigravity-agent-suite`  
**Date:** 2026-11-12 (r52 HQ round)  
**Checkpoint:** `.sir/CHECKPOINT.md` (updated 2026-11-12)  
**Plan:** `plans/sir-laptop-manager.md`  
**Competitor Matrix:** `ops/competitors/sir-laptop-manager.md`  
**Feature Gaps:** `.sir/plans/FEATURE_GAPS.md` (24 ranked gaps)

---

## Task Queue Rules
- Each task ≤ 2 hours for a free agent (Kilo, OpenCode, Devin CLI, ZCode)
- Title + one-paragraph brief + acceptance test + files to touch
- Run `scripts/verify.ps1` after each task; paste passing output in checkpoint
- Commit & push to `main` after each green verify
- Update `.sir/CHECKPOINT.md` with Now / Next step / Open promises / Re-read list
- Never ask owner; if blocked by permission, write single command to `OWNER_ACTIONS.md` and continue

---

## TASK 1: Fix 19 Failing Tests

**Files:** `src/sir_laptop_manager/ops_ui/server.py`, `tests/test_ops_ui_server.py`, `tests/test_tailnet_allowlist.py`  
**Brief:** The test suite reports 188 passed, 19 failed (per 2026-11-10 audit). Root cause: tests patch `ops_ui.server.execute_cleanup`, which no longer exists in the current codebase. Restore the function with its original signature in `server.py` OR update the tests to mock the new cleanup entry point. Run `uv run --offline pytest -q` iteratively until 0 failed. Update checkpoint with real pass count.  
**Acceptance:** `uv run --offline pytest -q` shows 0 failed, 207+ passed. Checkpoint updated with actual numbers.  
**Priority:** P0 — unblocks all milestones

---

## TASK 2: Harden `verify.ps1` with Evidence Output

**Files:** `scripts/verify.ps1`  
**Brief:** The current verify script does not fail on test failures and does not write evidence. Modify `scripts/verify.ps1` to: (1) run `uv run --offline pytest -q` and capture exit code; (2) run `ruff check src tests` and `mypy --strict src`; (3) run `gitleaks detect --source . --verbose`; (4) if any step fails, exit non-zero; (5) on success or failure, write a markdown file to `.sir/evidence/verify-latest.md` with date, command, exit codes, and real counts (tests passed/failed, ruff issues, mypy errors, gitleaks findings). Run it once to confirm the file shows real numbers.  
**Acceptance:** `scripts/verify.ps1` exits 0 only when all checks pass; `.sir/evidence/verify-latest.md` exists with real counts from the run.  
**Priority:** P0 — required for M0 exit check

---

## TASK 3: Push to GitHub & Record CI Run

**Files:** `.github/workflows/` (create if missing), any CI config  
**Brief:** Push the current state to `sirahmed8/sir-laptop-manager` (private). Ensure `.github/workflows/` contains a workflow that runs on push: `uv sync --dev`, `uv run --offline pytest -q`, `ruff check src tests`, `mypy --strict src`, `gitleaks detect`. If the Actions run is red, fix the failing step(s) and push again. Record the green run URL in `.sir/CHECKPOINT.md`. If CI quota is exhausted (flag file `ops/ci-quota-exhausted.flag` exists), run full local verification instead and paste passing output in checkpoint per WORKER_PREAMBLE.md rule 18.  
**Acceptance:** Green CI badge URL in checkpoint (or local verify output pasted per rule 18).  
**Priority:** P0 — required for M0 exit check

---

## TASK 4: Security Tests for Every POST Route

**Files:** `tests/test_ops_ui_security.py` (new), `src/sir_laptop_manager/ops_ui/server.py` (reference)  
**Brief:** Create `tests/test_ops_ui_security.py` with parametrized tests covering every POST route in `server.py`. Each test must assert: (1) path traversal attempts (e.g., `../../etc/passwd` in file-path params) return 400/403; (2) bad `Origin` / `Referer` headers (foreign domains) return 403; (3) missing or invalid CSRF HMAC token returns 403; (4) missing `Tailscale-User-Login` header returns 403 when not on loopback. A route without these guards must make the test fail. Run pytest until all security tests pass.  
**Acceptance:** `uv run --offline pytest tests/test_ops_ui_security.py -v` passes; any new POST route added without guards will cause a test failure.  
**Priority:** P1 — required for M3 security checklist

---

## TASK 5: Restore Drill Evidence

**Files:** `scripts/restore_drill.py` (new), `.sir/evidence/restore-drill.md` (output)  
**Brief:** Write a small script `scripts/restore_drill.py` that: (1) creates a temp file with known content in a test directory; (2) calls the quarantine API (`POST /api/cleanup/quarantine`) to move it to quarantine; (3) calls the restore API (`POST /api/cleanup/restore`) with the quarantine manifest ID; (4) computes SHA-256 of the original and restored files; (5) writes `.sir/evidence/restore-drill.md` with date, original hash, restored hash, and "MATCH" or "MISMATCH". Run it and confirm MATCH.  
**Acceptance:** `.sir/evidence/restore-drill.md` shows identical SHA-256 hashes for original and restored file.  
**Priority:** P1 — required for M1 exit check

---

## TASK 6: Licence Audit Script for 97 Legacy Skills

**Files:** `scripts/license_audit.py` (new), `.sir/evidence/skills-licences.csv` (output)  
**Brief:** Scan `legacy/antigravity-agent-suite/skills/` (97 skill folders). For each skill, detect licence from: `LICENSE` file, `package.json` `license` field, `SKILL.md` header, or GitHub repo `license` API. Output CSV with columns: `skill_name`, `detected_licence`, `source_url`, `decision` (keep/unknown). Skills with MIT/Apache-2.0/BSD/ISC → "keep". Unknown or non-permissive → "unknown". Save CSV to `.sir/evidence/skills-licences.csv`. Unknown skills are excluded from import (Task 7).  
**Acceptance:** CSV has 97 rows; every row has a licence or "unknown"; no row is empty.  
**Priority:** P1 — required for M1 agent config sync

---

## TASK 7: Port Keeper Skills with Manifest

**Files:** `src/sir_laptop_manager/agent_config/skills/` (new folder), `src/sir_laptop_manager/agent_config/skills/manifest.json` (new)  
**Brief:** For each skill marked "keep" in the licence audit CSV, copy the skill folder to `src/sir_laptop_manager/agent_config/skills/<name>/`. Create `manifest.json` with an array of objects: `{ "name": "...", "version": "...", "licence": "...", "source": "legacy/antigravity-agent-suite/skills/<name>", "copied_at": "ISO8601" }`. Run the agent config sync dry-run (`POST /api/agent-sync/dry-run`) and assert it lists the ported skills with 0 deletions.  
**Acceptance:** Sync dry-run response includes all ported skills; `deleted` array is empty.  
**Priority:** P1 — required for M1 agent config sync

---

## TASK 8: RAG Eval Set + Runner

**Files:** `tests/rag_eval/questions_ar.json`, `tests/rag_eval/questions_en.json`, `scripts/rag_eval.py` (new), `.sir/evidence/rag-eval.md` (output)  
**Brief:** Create 20 Arabic + 20 English grounded questions in the JSON files. Each question: `{ "question": "...", "expected_snippet": "...", "expected_file": "relative/path.md" }`. Questions must be answerable from the current corpus (`D:\Projects\_SIR\plans\`, `.sir\plans\`, `AI_Models_Hub\docs\`). Write `scripts/rag_eval.py` that: (1) loads the local `qwen` embeddings index; (2) runs each question through the RAG pipeline; (3) scores 1.0 if expected_snippet appears in top-3 results AND expected_file matches; 0.5 if only snippet matches; 0 otherwise; (4) prints per-question scores and overall percentage; (5) saves markdown report to `.sir/evidence/rag-eval.md` with date, scores, and overall %.  
**Acceptance:** `.sir/evidence/rag-eval.md` exists with 20 AR + 20 EN scores and overall percentage recorded.  
**Priority:** P2 — required for M4

---

## TASK 9: Telegram Weekly Report Builder + Privacy Filter

**Files:** `src/sir_laptop_manager/core/report.py` (new), `tests/test_report.py` (new)  
**Brief:** Implement `build_weekly_report()` in `core/report.py` that returns an Arabic string with: disk free C: & D: (GB), bytes freed this week (from quarantine manifest), quarantine size (GB), last backup date (from `.sir/evidence/`), failed tests count (from latest verify). Add `privacy_filter(text: str) -> str` that redacts any path containing user profile folders (`C:\Users\a7med\` except project names), private repo names, or the string "Habiba". Write `tests/test_report.py` asserting: (1) report contains all 5 metrics; (2) a test string with `C:\Users\a7med\Documents\private.txt` is redacted to `[private path]`; (3) project paths like `D:\Projects\SIR Laptop Manager\` are preserved. Real send test: call `scripts/deliver/send-telegram.mjs` with the report and assert API returns ok (requires owner's Telegram token in env).  
**Acceptance:** Unit test passes; privacy filter test proves private path redacted; real send returns API ok.  
**Priority:** P2 — required for Operations Standard 26

---

## TASK 10: Five-State Screenshots + Overflow Fix at 320/390px

**Files:** `scripts/capture_320.mjs`, `scripts/capture_390.mjs` (new or update), `.sir/evidence/m5/` (output folder)  
**Brief:** Extend the Playwright capture scripts to render the Cleanup tab and Game Mode tab at 320px and 390px viewports, in both English and Arabic, light and dark themes (8 captures per tab = 16 total). For each capture, assert `document.documentElement.scrollWidth <= window.innerWidth` (no horizontal overflow). If any capture fails, fix the CSS/layout (likely: table→card layout at <768px, `word-break: keep-all`, `overflow-wrap: anywhere`, flex-wrap on chip rows). Save all 16 screenshots to `.sir/evidence/m5/` with naming: `cleanup-320-en-light.png`, `cleanup-320-ar-dark.png`, etc. Update checkpoint with pass/fail per capture.  
**Acceptance:** All 16 captures pass `scrollWidth <= innerWidth`; screenshots saved in `.sir/evidence/m5/`; checkpoint updated.  
**Priority:** P2 — required for M5 quality sweep

---

## Notes for Agents

1. **Read first:** `.sir/CHECKPOINT.md`, `plans/sir-laptop-manager.md`, `ops/competitors/sir-laptop-manager.md`, `.sir/plans/FEATURE_GAPS.md`
2. **Environment:** `uv run --offline` for Python; `pytest`, `ruff`, `mypy` in dev deps; Playwright uses system Chrome/Edge (skips cleanly if absent)
3. **Secrets:** Never commit; use Windows Credential Manager or untracked `.env`
4. **Arabic/English:** Every UI string must have both; use `tr()`/`trf()` helpers; per-char bidi in inputs
5. **Five states:** Idle, loading skeleton, empty (one action), error (retry), populated
6. **Spring motion:** `cubic-bezier(0.16,1,0.3,1)`; transform/opacity only; matching open/close
7. **Commit message format:** `r52-laptop: <task title> — <one-line result>`
8. **After each task:** run `scripts/verify.ps1`, commit, push, update checkpoint, tick task in this file