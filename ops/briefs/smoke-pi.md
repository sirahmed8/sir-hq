# Smoke test for the Pi agent (free Groq model)
Folder: D:/Projects/_SIR. Read only the files named here; edit nothing else.
1. Run: python D:/Projects/_SIR/scripts/hq_team.py --help (only to see that it exists; do not run it).
2. Write ops/agy-runs/reports/smoke-pi.md listing the names and versions of these CLI tools as shown by their --version flags: codex, kilo, opencode, devin, gemini, agy, auggie, pi, and the cursor agent at C:/Users/a7med/AppData/Local/cursor-agent/agent.cmd. Mark any tool that fails.
3. Run: git add ops/agy-runs/reports/smoke-pi.md && git commit -m "smoke: pi test report" && git push origin main
4. Finish by writing the done marker: python D:/Projects/_SIR/scripts/agy-done.py smoke-pi ok "pi smoke report written and pushed"
