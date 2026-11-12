# direct-action-shield

## Summary
A response-style protocol that bans conversational filler (greetings, apologies, recaps, "let me know") and enforces a fixed reply anatomy: numbered actions taken, surgical diffs/code with clickable file links, verification proof (build/test output), and one immediate next step. Includes a small mermaid flow: Inspect → Execute → Verify → Output.

## When to use / when NOT
Use in any agent session where terse, execution-first replies are wanted — it is essentially the operating rule already used across SIR worker preambles. Do NOT use for teaching/explaining contexts where the user asked for narrative, or for owner-facing messages that have their own mandated format (WORKER_PREAMBLE rule 12).

## Inputs, outputs, tools
- Inputs: the user's request.
- Outputs: structured replies — numbered actions, minimal diffs, verification output, next step.
- Tools: none; pure communication discipline.

## 5 most important rules
1. No preamble greetings or "happy to help" openers.
2. No apologies-as-preamble — fix the mistake directly.
3. Number what was done; show only relevant code, link full files.
4. Always attach verification proof (test/build/runtime output).
5. End with one actionable next step, not an open-ended offer.

## Risks / things needing the owner
Over-application can read as curt to non-technical stakeholders; owner-facing Telegram messages follow a different mandated format and must not be squeezed into this anatomy.

## Category / tags
ai · communication, style, agent-behavior

## Revisions
Six tools hold it plus gemini-plugin; bodies byte-identical, only `description` differs. Claude copy preferred for trigger-style description.
