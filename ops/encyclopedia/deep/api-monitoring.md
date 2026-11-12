# api-monitoring

Source read: `C:\Users\a7med\.gemini\config\plugins\postman\skills\api-monitoring\SKILL.md` (4.6 KB; gemini-plugin/postman).

## Summary
Skill for turning a saved collection into recurring evidence about a live API via Postman Monitors, including scheduling, runner choice, failure triage and verification.

## When to use / when NOT
Use when setting up recurring checks, running or diagnosing a Postman Monitor, changing its schedule, or reaching private APIs through a self-hosted runner. Do NOT use for one-off endpoint checks or simulation of failures; use api-testing and api-simulation.

## Inputs, outputs, tools
- Inputs: collection, cadence, execution location, alert recipients.
- Outputs: monitor configuration, run or job outcomes, metrics.
- Tools: postman monitor commands, postman runner commands, postman collection assertions.

## 5 most important rules
1. A 200 response is a weak health signal if the response can violate the contract; reuse meaningful assertions and check auth, target environment and write side effects.
2. `monitor create` and `monitor update` cannot change the collection or pause or resume a monitor; use pause and resume for those.
3. Use a self-hosted runner when the target is private; verify the runner is reporting in before assigning runs.
4. The CLI timeout caps waiting, not execution; after a timeout read the job with `monitor jobs get`.
5. In a CI gate run `monitor run` without `-x` so a failed run fails the build.

## Risks / things needing the owner
Monitor creation starts an immediate run by default; permanent monitor deletion needs explicit intent.

## Category / tags
Category: ops. Tags: api, postman, monitor, health-check, runners, alerts.

## Revisions
Single gemini-plugin/postman copy. No competing revisions.
