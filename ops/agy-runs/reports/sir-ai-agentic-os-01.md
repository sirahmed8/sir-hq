# sir-ai-agentic-os-01 — Agentic OS phase 1 kick-off report

Date: 2026-11-14
Project: `D:/Projects/SIR AI`
Branch: `main`
Commits pushed: `827b80f` (`feat(agentic-os): phase 1 CLI fleet registry and status panel`), `3f4fe3b` (`docs(checkpoint): sir-ai-agentic-os-01 phase 1 close-out`)

## Result

DONE. The phase-1 slice is implemented, verified locally, committed and pushed. The remaining work is explicitly documented in `docs/AGENTIC_OS_PHASE1.md` and `.sir/CHECKPOINT.md`.

## What the brief asked vs what was found

Brief source read: `D:/Projects/_SIR/ops/briefs/SIR_AI_AGENTIC_OS.md` and `D:/Projects/_SIR/ops/briefs/sir-ai-agentic-os-01.prompt.txt`.

Already real before this round:

- `packages/cli-bridge` had 12 adapters with real non-interactive args, permission modes, `which`/version/login probes, process spawning, outcome classification, cooldowns and rotation.
- `apps/agent` detected CLIs, synced the pool, ran queued tasks, heartbeated and published a minimal `clis` array to `users/{uid}/devices/{deviceId}`.
- `apps/web` already had Agents + Devices screens, Firestore watchers, five-state UI, bilingual RTL i18n and server-written agent collections.
- `packages/core/src/manager` already had queue, writer locks, pool cooldowns, runner rounds, watchdog, fallback and resource gate.

Gaps closed:

- No shared provider/routing/status contract for the fleet.
- `CliInfo`/Firestore `clis` carried only `id/installed/loggedIn/runnable`.
- `ModelPool.add()` reset cooldown/failure state on every re-sync and had no explicit routing priority.
- The web UI showed only compact chips for installed CLIs, not each adapter's real state.
- There was no unified chat event contract or event sink.

## Implemented

### Core domain model

- `packages/core/src/agentic.ts` (new): `AgentProviderKindSchema`, `AgentAdapterStateSchema`, `CliStatusSchema`, `ChatEventSchema`, `ChatEventSink`, `CliDetection`, `CliPoolHealth`, `adapterState()`, `toCliStatus()`, `sortCliStatuses()`.
- `packages/core/src/index.ts`: exports `./agentic`.
- `packages/core/src/manager/pool.ts`: `PoolEntrySchema.priority`, `ModelPool.list()`, `ModelPool.add()` preserves existing cooldown/failure/enabled state and accepts priority, `available()` sorts by priority then failures then provider id.

### CLI bridge registry and health

- `packages/cli-bridge/src/types.ts`: `CliInfo` now carries `label`, `providerId`, `providerLabel`, `providerKind`, `routingPriority`, `checkedAt`.
- `packages/cli-bridge/src/adapters.ts`: every adapter declares provider identity/kind and routing priority. Order implemented: `claude` 10, `antigravity-cli` 20, `devin` 30, `kilo` 40, `opencode` 50, `aider` 60, `codex` 70, `qwen-code` 80, `gemini-cli` 90, `cursor-agent` 100, `ollama` 110, `lm-studio` 120. This encodes `Claude > AGY > Devin > rest` with the free pool order inside "rest".
- `packages/cli-bridge/src/detect.ts`: `detectAll(runner, now)` returns full metadata from real `which`/version/login probes; sign-in stays `null` when a CLI cannot tell.
- `packages/cli-bridge/src/bridge.ts`: `CliBridgeOptions.onEvent`; `CliWorker` emits schema-valid `status` and bounded `output` events; `syncPool()` passes routing priority; `statuses(info?, now)` merges detection with pool health and returns sorted `CliStatus[]`.

### Agent publication and web panel

- `apps/agent/src/firestoreCommands.ts`: `writeClis()` accepts `CliStatus[]` and writes the full array with `clean()`.
- `apps/agent/src/main.ts`: `publishClis()` calls `syncPool()` once, then `statuses(info)` and publishes the result.
- `apps/web/src/data/remote.ts`: imports `CliStatusSchema`; `cliFromData()` validates new docs and safely maps legacy minimal docs to `unknown` state; device `clis` are sorted by routing priority.
- `apps/web/src/components/CliFleet.tsx` (new): fleet panel showing label, provider, version, route priority, state badge, cooldown-until, failures and last check time.
- `apps/web/src/screens/Devices.tsx`: replaces compact CLI chips with `CliFleet`.
- `apps/web/src/i18n/ar.ts` and `en.ts`: new `dev.fleet*` and `dev.adapter.*` keys.

### Docs and evidence

