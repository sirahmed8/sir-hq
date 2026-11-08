Use your skills and tools as you see fit: plan first, use teamwork/sub-agents for independent parts, keep going until the done-when checks pass.

Task: Implement SIR Jobs T-009 / T-010 (Automated Feed Sync & Shortlist Staging).
Read: D:/Projects/SIR Jobs/.sir/TASKS.md, shortlist-2026-11-08.md, and `D:/Projects/SIR Life/data/feeds/jobs.json`.
Work in D:/Projects/SIR Jobs:
1. Verify `data/feeds/jobs.json` adheres to the Feeds contract required by SIR Life:
   `{ "project": "jobs", "generatedAt": ISO, "status": "ok", "items": [...] }`.
2. Ensure `scripts/digest/run.mjs` writes clean, non-leaking items to `D:/Projects/SIR Life/data/feeds/jobs.json` with zero IP tokens, zero non-Egypt listings, and truthful profile match tags.
3. Run `npm test` and `pwsh scripts/verify.ps1`.
Done when: verify passes with 0 leaks, full report written.
