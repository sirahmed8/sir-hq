# Report: normal-sir-ai-runnable-adapters-01

See canonical task report at `D:\Projects\_SIR\ops\tasks\reports\normal-sir-ai-runnable-adapters-01.md`.

Summary:
- Registered and implemented `hermes`, `openclaw`, `droid`, and `pi` as runnable `CliAdapter` entries in `D:\Projects\SIR AI\packages\cli-bridge` (`16/16` `CLI_IDS` now in `RUNNABLE_ADAPTERS`; 0 detect-only adapters remain).
- Verified host binary presence and `--version` for all four CLIs on this PC (`Hermes Agent v0.23.1`, `OpenClaw 2026.11.1 (4ffdd20)`, `droid 1.10.0`, `pi 1.5.2`).
- Local gates passed: `npm run typecheck` (exit 0), `npm run lint` (exit 0), `npm test` (`34 test files passed, 341 tests passed`, exit 0), `npm run build` (exit 0).