- `docs/AGENTIC_OS_PHASE1.md` (new): audit, contracts, routing order, wiring map, verification evidence and honest gaps.
- `.sir/TOOLS_INVENTORY.md`: committed the existing tool inventory (no secrets; keys remain in `_SIR/_local`).
- `.sir/evidence/agentic-os-a11y/after.json`: a11y audit result, 0 findings.
- `.sir/CHECKPOINT.md`: new round entry with verification and next step.

## Unified chat event skeleton

`ChatEventSchema` is a discriminated union supporting `user`, `assistant`, `thinking`, `tool_call`, `file_diff`, `output`, `fallback`, `error` and `status`. `CliBridge` emits real `output`/`status` events today; the thinking/tool/diff/fallback parser is the documented next slice. No mock events were added to production paths.

## Verification commands and real output

All run in `D:/Projects/SIR AI` on the final change set.

- `npm run typecheck` -> exit 0, clean across workspaces (`@sir-ai/ai-chain`, `cli-bridge`, `core`, `ui`, `agent`, `api`, `bot`, `desktop`, `web`).
- `npm test` -> exit 0:
  - `Test Files 34 passed (34)`
  - `Tests 332 passed (332)`
  - Includes new `packages/core/test/agentic.test.ts` (3) and `packages/cli-bridge/test/agentic-os.test.ts` (4).
- `npm run lint` -> exit 0 after removing one unused test import.
- `npm run build` -> exit 0, `vite v7.3.8` built in `16.60s`; pre-existing chunk-size warning only.
- Focused tests earlier: `npx vitest run packages/core/test/agentic.test.ts packages/core/test/manager.test.ts packages/cli-bridge/test/agentic-os.test.ts packages/cli-bridge/test/bridge.test.ts packages/cli-bridge/test/task9.test.ts` -> `5 passed`, `42 tests`.
- Browser/a11y: started Firebase auth+Firestore emulators and Vite dev server, installed Playwright chromium to `D:\Caches\ms-playwright`, then `node apps/web/e2e/a11y.mjs .sir/evidence/agentic-os-a11y after` -> `{ "label": "after", "total": 0, "byCheck": {} }`.
- `git diff --check` -> clean.
- `git status --short` after checkpoint commit -> clean.

## CI status (honest)

`gh run list --limit 3` showed the new push queued, then `gh run watch 43516044307 --exit-status` reported `failure` in ~2s with zero steps. `gh run view 43516044307 --json status,conclusion,displayTitle,jobs` returned:

```json
{"conclusion":"failure","displayTitle":"docs(checkpoint): sir-ai-agentic-os-01 phase 1 close-out","jobs":[{"completedAt":"2026-11-13T22:03:26Z","conclusion":"failure","name":"verify","startedAt":"2026-11-13T22:03:24Z","status":"completed","steps":[]}]}
```

`D:/Projects/_SIR/ops/ci-quota-exhausted.flag` is present, so this matches the known quota block; local gates above are the recorded proof. No CI green is claimed.

## Screenshots / visual evidence

No screenshots were captured. The a11y harness produced `.sir/evidence/agentic-os-a11y/after.json` with 0 findings; the fleet panel is covered by unit/schema tests and the web build/a11y run rather than a dedicated screenshot this round.

## Uncertainties and honest gaps

- `ChatEventSchema` and `onEvent` are real, but production currently emits `output`/`status` only. `thinking`, `tool_call`, `file_diff` and `fallback` need the stream parser.
- Sign-in state is still best-effort: CLIs without a reliable login probe report `loggedIn: null` and state `unknown` (or `ready` for local providers), never guessed.
- Hermes, OpenClaw, Droid/Factory, DeepSeek harness and Pi are mentioned in the vision/tools inventory but are not yet in `CLI_IDS`; they need real binaries/non-interactive contracts before joining the registry.
- The fleet panel reads what the desktop agent publishes; it does not spawn agents per view and does not invent fleet entries.
- Parked-provider rule from the brief (one provider = one strongest tool; OpenRouter shared by Factory + pool) is noted in docs but not enforced in code yet.

## Recommendations / next step

Exact next step recorded in `.sir/CHECKPOINT.md`: phase 2 stream parser that upgrades CLI stdout/stderr into `thinking`/`tool_call`/`file_diff`/`fallback` `ChatEvent`s, plus a minimal chat surface that consumes them. After that: manager picker and team roster, then Hermes/OpenClaw adapters once their local contracts are verified.

## Taskboard / bus / lock

- `python D:/Projects/_SIR/scripts/taskboard.py finish sir-ai-agentic-os-01 ...` moved `ops/tasks/active/5-sir-ai-agentic-os-01.md` to `ops/tasks/review/`.
- Team bus DONE note appended to `D:/Projects/_SIR/ops/bus/team.md`.
- Project lock `D:/Projects/_SIR/ops/locks/sir-ai.lock` is released after the done signal.
