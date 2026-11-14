# discovering-gcp-data-assets (Gemini skill, Google)

## Summary
Discovery skill for finding and inspecting GCP data assets (BigQuery datasets/tables/views, BigLake, Spanner, GCS): prefer assets already in conversation; for `bigquery-public-data` skip Dataplex and inspect via `bq`/MCP directly; for everything else run Dataplex search (`gcloud dataplex entries search` or search_entries MCP) — semantic mode for natural language, keyword mode for technical strings — to get full `projects/...` entry names required by Lookup Context, then fetch schema/metadata/governance.

## When to use / when NOT
Use when finding/exploring/inspecting GCP data assets, when you have a keyword but not a resource ID, or instead of `bq ls`. Referenced by dbt-bigquery and dataform-bigquery for missing asset IDs. Do NOT use for non-GCP assets or when the asset was already identified earlier in the conversation.

## Inputs, outputs, tools
- Inputs: natural-language intent or technical keywords, optional known project/dataset.
- Outputs: full Dataplex entry names → schema/metadata/policy via Lookup Context.
- Tools: `gcloud dataplex entries search` (--semantic-search for NL, keyword syntax otherwise), Dataplex Lookup Context, `bq` CLI / BigQuery MCP for public datasets; requires dataplex API + `dataplex.entries.get`.

## 5 most important rules
1. Dataplex Lookup Context is mandatory for all GCP assets — even when IDs are known — because Step 4 needs the full entry name.
2. `--project` is always required for search but only attributes the call; it does NOT restrict scope — use `parent:` filters to scope.
3. Search syntax differs by mode: semantic uses UPPERCASE AND/OR + plural `labels.`; keyword is case-insensitive with singular `label.`, `|`=OR `,`=AND, `:`=token vs `=`=exact (required for system/type/location).
4. Keyword search: convert plurals to singular; semantic handles variants automatically.
5. `bigquery-public-data` tables bypass Dataplex — inspect directly with bq/MCP.

## Risks / things needing the owner
Requires Dataplex API enabled and IAM permissions in the attributed project. Search results may expose dataset names/descriptions — fine for discovery, but don't paste sensitive schema contents into external places.

## Category / tags
data · gcp, dataplex, bigquery, discovery, metadata

## Revisions
Single revision: `C:\Users\a7med\.gemini\skills\discovering-gcp-data-assets\SKILL.md` (v4, Apache-2.0, google). Only gemini tool holds it.
