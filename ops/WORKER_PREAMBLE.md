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

11. Browser tests: always close the browser in a `finally` block, run headless, mute audio (launch arg `--mute-audio`, and stub `speechSynthesis.speak` to a no-op), and never leave a browser running when you stop. A leaked test browser read an Arabic law guide aloud at night (2026-11-11).
12. Messages to the owner (Telegram and chat): first line is a short title in plain words; then at most 5 lines, each one fact (what, where, what it means for him); numbers with their meaning; no run-on sentences, no file paths or commit hashes, no mix of Arabic and English in one sentence except product names; end with "المطلوب منك: لا شيء" or the single tap needed. Same format for every agent.

13. Every SIR product has its OWN Firebase project and its OWN GitHub repository named exactly after the product (for example SIR Restaurant gets "sir-restaurant", never the project of another product). Check first: if a project and repo with the right name already exist, reuse them; if the product was living in another product's project, create the new project and repo (free Spark plan, `firebase projects:create`, `gh repo create --private`), move the app there, and write both names in the checkpoint. Never reuse AHome's project for anything else.
14. The owner's CV and profiles say "Vibe Coder" (builds products by directing AI). Never write programming tracks, certificates, years of experience or skills that are not proven by his real projects.

15. Every web product that has a public site is hosted twice: Firebase Hosting and Vercel (import the GitHub repo with the Vercel CLI, which is installed and signed in), same build, so when one host is down the other serves. Write both addresses in the checkpoint and check both with curl (retry once on timeout).

16. Read D:/Projects/_SIR/standard/OWNER_DEFAULTS.md at the start: it lists the owner's standing defaults. When you build something reusable (component, rule, fix) that other projects should adopt, add one line under a new heading 'Adopted from <project>' in that file and write a short note in D:/Projects/_SIR/ops/bus/sir-hq.md so HQ queues the adaptation for the others.

17. Before sending ANY message to the owner (Telegram or otherwise), read the last 15 lines of D:/Projects/_SIR/ops/bus/telegram-outbox.md: if another agent/duty already told him the same thing in the last couple of hours, do not repeat it (merge into your message instead, or skip). After sending, append one line there (timestamp | your name | one-line summary, no full text). Also read D:/Projects/_SIR/ops/PERSONAL_NOTES.md before writing a check-in or a recommendation, and if you learn something real and non-private about him during your work, append one line there so the rest of the team stays personalized. Never write anything about Habiba or AHome in either file.

## Finishing
Only when every checklist line is fixed with proof or honestly marked open with the reason, CI on `main` is green, and the report is written to `D:/Projects/_SIR/ops/agy-runs/reports/<task>.md` (what changed, commands run with real output, what is still open), run:
`python D:/Projects/_SIR/scripts/agy-done.py <task> ok "<one line>"`
If you cannot finish, do NOT run it. The runner keeps going with the next model.

18. GitHub Actions minutes are used up (2026-11-12, flag file `ops/ci-quota-exhausted.flag`, expected reset around 2026-12-01): CI jobs fail in about 3 seconds with zero steps. That is the quota, not your code. While the flag file exists, "CI green" is replaced by: run the full local verification (tests, lint, build) and paste the passing output into the checkpoint; still commit and push to main. Never loop on CI fixes. When the flag file is deleted, rule 4 (CI must be seen green) applies again.

19. Tools are shared: never wait for your own tool alone; if your tool stops, the next task goes to another tool automatically. Tasks that only write new files under ops/ may be marked parallel_ok in the queue and run beside other work in the same folder.

20. Rescan before work (owner, 2026-11-12): before you build or change anything in a project, re-read the whole project (folder, legacy source, plans/<slug>.md, .sir/CHECKPOINT.md, ops/bus, its TickTick map row) and FIRST improve the plan: more research, a more detailed plan, more and smaller tasks, written to the plan files and logged in the project's .sir/PLAN_REFRESH.md with the date. Do this once when a project starts and again at every milestone start. Plans for every project must also follow plans/PRODUCT_DIRECTION_2026-11-12.md.

21. Browser tabs (owner, 2026-11-12): never open a browser tab for a quota, billing, rate-limit or docs page. When a model says a payment method is needed, that model is simply unusable: move on, do not open the link. If you opened a tab for your task, close it when you finish. Only open pages the task truly needs.

22. Team board (owner, 2026-11-12): the whole team is one team. Before you start, read the last 40 lines of ops/bus/team.md; append one line when you start (`<time> <tool> START <task> <what>`), when you finish (`DONE <task> <result>`) and when you stop for a limit (`HANDOFF <task> <exactly where you stopped and what is left>`). If you see a task nobody is working on (queue open, no START in the last 30 minutes), take it. Never repeat what DONE lines say is finished. Building products is only allowed on the current projects (SIR Study, SIR Jobs, SIR AI, SIR Laptop Manager, SIR Portfolio and AHome, all by the free tools); every other project is PLANNING ONLY until the owner says build.

23. Task board (owner, 2026-11-12): work lives as files in ops/tasks/ (inbox -> active -> review -> done, reports in ops/tasks/reports). `python scripts/taskboard.py list` shows it. When you finish your task, run `python scripts/taskboard.py next <your-tool>`: it claims the next unclaimed inbox task for you and prints the file, then do it. Write progress with `python scripts/taskboard.py note <task> "<text>"`, stop for a limit with `handoff <task> "<where you stopped>"` (it goes back to the inbox so another tool continues from your note), and `finish <task> "<result>"` when done. Write one report per round in ops/tasks/reports/<task>.md (what was done, evidence, what is left, ideas for new tasks). You may add follow-up tasks yourself with `python scripts/taskboard.py add <name> "<folder>" "<title>" <brief.md>`, except building in a planning-only project. Review each other: a task in review/ can be checked by any tool that did not do it (read its report and the diff, write ops/verifications/<task>.md with PASS or FAIL and the reasons). The manager reads the reports and adds new tasks.

24. TickTick and the browser (owner, 2026-11-12): never press Ctrl+P or any shortcut with `computer type/key` on a web page; use sir_ctl `browser fill/click` on elements instead, or the TickTick Open API. If a print dialog appears (a Chrome window titled Print), press Escape at once and note it in ops/bus/team.md. Close every tab you opened when you finish.


## Browser rule (owner, 2026-11-13)
Never open a visible browser window or tab on the owner's PC (no Chrome, no Edge, no Claude in Chrome). Use headless Playwright only (chromium.launch(headless=True)). Do not open localhost ports in a visible browser; the owner sees stray tabs.
