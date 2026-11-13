# Instruction parity across free tools (review, no product code)
Folder: D:/Projects/_SIR. Goal: every free tool reads the same rules: D:/Projects/AGENTS.md, D:/Projects/GEMINI.md, plans/CLI_AGENT_INSTRUCTIONS.md, plans/GEMINI_QUALITY_CHARTER.md, standard/23-premium-code-bar.md.
1. For each tool (Cursor agent, Pi, Devin, Kilo, OpenCode, Codex, Antigravity agy, Auggie) check how it loads project instructions (its config file or a flag). Use the tool's --help and its config folder. Read only; do not change settings outside _SIR.
2. Write ops/agy-runs/reports/parity-instructions.md: a table tool | instruction file it reads | loads AGENTS.md? | loads skills? | gap.
3. For each gap that can be closed inside _SIR (for example a prompt preamble in ops/WORKER_PREAMBLE.md), add it. Do not touch AHome.
4. Commit and push to main. Done marker: python D:/Projects/_SIR/scripts/agy-done.py parity-instructions ok "<one line>".
