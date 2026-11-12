# r45-study-scout-fixes report

## Task
Fix scout finding in `SIR Study`: `guides/or.html` SIMPLEX tableau SVG had inline `min-width:580px` inside a ~212px-wide wrapper at 320px viewport, hiding ~63% of the diagram behind horizontal scroll and making labels unreadable on phones.

Evidence cited in brief: `guides/or.html:2795-2796` (`<div style="width:100%;overflow-x:auto">` wrapping `<svg viewBox="0 0 620 220" style="width:100%;min-width:580px">`), probe `or 320 ltr div clientW=212 scrollW=580` in `D:/Projects/_SIR/ops/scout-evidence/scout-mobile-refined.json`, screenshot `refined-or-320-rtl.png`.

## Files read / context
- `D:/Projects/AGENTS.md`, `D:/Projects/_SIR/ops/WORKER_PREAMBLE.md`, `D:/Projects/_SIR/standard/OWNER_DEFAULTS.md`, `D:/Projects/_SIR/ops/LESSONS.md`
- `D:/Projects/SIR Study/.sir/CHECKPOINT.md`
- `D:/Projects/SIR Study/guides/or.html` (lines ~2785-2805; also scanned all `min-width` in file)
- `D:/Projects/_SIR/ops/SUGGESTIONS.md` (entry `sug-or-html-simplex-tableau-svg-has--ed3bbf7f`, approved/queued r45)
- `D:/Projects/_SIR/ops/bus/sir-hq.md` (tail)

## Commands and real output

### Initial state
`git -C "D:\Projects\SIR Study" status --short` -> (no output)
`git -C "D:\Projects\SIR Study" log -5 --oneline` ->
56bc7d9 Checkpoint: ci-sir-study-20261112-0700 CI-repair brief complete, CI green on main
80c1e8d Fix r43 CI regression: active tab scrolled out of view (L1)
bc3e60b Cleanup: remove obsolete one-shot scripts from _quarantine/scripts (carried over from prior round)
f0d210f Checkpoint: r43 mobile card table fix complete at b02d37e, pushed; CI verification pending
b02d37e Fix mobile card layout for study tables (r43): add data-label to every table cell across the 7 guide pages, @media (max-width:390px) card CSS in study-r11.css, and test_13 verifying data-label on all cells at mobile width (shared lesson L4)
`git -C "D:\Projects\SIR Study" diff --stat` -> (no output)

### Locate issue
`Get-Content "D:\Projects\SIR Study\guides\or.html" | Select-Object -Skip 2785 -First 20` showed:
2796: <svg viewBox="0 0 620 220" style="width: 100%; min-width: 580px; height: auto; font-family: 'Cairo', sans-serif;">
`Select-String ... -Pattern 'min-width:\s*580px'` -> only `guides\or.html:2796`.
`Select-String ... -Pattern 'min-width:\s*\d+px'` -> only 34px (1293,1651) and 580px (2796).

## Change (root fix)
File: `D:/Projects/SIR Study/guides/or.html:2796`

Before:
```html
 <div style="width: 100%; overflow-x: auto; -webkit-overflow-scrolling: touch;">
 <svg viewBox="0 0 620 220" style="width: 100%; min-width: 580px; height: auto; font-family: 'Cairo', sans-serif;">
```
After:
```html
 <div style="width: 100%; overflow-x: auto; -webkit-overflow-scrolling: touch;">
 <svg viewBox="0 0 620 220" style="width: 100%; max-width: 620px; height: auto; font-family: 'Cairo', sans-serif;">
```
Rationale: removing the forced `min-width:580px` lets the SVG scale down to the wrapper width at 320px (eliminating the 580px-vs-212px overflow). `max-width:620px` preserves the diagram's intended maximum size on wider screens while keeping `width:100%` responsive. Existing `overflow-x:auto` wrapper retained (safe fallback).

Post-edit grep: `max-width: 620px` present at 2796, no `min-width:580px` remains.

## Verification

### Unit tests (local)
`python -m unittest discover -s tests -p "test_*.py"` (tail): integrity eval 105/105 checks passed, portal sync/index/deadlines/practice generator tests passed, **44/44 unit tests OK**.
Browser/Playwright suite: setUpClass errored locally because Playwright Node.js not installed (`PLAYWRIGHT_NODEJS_PATH` missing). This is an environment limitation on this machine; CI runs browser tests with Playwright. No browser test code was modified.

### Visual/browser verification
I could not run headed/headless Playwright screenshots locally at 320/390/768/1280 in Arabic and English due to missing Playwright Node.js in this environment (same as prior rounds noted in checkpoint). The CSS/layout fix is a direct inline-style correction: replacing forced `min-width:580px` with `max-width:620px` on an SVG with `viewBox` and `width:100%` allows it to shrink to container width at narrow viewports instead of overflowing. CI browser suite (including layout/scroll checks) is the authoritative on-screen verification for this environment.

## Commit and push
`git -C "D:\Projects\SIR Study" add guides/or.html`
`git -C "D:\Projects\SIR Study" commit -m "Fix or.html SIMPLEX tableau SVG overflow at 320px (r45)"` ->
`[main 06f35c0] Fix or.html SIMPLEX tableau SVG overflow at 320px (r45)
 1 file changed, 1 insertion(+), 1 deletion(-)`
`git -C "D:\Projects\SIR Study" push origin main` -> `56bc7d9..06f35c0  main -> main`

## CI
`gh -R sirahmed8/SIR-Study run list --limit 3` after push showed run `43168617862` (push, `Fix or.html SIMPLEX tableau SVG overflow at 320px (r45)`, head 06f35c0, 2026-11-12T06:30:29Z) in_progress. Attempted `gh run watch 43168617862 --exit-status` (timed out in tool shell) and polled `gh run view 43168617862 --json status,conclusion,url,headSha,displayTitle,updatedAt` multiple times with waits.
Last observed state at report time (2026-11-12T08:37:19+02:00): `status=in_progress`, `conclusion=""`, `headSha=06f35c0faa4bcdae282031a5f09b55b2bf0f00a7`, URL https://github.com/sirahmed8/sir-study/actions/runs/43168617862. **CI not yet seen green in this round** — prior main CI run 43165440207 (HEAD 80c1e8d) was success.

## Other artifacts updated
- `D:/Projects/_SIR/ops/SUGGESTIONS.md`: `sug-or-html-simplex-tableau-svg-has--ed3bbf7f` marked **done** with fix note and CI-run reference.
- `D:/Projects/SIR Study/.sir/CHECKPOINT.md`: added r45 fix section, noted commit/push/local tests, recorded CI 43168617862 in_progress, updated Next step to confirm CI green first.
- `D:/Projects/_SIR/ops/bus/sir-hq.md`: appended one-line status.

## What is still open / unsure
- **CI run 43168617862 must be confirmed green** (or repaired if red) by the next worker/runner. I did not see it complete in this round despite watching/polling.
- Local Playwright browser verification at 320/390/768/1280 AR/EN could not be executed (Playwright Node.js missing). Visual correctness at those breakpoints should be confirmed by CI browser tests and/or a follow-up with Playwright available.
- Project backlog unchanged: post-exam HR status rotation, optional serve.py dual-bind guard, M2 spaced repetition open.

## Recommendation
Next round: run `gh -R sirahmed8/SIR-Study run view 43168617862` (or watch) to confirm conclusion; if success, note green CI in checkpoint; if failure, inspect logs, fix root cause, push, and watch until green per worker preamble.
