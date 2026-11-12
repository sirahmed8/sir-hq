# datasets (Postman)

## Summary
Skill for Postman dataset manifests — giving files and database sources a queryable interface via local `.dataset.yaml` manifests, federated SQLite querying (default) or native `--source` dialects, saved views for reusable test input, and two consumption modes: `--iteration-data-dataset`/`--iteration-data-view` for row-per-iteration runs (parameter-free views only) vs repeatable `--dataset` exposing `pm.datasets()` to scripts. Covers source add/query/view create, JDBC inspect, credential boundaries (vault refs vs literal storage), and failure interpretation.

## When to use / when NOT
Use when a collection needs queried/joined test inputs, a reusable named view, spreadsheet/database rows, or script access. A one-off CSV/JSON iteration can stay with `collection run -d` — a dataset must earn its config. Do NOT use for simple single-file fixtures or when live DB auth isn't worth it.

## Inputs, outputs, tools
- Inputs: file/URL/JDBC/database sources, `.dataset.yaml` manifests, queries with positional `$1` params.
- Outputs: queryable datasets, saved views, iteration data, `pm.datasets()` in scripts.
- Tools: `postman dataset create|source add|query|view create|jdbc inspect`, `collection run --iteration-data-*`/`--dataset`; reference/schema.md + spreadsheets.md.

## 5 most important rules
1. Prefer local file sources for reproducibility; live DB adds auth/entitlement/network/credential requirements even locally — check actual CLI capability first.
2. Federated SQLite is default; `--source` switches to native dialect — don't switch modes just to silence SQL errors (changes semantics); JDBC can't join in federation.
3. Credential boundary matters: JDBC accepts `vault:<id>/<secret>` refs; native DB creds store literally in YAML — keep secret-bearing config out of Git.
4. Iteration flags feed one row per iteration and exclude `-d`, require parameter-free views; `--dataset` exposes pm.datasets() but doesn't create iterations — choose deliberately.
5. File sources copy into data_dir unless `--ref-only` (absolute paths, machine-specific); `--upload` is what actually uploads bytes to a workspace dataset.

## Risks / things needing the owner
Literal DB credentials may persist in dataset YAML — vault refs preferred. Workspace dataset deletion is permanent. `data.db`/`meta.db`/daemon.log engine state must stay out of git.

## Category / tags
data · postman, datasets, testing, jdbc, credentials

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\postman\skills\datasets\SKILL.md` + reference/{schema,spreadsheets}.md. Only gemini-plugin holds it.
