# First 10 tasks for free agents: SIR Content Creation Studio

Queue-ready tasks (title plus one-paragraph brief each). Each task under 2 hours. Ordered by dependency. Free agents may run tasks 1-3 in parallel; 4 depends on 2; 5 depends on 4; 6 depends on 1; 7 depends on 3; 8 depends on 7; 9 depends on 8; 10 depends on 8.

## T1 - Deep scan of legacy and feature list
Read `legacy/SIR Content Creation Studio (v1)` and the inventory `ops/inventory/SIR-Content-Creation-Studio.md`; produce `.sir/reports/deep-scan.md` listing every feature with keep/drop and a note on tracked personal state files (profile, uid, pro flag, studio.db, audio files). Do not edit legacy. Done when: the file lists each feature with keep/drop and each personal-state file is named.

## T2 - Secrets report and key rotation plan
Scan legacy for the ~40 provider key names in `.env` (ignored), the 18 `curl-auth-header` hits under `.agents`/`.claude`, and the two Firebase admin JSON keys mentioned in the inventory; write `.sir/reports/secrets-report.md` with key names only (never values), which are tracked vs ignored, and a rotation order. Done when: report exists and names only key names, no values.

## T3 - Pin Python 3.12 and create the engine skeleton
Add `.python-version` (3.12), `pyproject.toml`, and CI using Python 3.12; create the FastAPI engine skeleton with `/health` returning 200 and a `/api/status` JSON. Done when: `uv run pytest` green and health returns 200 locally.

## T4 - Remotion minimal composition rendering a 5-second caption clip
Under `apps/render/`, create a Remotion composition that renders a 5-second 1080x1920 clip with a caption from JSON input. Done when: an MP4 file exists and ffprobe prints duration 5s.

## T5 - Arabic caption shaping test
Render a fixture Arabic sentence (RTL, with diacritics) in a frame and compare against a golden frame image. Done when: the image diff test passes and the frame shows connected Arabic with no diacritic clipping.

## T6 - License table and exporter check
Create `docs/LICENSES.csv` and an exporter check that refuses an asset with no licence row. Done when: a test fails when an asset has no licence row and passes when it does.

## T7 - Credential store wrapper for provider keys
Wrap the OS credential store (Windows Credential Manager) for provider keys; round-trip a key; ensure no key is in the repo (gitleaks). Done when: round-trip test passes and gitleaks is clean.

## T8 - Draft model and approval flow
Implement the draft state machine (draft, approved, scheduled, posted) with tests; an unapproved publish is refused. Done when: the unapproved-publish test passes and the state transitions are covered.

## T9 - Posting cap and audit log
Implement a per-account posting cap and an append-only audit log; tests for cap exceeded and append-only behaviour. Done when: the cap test passes and audit lines are append-only (test verifies).

## T10 - Dry-run publisher against a mock platform server
Implement a dry-run publisher that sends the right payload to a mock platform server with no real network call. Done when: the mock receives the expected payload and no real network request is made (test asserts).