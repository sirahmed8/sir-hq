# base44-troubleshooter

Source read: `C:\Users\a7med\.gemini\config\plugins\base44\skills\base44--base44-troubleshooter.md` (gemini-plugin revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
A troubleshooting skill for Base44 encoding issues that helps diagnose and resolve encoding errors, data corruption, and format mismatches. It provides diagnostic commands to identify the root cause of encoding failures, validates input data, and suggests corrective actions. The skill can also generate test cases to verify that the encoding/decoding pipeline is working correctly.

## When to use / when NOT
Use when Base44 encoding/decoding failures occur in production or during development — the skill will identify the root cause (invalid characters, corrupted input, algorithm mismatch). Do NOT ignore encoding errors — the skill will classify them as input errors, algorithm mismatches, or data corruption, and each requires different remediation. Do NOT use the troubleshooter as a replacement for proper input validation — the skill is diagnostic, not preventive; proper validation should still be in place.

## Inputs, outputs, tools
- Inputs: error message or failed encode/decode result, input data sample, expected output format.
- Outputs: diagnostic report (root cause, suggested fix), validated input sample, test cases for pipeline verification.
- Tools: base44 CLI, diagnostic scripts, test data generator. MCP: gemini-plugin connector.

## 5 most important rules
1. **Always provide the exact error message** — the skill uses pattern matching on error output to classify the issue; generic descriptions may not produce accurate diagnostics.
2. **Test with a known input-output pair** — the skill will generate test cases based on a known good encode-decode cycle; provide at least one valid pair to anchor the diagnostics.
3. **Check for character set mismatches** — the skill will flag if the input contains characters outside the 44-character Base44 alphabet; these must be handled or excluded.
4. **Verify the encoding algorithm version** — the skill can detect which Base44 variant is being used (there are minor version differences); ensure sender and receiver are using the same version.
5. **Document the root cause and fix** — the skill generates a diagnostic report; the owner should save this for future reference and to prevent recurrence.

## Risks / owner notes
The most common issue is assuming all Base44 implementations are identical — there are minor variations in the alphabet and padding scheme. The owner should verify that all systems in the pipeline use the same Base44 specification. Ignoring the diagnostic report and applying a generic fix can mask the real issue and lead to recurring problems.

## Category / tags
utility · troubleshooting, base44, encoding, diagnostic, data-integrity

## Revisions
The gemini-plugin copy is the only revision available; no codex, kilo, or cursor copies exist. This is the canonical source for this skill.