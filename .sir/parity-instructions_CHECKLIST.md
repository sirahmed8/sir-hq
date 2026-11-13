# parity-instructions checklist

- [ ] 1. Audit how each free tool loads project instructions (config / --help / config folder). Read only outside `_SIR`.
- [ ] 2. Write `ops/agy-runs/reports/parity-instructions.md` table: tool | instruction file | loads AGENTS.md? | loads skills? | gap.
- [ ] 3. Close every gap that can be fixed inside `_SIR` (preamble, runner, project rule files). Do not touch AHome. Do not edit settings outside `_SIR`.
- [ ] 4. Commit and push to main. Local verify while `ops/ci-quota-exhausted.flag` exists. Done marker: `python scripts/agy-done.py parity-instructions ok "<one line>"`.
