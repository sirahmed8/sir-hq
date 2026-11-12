# data-autocleaning (Gemini skill, Google)

## Summary
Mandatory pre-flight data-quality protocol for ANY task whose source is BigQuery or GCS — even trivial "move/copy table" asks. It requires Dataplex profiling (never ad-hoc BigQuery profiling) via `scripts/dataplex_scanner.py`: check eligibility, get explicit user approval for the scan command (approval covers all executions for the task), run concurrent scans with dynamic sampling for >1M-row tables, wait for results before finalizing transformations, then use the profile (null rates, distinct values, distributions) to drive cleansing and schema-mapping decisions. GCS sources need an external table created first; scan location must be a real region (us-central1), not multi-region.

## When to use / when NOT
MUST be used for any BigQuery/GCS-sourced operation — copying, moving, appending, ingesting, extracting — applied to the source node. Referenced by dbt-bigquery as a required sub-protocol. Do NOT skip for "simple" moves; do NOT substitute BigQuery-native profiling for Dataplex.

## Inputs, outputs, tools
- Inputs: BigQuery tables / GCS sources, `--tables`, `--location` (region), `--output-dir`.
- Outputs: JSON profile results driving cleaning/transformation decisions; feeds implementation_plan.md.
- Tools: `scripts/dataplex_scanner.py` (dataplex scans, dynamic sampling, concurrent polling), Dataplex API, BigQuery external tables for GCS.

## 5 most important rules
1. NEVER skip Dataplex profiling — Steps 1 and 3 are mandatory for every BQ/GCS task.
2. Get explicit user approval for the scanner command BEFORE running (present command + summary + value); approval covers the whole task.
3. Do not finalize transformations until the profile is available (unless user denied the scan).
4. GCS sources require an external table before scanning; location must be a specific region.
5. Dynamic sampling (>1M rows) and concurrent multi-table scans are handled by the script — pass all tables in one `--tables` call.

## Risks / things needing the owner
Dataplex scans cost money and need IAM permissions; user approval gate is explicit. Profile data may contain sample values — don't leak sensitive cell data into reports.

## Category / tags
data · bigquery, dataplex, data-quality, etl, gcp

## Revisions
Single revision: `C:\Users\a7med\.gemini\skills\data-autocleaning\SKILL.md` + `scripts/dataplex_scanner.py`. Only gemini tool holds it.
