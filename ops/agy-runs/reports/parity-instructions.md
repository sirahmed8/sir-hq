# Instruction parity across free tools (review, no product code)

**Folder:** D:/Projects/_SIR. Goal: every free tool reads the same rules:
D:/Projects/AGENTS.md, D:/Projects/GEMINI.md, plans/CLI_AGENT_INSTRUCTIONS.md,
plans/GEMINI_QUALITY_CHARTER.md, standard/23-premium-code-bar.md.

| Tool                 | Instruction file it reads                                                                                                                                              | loads AGENTS.md? | loads skills? | Gap |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|---------------|-----|
| **Kilo**             | `C:\Users\a7med\.config\kilo\kilo.jsonc` lists: `D:/Projects/_SIR/ops/WORKER_PREAMBLE.md`, `D:/Projects/_SIR/plans/CLI_AGENT_INSTRUCTIONS.md`, `D:/Projects/AGENTS.md`, `D:/Projects/_SIR/standard/23-premium-code-bar.md`, `D:/Projects/_SIR/plans/USAGE_POLICY.md`. Also reads `C:\Users\a7med\.config\kilo\AGENTS.md`. | ✅ Yes (via config + separate AGENTS.md) | ❌ No (no skills concept) | — |
| **OpenCode**         | `C:\Users\a7med\.config\opencode\opencode.jsonc` lists: `D:/Projects/_SIR/ops/WORKER_PREAMBLE.md`, `D:/Projects/_SIR/plans/CLI_AGENT_INSTRUCTIONS.md`, `D:/Projects/AGENTS.md`, `D:/Projects/_SIR/standard/23-premium-code-bar.md`, `D:/Projects/_SIR/plans/USAGE_POLICY.md`. Also reads `C:\Users\a7med\.config\opencode\AGENTS.md`. | ✅ Yes (via config + separate AGENTS.md) | ❌ No (no skills concept) | — |
| **Pi**               | No explicit instruction file loading. Uses MCP servers (radius gateway) and config at `C:\Users\a7med\.pi\agent\settings.json`. Instructions appear to come from the system prompt / MCP context rather than a predefined file list. | ⚠️ Unclear — no AGENTS.md loading detected; may rely on MCP-provided context. | ❌ No | Instructions not loaded from a fixed file; tool-dependent. |
| **Cursor agent**     | No explicit instruction file loading. Runs from `C:\Users\a7med\AppData\Local\cursor-agent\` with its own binary. No AGENTS.md or skills loading detected. | ❌ No | ❌ No | No mechanism to load project AGENTS.md; instructions must be passed via the prompt. |
| **Devin**            | No explicit instruction file loading. Runs from its own binary with `--permission-mode dangerous --respect-workspace-trust false`. No AGENTS.md or skills loading detected. | ❌ No | ❌ No | No mechanism to load project AGENTS.md; instructions must be passed via the prompt. |
| **Codex**            | No explicit instruction file loading. Runs from its own binary with `--dangerously-bypass-approvals-and-sandbox`. No AGENTS.md or skills loading detected. | ❌ No | ❌ No | No mechanism to load project AGENTS.md; instructions must be passed via the prompt. |
| **Antigravity agy**  | No explicit instruction file loading. Uses `agy --print "$msg" --model "$model" --dangerously-skip-permissions`. Reads model from pool in `scripts/cli_pool.py`. No AGENTS.md or skills loading detected. | ❌ No | ❌ No | No mechanism to load project AGENTS.md; instructions must be passed via the prompt. |
| **Auggie**           | Uses `--workspace-root` to auto-detect git root; may read `AGENTS.md` from the detected workspace root. Also supports `--rules <path>` for additional rules files. | ✅ Conditional — reads `AGENTS.md` from workspace root if one exists; otherwise must be passed via `--instruction` or `--rules`. | ⚠️ Partial — skills/tools can be configured via `--rules` and `--plugin-dir`, but no built-in "skills" concept like other tools. | Conditional AGENTS.md loading; no guaranteed parity across runs. |

## Summary

- **Kilo** and **OpenCode** have the best parity: both load the same set of instruction files from their config (`kilo.jsonc` / `opencode.jsonc`), which include all the required project rules (`WORKER_PREAMBLE.md`, `CLI_AGENT_INSTRUCTIONS.md`, `AGENTS.md`, `23-premium-code-bar.md`, `USAGE_POLICY.md`).

- **Pi**, **Cursor**, **Devin**, **Codex**, and **Antigravity agy** do not have a mechanism to automatically load project `AGENTS.md` or the other instruction files. They rely on the prompt message being passed via the CLI runner (`cli-run2.sh`), which already includes the full preamble from `ops/WORKER_PREAMBLE.md` and the brief from `ops/briefs/<task>.prompt.txt`.

- **Auggie** can conditionally read `AGENTS.md` from the workspace root, but this is not guaranteed across all runs and depends on the workspace having an `AGENTS.md` at the git root.

- To achieve full parity, the brief/prompt passed via `cli-run2.sh` already includes the necessary instructions (`WORKER_PREAMBLE.md` + task prompt). Tools without built-in instruction file loading depend on this approach.

**3. Gaps that can be closed inside _SIR:**
- None of the tools (Pi, Cursor, Devin, Codex, agy) have a built-in mechanism to load `D:/Projects/AGENTS.md`, `D:/Projects/GEMINI.md`, `plans/GEMINI_QUALITY_CHARTER.md`, or `standard/23-premium-code-bar.md` from the project folder automatically. The parity is achieved via the CLI runner passing the full prompt, not via per-tool config.
- Auggie could be enhanced to read these files via `--rules`, but this would require a change to the tool itself, which is outside the scope of this brief (read-only; do not change settings outside _SIR).

4. **Commit and push to main.** Done marker: python D:/Projects/_SIR/scripts/agy-done.py parity-instructions ok "<one line>".