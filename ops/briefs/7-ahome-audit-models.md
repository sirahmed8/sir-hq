# Audit AHome local AI models and fallback chain

## Context
AHome has a fallback chain for local AI models (Ollama, LM Studio, etc.). The chain may be stale or misconfigured. Audit the current setup and verify the chain works.

## Required
1. Read `D:/Projects/AHome/.sir/CHECKPOINT.md` and `D:/Projects/AHome/AGENTS.md` (if exists) for context.
2. Check the current fallback chain config:
   - Look for `ollama` or `lm-studio` in `D:/Projects/AHome` source.
   - Find the model fallback chain (e.g., in `src/lib/` or `config/`).
   - List all configured models and their priorities.
3. Verify each model in the chain:
   - Check if Ollama is running (`ollama list`).
   - Check if LM Studio is running (if applicable).
   - Test one simple prompt through each model (e.g., "Say hello").
4. Check for any broken links or missing models.
5. Write a short report to `ops/agy-runs/reports/7-ahome-audit-models.md` with:
   - Current chain (list models in order).
   - Which models are available and working.
   - Any issues found (e.g., model not installed, service not running).
   - Recommendations (e.g., update chain, install missing model).

## Done when
- Report file is written and committed.
- `ops/verifications/7-ahome-audit-models.md` confirms the audit was completed.

## Notes
- Do not open private AHome content (messages, notes, photos, vault).
- Only source code, config files, and service status.
- If a model is missing, note it but do not install (that is a separate task).