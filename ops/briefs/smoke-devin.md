# Check the Devin worker is active (free SWE-2 model)
Folder: D:/Projects/_SIR. Read only the files named here; edit nothing else.
1. Run: python D:/Projects/_SIR/scripts/cli_pool.py status and paste its output.
2. Read ops/agy-runs/model-pool.json and report the devin entry (last_pick, last_ok, until).
3. Write ops/agy-runs/reports/smoke-devin.md with those facts and one sentence saying whether Devin answered a test prompt in this run.
4. Run: git add ops/agy-runs/reports/smoke-devin.md && git commit -m "smoke: devin status report" && git push origin main
5. Finish by writing the done marker: python D:/Projects/_SIR/scripts/agy-done.py smoke-devin ok "devin status report written and pushed"
