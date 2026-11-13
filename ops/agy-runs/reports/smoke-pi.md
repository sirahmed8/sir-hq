# Smoke test: smoke-pi (Pi agent, free Groq model)

Date: 2026-11-13.

Task: smoke-pi. Folder: D:/Projects/_SIR. Brief: ops/briefs/smoke-pi.md and ops/briefs/smoke-pi.prompt.txt.

## What the brief asks

1. Run: python D:/Projects/_SIR/scripts/hq_team.py --help (only to see that it exists; do not run it).
2. Write ops/agy-runs/reports/smoke-pi.md listing the names and versions of these CLI tools as shown by their --version flags: codex, kilo, opencode, devin, gemini, agy, auggie, pi, and the cursor agent at C:/Users/a7med/AppData/Local/cursor-agent/agent.cmd. Mark any tool that fails.
3. Run: git add ops/agy-runs/reports/smoke-pi.md && git commit -m "smoke: pi test report" && git push origin main
4. Finish by writing the done marker: python D:/Projects/_SIR/scripts/agy-done.py smoke-pi ok "pi smoke report written and pushed"

REPORT AND SIGNAL (always, even on failure or when blocked):

1. Write the full report (everything done and found, file paths, commands and real output, screenshots taken, what is unsure, what is recommended next; no shortening) to D:/Projects/_SIR/ops/agy-runs/reports/smoke-pi.md.

2. Then run exactly: python D:/Projects/_SIR/scripts/agy-done.py smoke-pi <ok|fail|blocked> "<one line: result>"

3. The final reply may be short; the report file is what the manager reads.

## Checklist state

- Item 1: python D:/Projects/_SIR/scripts/hq_team.py --help. The brief says to only see that the file exists and not to run it. The file exists at D:/Projects/_SIR/scripts/hq_team.py (15615 bytes, modified 2026-11-12 14:50). Checked, not run. Ticked as satisfied by existence.
- Item 2: ops/agy-runs/reports/smoke-pi.md written in this round with the tool names and versions from the --version flags.
- Items 3 and 4: pending this round.

## Tool version results (captured in this session, 2026-11-13)

Commands run with the real shell. Every tool answered and every command exited 0.

- codex: command: /c/Users/a7med/AppData/Local/Programs/OpenAI/Codex/bin/codex --version. Output: codex-cli 0.167.2. Exit code: 0. Status: OK.
- kilo: command: /c/Users/a7med/AppData/Roaming/npm/kilo --version. Output: 7.8.27. Exit code: 0. Status: OK.
- opencode: command: /c/Users/a7med/AppData/Roaming/npm/opencode --version. Output: opencode v2.2.7. Exit code: 0. Status: OK.
- devin: command: /c/Users/a7med/AppData/Local/devin/cli/bin/devin --version. Output: devin 3000.12.32 (1126aba4a596). Exit code: 0. Status: OK.
- gemini: command: /c/Users/a7med/AppData/Roaming/npm/gemini --version. Output: 0.68.0. Exit code: 0. Status: OK.
- agy: command: /c/Users/a7med/AppData/Local/agy/bin/agy --version. Output: 1.5.7. Exit code: 0. Status: OK.
- auggie: command: /c/Users/a7med/AppData/Roaming/npm/auggie --version. Output: 0.37.1 (commit e8d38687). Exit code: 0. Status: OK.
- pi: command: /c/Users/a7med/.pi/agent/bin/pi --version. Output: 1.5.2. Exit code: 0. Status: OK.
- cursor agent: command: /c/Users/a7med/AppData/Local/cursor-agent/agent.cmd --version. Output: 2026.11.11-b912975. Exit code: 0. Status: OK.

Every tool on the brief list passed with exit code 0. No tool was marked failing.

## Runner history for this task

The autopilot runner (scripts/hq_autopilot.py -> scripts/cli-run2.sh) worked this task in several rounds. The log is D:/Projects/_SIR/ops/agy-runs/cli-smoke-pi.log.

- Round 1, tool opencode, model opencode/flint-40b-free, started 2026-11-13 05:17. The round read the worker preamble, the brief, git status, git diff and the last commits, and looked for the checklist file named in the brief.
- Round 1, tool opencode, model opencode/big-pickle, started 2026-11-13 05:53. Ended code 1, reason usage limit.
- Round 1, tool opencode, model opencode/glm-5.3-flash-free, started 2026-11-13 05:54. Ended code 1, reason usage limit.
- Round 1, tool agy, model claude-sonnet-4-6, started 2026-11-13 05:54. Ended code 3, reason usage limit.
- Round 1, tool cline, model reflection/beam-free, started 2026-11-13 05:55. Ended code 1, reason usage limit.
- Round 5, tool aider, model nvidia_nim/nvidia/nemotron-3-ultra-550b-a55b, started 2026-11-13 05:56. Ended code 0, result ok.
- Round 6, tool aider, model gemini/gemini-flash-lite-latest, started 2026-11-13 05:58. Ended code 0, result ok.
- Round 7, tool aider, model gemini/gemini-flash-latest, started 2026-11-13 05:59. Ended code 0, result ok.
- Round 8, tool pi, model radius/recursive/flint, started 2026-11-13 06:06.

The earlier rounds hit usage limits on free tiers and the later rounds finished ok. Round 8 was the last round at the time of this report.

## Local verification (CI substitute)

The CI quota flag ops/ci-quota-exhausted.flag exists (written 2026-11-12 17:42), so per worker rule 18 the full local verification replaces the GitHub Actions green check. The commands and real output:

- python -m compileall plans scripts. Output: compiled all plans and scripts modules. Exit code: 0.
- python plans/generate_dashboard.py. Output: generated D:/Projects/_SIR/ops/artifact/control-room.html (73443 bytes, hash a89b6fbd) at 2026-11-13 06:16. Exit code: 0.
- gitleaks detect --source . --config gitleaks.toml. Output: scanned 610 commits, 36633146 bytes, no leaks found. Exit code: 0.

## What is unsure

- The hq_team.py --help command was not run, because the brief forbids it. Only the file existence was checked.
- The cursor agent version is a date based build string (2026.11.11-b912975) and was captured from agent.cmd --version.
- The versions above are the CLI tool versions, not the model versions inside each tool.

## What changed in this round

- ops/agy-runs/reports/smoke-pi.md written with the smoke-pi result.

## Recommended next

- Finish item 3 (git add, commit, push) and item 4 (agy-done marker) for smoke-pi.
- Run the smoke-devin task next in the autopilot queue when a free slot opens.
