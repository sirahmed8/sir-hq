# Worker operating manual (read first, every round). Written by HQ 2026-11-10 after reading the failed rounds.

You are a coding worker started by the SIR autopilot (`scripts/hq_autopilot.py` -> `scripts/cli-run2.sh`). Several models take turns on one task: the model before you was cut by a quota limit and you continue where it stopped. Nothing you remember survives; only files do.

## Where the truth is
- Laws: `D:/Projects/AGENTS.md`. Project rules: `<project>/AGENTS.md`. State: `<project>/.sir/CHECKPOINT.md`. Your task: the brief named in your message and its checklist file. Review findings: `D:/Projects/_SIR/ops/reviews/2026-11-10/`.
- Start every round with `git status`, `git log -5` and `git diff --stat`. Uncommitted edits are the previous model's work: read them, finish or fix them, never revert them.

## How to work (lessons from real failures)
1. Small steps. After each finished item run the checks, commit, push to `main`, tick the checklist, update the checkpoint. A quota cut can come in the middle of a command.
2. Never leave `main` broken. A refactor (splitting files, moving exports) is done in one go: change the file, every importer and the tests together, run `node --check`/tests, and only then commit. If a round starts and the tree does not run, repair that first. (Round on 2026-11-10: a half-finished split left `telegram-ledger.mjs` importing an export that did not exist.)
3. "Green" means you saw it. After a push run `gh run list --limit 3`, wait for the run (`gh run watch <id>` or poll every 2 minutes) and read the result. Never write "all gates green" or "verified" without that output pasted in the report. A red CI run is the first thing to fix in the next round.
4. Shell: the tool shell on this PC is PowerShell 5, not bash. `&&` does not chain commands there; use `;` or separate calls. Quote any path with a space: `cd "D:\Projects\SIR Jobs"`. In Git Bash use `/d/Projects/...`. Prefer `git -C "<folder>" ...`.
5. Web search tool may ask permission and crash a non-interactive run. Use `curl`, a fetch tool, or Firecrawl instead. Never put private data in a query.
6. Private data: never open the AHome vault, messages, notes or photos; never write the names of private people into tracked files, logs or reports.
7. Do not stop to ask. Decide, write the decision in the checkpoint, continue. If something needs the owner (sign-in, 2FA, payment, CAPTCHA) write one tiny exact step in `D:/Projects/_SIR/ops/OWNER_ACTIONS.md` and continue with the rest.
8. If you hit a quota message ("usage limit", "too many requests"): write what is done and the exact next step into the checkpoint, commit, and stop. The runner switches to the next model by itself.
9. One tool call that prints thousands of lines wastes your context: pipe long output through `tail -40` or `Select-Object -Last 40`.
10. Quality: `D:/Projects/_SIR/standard/23-premium-code-bar.md`. No placeholders, no mock data, no emoji, no em-dashes in copy, version stays 1.0.0, never delete `legacy/`.

## Finishing
Only when every checklist line is fixed with proof or honestly marked open with the reason, CI on `main` is green, and the report is written to `D:/Projects/_SIR/ops/agy-runs/reports/<task>.md` (what changed, commands run with real output, what is still open), run:
`python D:/Projects/_SIR/scripts/agy-done.py <task> ok "<one line>"`
If you cannot finish, do NOT run it. The runner keeps going with the next model.
