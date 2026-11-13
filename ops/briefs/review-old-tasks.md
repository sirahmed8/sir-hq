# Verify three old "done" claims that have no PASS report (verifier)
Folder: D:/Projects/_SIR. Pick, in order, the first three names from ops/AUTOPILOT_QUEUE.json with done true whose ops/agy-runs/reports/<name>.md has no word PASS in it: r60-build-sir-jobs, r60-build-sir-study, r60-build-sir-portfolio.
For each: read its report, run the test command that report names (or npm test / the project's verify script), record exact counts. Write ops/agy-runs/reports/verify-<name>.md with PASS or FAIL and evidence. Do not change product code; if it fails, list the file and line.
Commit reports only, push to main. Done marker: python D:/Projects/_SIR/scripts/agy-done.py review-old-tasks ok "<one line>".
