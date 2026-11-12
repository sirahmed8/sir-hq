# Report: audit-sir-study-20261112-1401-fix1

Task: fix every item that failed verification of `audit-sir-study-20261112-1401`.
Verification file: `D:/Projects/_SIR/ops/verifications/audit-sir-study-20261112-1401.md`.
Only item 6 failed: "Ship at least 10 visible improvements with before and after
screenshots under `.sir/evidence/`." — 7 pairs existed, 6 claimed improvements had
no pair.

## What I found on arrival

The previous model had already done most of the fix but not committed it:

- 14 before/after PNG pairs under
  `.sir/evidence/20261112-1401/improvements/{before,after}/` (01–14), including
  new emulated pairs for color-scheme, prefers-contrast, reduced-motion,
  portal-empty, toast-tap-dismiss, read-progress chip, streak card and ics button.
- `COVERAGE.md` rewritten (14 pairs, honest method notes), `contact-sheet.png`,
  `metrics.json` (14 shots per side).
- New tooling: `scripts/evidence_shots.py`, rewritten `scripts/audit_1112_shots.py`,
  `scripts/verify_improvement_pairs.py` (pixel diff in Chromium + contact sheet).
- New guard `tests/test_evidence_pairs.py` (5 tests).
- `tests/test_browser.py` test_15 extended with color-scheme and
  prefers-contrast computed-style assertions.
- `.sir/PLAN_REFRESH.md` (rule-20 rescan log) and new tasks T-110–T-113 in
  `.sir/TASKS.md`; PLAN.md M5 gained the evidence line and an open running-exam line.
- Regenerated brand icons (`assets/brand/icon.ico`, `icon.png`, `folder.ico`)
  left dirty by the project's icon tooling.

## What I did

1. Verified the inherited work: `python -m unittest tests.test_evidence_pairs -v`
   → 5/5 OK; `test_15_audit1401_visible_improvements` → OK (20.5s).
2. Committed it: `bad69de` "Ship 14 proven before/after improvement pairs for
   audit-20261112-1401" (46 files: pairs, COVERAGE.md, metrics.json,
   contact-sheet.png, scripts, tests, PLAN/TASKS/PLAN_REFRESH/status.json,
   browser_report.json, .gitignore `.aider*`).
3. Committed the regenerated icons separately: `57747b3`.
4. Fixed the open defect the rescan had logged (T-111, now the first unchecked
   M5 line): the hub showed `00:00:00:00` and "exam over" during the exam hour.
   - `guides/START_HERE.html`: duration-aware `endDate` (two-hour exams),
     `running` state → `tag-live` status tag (new pulsing green CSS),
     `hub.timer.live` countdown to exam end, hero badge `hub.hero.badgeLive`,
     hero digits count down to `endDate`, `heroKey` tracks the live flag so the
     hero repaints at exam start/end.
   - `guides/i18n.js`: `hub.tag.live`, `hub.timer.live`, `hub.hero.badgeLive`
     in both EN and AR dicts.
   - `tests/test_browser.py::test_19_r46_running_exam_state`: routes a mocked
     `exams.json` (hr exam 30 min in the past) and asserts tag-live, live timer,
     live hero badge, ~30-minute digits, past exam still `tag-done`, plus
     computed-style proof of the `sirRise`/`sirTick` animations (T-112).
     Passes locally (4.1s).
5. Ticked T-111 and T-112 in TASKS.md and the M5 line in PLAN.md. T-113 left
   open honestly: marking the Human Rights exam done is owner data; the hub
   already flips to done/next-exam by the clock.
6. Full local verification (CI quota flag `ops/ci-quota-exhausted.flag` present;
   latest GH run 43267084590 failed in 4s with 0 steps = quota, not code):
   `PLAYWRIGHT_NODEJS_PATH="/c/Program Files/nodejs/node" python -m unittest
   discover -s tests -p "test_*.py"` → **Ran 68 tests in 714.979s — OK**;
   integrity eval appended: **73/73 refused, 32/32 answered, 105/105 checks
   passed**.
7. Pushed to main: `bad69de`, `57747b3`, `d4800b4`, `267ffd7` (checkpoint).

## Item-6 evidence summary

- 14 pairs (requirement was ≥10), each a real visible change; `metrics.json`
  records before/after URLs (`:3320` worktree `661a0d9` vs `:3310` main) and
  per-pair diff percentages (0 failed the pixel check: "14 pairs, 0 failed").
- `tests/test_evidence_pairs.py` fails the build if a pair is missing, blank,
  identical, or absent from COVERAGE.md — the evidence cannot rot silently.
- Pairs needing emulation (color-scheme, contrast, reduced-motion, fixtures)
  are documented as such in COVERAGE.md; motion-only improvements
  (scrollbar-width, content-visibility, stagger) are covered by computed-style
  assertions in test_15/test_19 instead of fake screenshots.

## Still open / notes

- T-113 (owner data step): mark HR exam done / rotate hub — clock handles state
  automatically; left for the owner/coached round.
- Follow-up discovered: the 7 subject guides carry hardcoded per-guide
  countdowns that also say "تم الامتحان" inside the exam hour; same live-state
  pattern can be ported from the hub later.
- CI on main is red only because the Actions quota flag exists; per
  WORKER_PREAMBLE rule 18 local verification substitutes and was green.

## Commands run (real output)

- `python -m unittest tests.test_evidence_pairs -v` → Ran 5 tests, OK.
- `PLAYWRIGHT_NODEJS_PATH=... python -m unittest tests.test_browser.BrowserAcceptance.test_15_audit1401_visible_improvements` → OK (20.5s).
- `PLAYWRIGHT_NODEJS_PATH=... python -m unittest tests.test_browser.BrowserAcceptance.test_19_r46_running_exam_state` → OK (4.1s).
- `PLAYWRIGHT_NODEJS_PATH=... python -m unittest discover -s tests -p "test_*.py"` → Ran 68 tests in 714.979s, OK; integrity 105/105.
- `git push origin main` → `a70cc30..267ffd7 main -> main`.
- `gh run list --limit 3` → latest run 43267084590 "failure" in 4s (quota flag present).
