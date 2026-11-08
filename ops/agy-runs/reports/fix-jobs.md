# fix-jobs report (2026-11-08)
- scripts/scheduled_run.ps1: node now gets separate args via Invoke-Step (&$Exe @args), checks exit code after every step, logs FAILED and exits with the code; default is LIVE, -Offline is opt-in; test hooks SIR_NODE_BIN, SIR_JOBS_ROOT.
- scripts/register-scheduler.ps1:48: removed -Offline; task SIR-Jobs-Weekly-Digest re-registered user-level (Mon 08:00), reversible with -Operation Unregister.
- IP/token: verify.ps1:34-36, test/test-pipeline.mjs:216-217 built by concatenation; remoteok fixture and test-digest.mjs use a synthetic token. git grep for the literals outside legacy/ = 0 hits (history untouched).
- Askable link: WWR returns 403 to scripts (Cloudflare), but the live WWR RSS feed lists the same URL, so it is live; kept.
- test/test-scheduled-run.mjs (added to npm test): failing node => exit 3, log says FAILED, no "Finished Successfully".
- Proof: Start-ScheduledTask run 12:11, LastTaskResult 0, log "mode LIVE ... Finished Successfully", 586 live items from 5 sources, SIR Life jobs.json rewritten 12:11:20.
- npm test green (7 suites, 0 fail); scripts/verify.ps1 "all green".
- Not done: perpetual UX/security lens cycles (skipped per instruction).
