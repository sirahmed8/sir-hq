# notebook-guidance

Tools: gemini (Google-published, Apache-2.0, version v5).
Source: C:\Users\a7med\.gemini\skills\notebook-guidance\SKILL.md (326 lines, read in full; no scripts/references folder)

## Summary
Google's guidance skill for Jupyter notebook work, especially BigQuery analysis. It decides when a notebook is warranted (insights, charts, stateful exploration — not single-number lookups), enforces a cell-by-cell generate→execute→validate loop when an execute tool exists, and lays down strict BigQuery rules: use `%%bqsql` BigFrames magics instead of the Python client, stay in BigFrames/BQML rather than pandas/scikit-learn, and finish with a structured markdown summary.

## When to use / not use
Use for multi-step data analysis, exploration, visualization, or explicit .ipynb requests, particularly against BigQuery. Skip it for simple fact lookups (row counts, schema previews) — a plain query answer is cheaper.

## Inputs, outputs, dependencies
Input: an analysis question plus (for BigQuery) a `project.dataset.table` ID found via asset discovery. Output: an executed, clean notebook with visualizations and a summary cell. Needs: a live kernel (local Python with `bigframes>=2.38` + `ipykernel`, or remote Spark/Colab), the `execute_cell` tool for the incremental flow, and optionally `managing-python-dependencies` and `ml-best-practices` companion skills.

## Key rules
1. Behavior branches on tool availability: with `execute_cell`, one cell at a time and inspect output before continuing; without it, generate the whole notebook and ask the user to run it.
2. Hard stop on any kernel error — never scaffold more cells until a kernel is confirmed active.
3. BigQuery access is `%%bqsql <df_name>` magics only; never `google.cloud.bigquery` or `read_gbq`; never mix Python into a magic cell; always name the output dataframe.
4. Keep cells small (one transformation or plot each), clean failed attempts before presenting, and end with a markdown summary containing only Q&A / Key Findings / Insights sections.
5. Plotting: distinct colors per feature, sized figures without overlapping legends, inline figures; line charts only for continuous data; PCA to 2D before cluster scatter plots.

## Risks / owner items
- Requires a working Python kernel and BigQuery access; in environments without them the skill degrades to "generate and ask the user to run".
- Its anti-pandas stance is opinionated — fine for BigQuery scale, wasteful for small local CSVs.
- References `@skill:` companions (discovering-gcp-data-assets, ml-best-practices) that may not exist outside Google's agent environment.

## Category and tags
study, data, build — jupyter, bigquery, bigframes, data-analysis, visualization, python.

## Revision note
Single Google revision (v5); only one copy on the machine.
