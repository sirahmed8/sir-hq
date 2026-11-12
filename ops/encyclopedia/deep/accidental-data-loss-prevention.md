# accidental-data-loss-prevention

Source read: `C:\Users\a7med\.claude\skills\accidental-data-loss-prevention\SKILL.md` (1.3 KB; claude revision; not found in codex/kilo/cursor/windsurf/opencode).

## Summary
A mandatory safety gate that stops any agent from executing commands causing irreversible data loss without explicit user consent. Covers SQL DROP/TRUNCATE/broad DELETE, cloud storage rm on production buckets, and infrastructure deletion (projects, Spanner, BigQuery, Dataproc, secrets, KMS keys). The rule is absolute: halt, explain impact and necessity, request explicit approval, wait for affirmative consent.

## When to use / when NOT
Use ALWAYS when any tool/command matches the destructive patterns listed. Do NOT bypass even if the task seems routine; the cost of a false positive (waiting for consent) is near zero, the cost of a false negative is catastrophic.

## Inputs, outputs, tools
- Inputs: the command or tool call the agent is about to run.
- Outputs: either a consent request to the user, or (after consent) the command proceeds normally.
- Tools: none; this is a behavioural guardrail applied before any shell/gcloud/gsql execution.

## 5 most important rules
1. **STOP AND VERIFY**: Never execute a destructive command without halting first.
2. **Explain impact**: Clearly state what data/resources will be lost and why the action is proposed.
3. **Request explicit consent**: Ask for a clear, affirmative "yes" from the user.
4. **Wait for consent**: Do not proceed until the user explicitly approves.
5. **Scope**: Applies to SQL DROP/TRUNCATE/broad DELETE, `gsutil rm`/`gcloud storage rm` on production, and `gcloud projects delete` or resource deletions (Spanner, BigQuery, Dataproc, secrets, KMS).

## Risks / owner notes
Low operational risk; the only cost is a brief pause for consent. The real risk is an agent ignoring this skill — if that happens, data loss is irreversible. Owner must be the final gate on any destructive infra action.

## Category / tags
ops · safety, data-loss-prevention, guardrail, consent-gate, sql, cloud-infra

## Revisions
Only the claude copy exists (1.3 KB). The skill is not present in the codex/kilo/cursor/windsurf/opencode 112-set. This is the canonical version.