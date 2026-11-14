# accidental-data-loss-prevention

Source read: `C:\Users\a7med\.claude\skills\accidental-data-loss-prevention\SKILL.md`.

## Summary
This is a mandatory safety gate for irreversible operations. Before running SQL that drops or truncates data, broad deletes, production storage removals, or infrastructure deletion, the agent must stop, explain the impact and why the action is needed, request explicit affirmative consent, and wait for the user before proceeding.

## When to use / when NOT
Use whenever a command or tool could cause irreversible data loss, including `DROP`, `TRUNCATE`, broad `DELETE`, `gsutil rm` or `gcloud storage rm` against production data, `gcloud projects delete`, or deletion of Spanner, BigQuery, Dataproc, secrets, or KMS resources. Do not bypass it for routine-looking tasks; when in doubt, ask. It is not needed for reversible edits, but it also does not replace backups or careful change design.

## Inputs, outputs, tools
Input is the exact command, tool call, or operation the agent is about to run. Output is either a consent request that names the impact, necessity, and requested approval, or normal execution after clear affirmative consent. There are no external tools or MCPs; it is a behavioral guardrail applied before shell, SQL, or cloud commands run.

## 5 most important rules
1. Halt execution before any destructive command runs.
2. Explain the concrete impact of the deletion or destruction.
3. Explain why the agent believes the action is necessary.
4. Request explicit approval and wait for a clear affirmative response.
5. Treat uncertainty as a reason to ask; the skill covers SQL, cloud storage, and infrastructure deletion patterns.

## Risks / owner notes
The operational cost is a short pause for confirmation, while ignoring the gate can cause permanent production data or infrastructure loss. The owner remains the final approval point for destructive actions, and agents should still prefer narrower, reversible operations when they satisfy the task.

## Category / tags
security · safety, data-loss-prevention, consent, sql, cloud-infra, guardrail, destructive-commands

## Revisions
The claude and gemini copies are identical in size and content; the claude copy is selected by the source rule. No codex, kilo, cursor, opencode, or windsurf copy was present.
