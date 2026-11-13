# AHome: free-tools fallback for hard tasks

Read first: D:/Projects/AHome/AGENTS.md, D:/Projects/AHome/apps/local-core/data/smart_ai_router.py, D:/Projects/AHome/infra-daemons/telegram_assistant.py, D:/Projects/_SIR/plans/CLI_AGENT_INSTRUCTIONS.md, D:/Projects/_SIR/ops/FREE_TOOLS_ORGANIZATION.md.

Owner requirement: AHome is local-AI only and private (never send Habiba/private content to outside providers). But when a task is too hard for local qwen, the system may escalate NON-PRIVATE work to the free CLI pool (kilo, opencode, devin-cli, agy, codex, gemini, kimi, qwen, goose, crush, cline, aider) through the existing fallback chain, with cooldowns and a hard cap on concurrent heavy workers (max 2 AI-heavy processes at once to protect the 24GB RAM).

This cycle:
1. Audit smart_ai_router.py: confirm private content can NEVER route to a cloud provider (P2/P3 stays local), and map where escalation would hook in.
2. Implement a bounded escalation path for P0/P1-classified tasks only: try local Ollama first, on failure/weak result escalate to the free CLI pool via the existing ask.ps1/fallback chain, respecting cooldown state in ops/backup-manager state files. Keep it opt-in/config-flagged if unsure.
3. Add/adjust tests; run the project test suite; commit and push to main; update .sir/CHECKPOINT.md.

Constraints: AHome private content never leaves the PC. Version stays 1.0.0. No PRs. Commit straight to main.
