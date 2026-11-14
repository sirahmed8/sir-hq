# bulk-create (canva-bulk-create)

## Summary
Canva skill that produces one design per row of tabular data by autofilling a brand template's data tags. Accepts any tabular source (uploaded file, pasted table/JSON, URL), inspects the template's field schema, maps columns to fields, uploads image URLs to Canva assets first, then calls autofill-design sequentially per row with progress tracking and a final success/failure report.

## When to use / when NOT
Use when the user wants batch generation from a template: "one design per product", "bulk create from CSV", "autofill a template from a spreadsheet". Requires a Canva Enterprise plan (autofill feature). Do NOT use for editing an existing design (use edit-design) or for single designs; do NOT promise undo — there is no bulk undo.

## Inputs, outputs, tools
- Inputs: tabular data (headers + rows), brand template ID or search query, optional column→field mapping overrides.
- Outputs: one Canva design per row (with URLs), plus a summary (total/successes/failures) and optional summary CSV.
- Tools (MCP): Canva:search-brand-templates, get-brand-template-dataset, upload-asset-from-url, autofill-design.

## 5 most important rules
1. Autofill needs Canva Enterprise; confirm plan before starting large runs.
2. Inspect the template dataset first to get exact (case-sensitive) field names and types.
3. Image fields need Canva asset IDs — upload URLs immediately before that row's design so failures stay localised; never pass raw URLs to autofill-design.
4. Call autofill-design sequentially, not in parallel, to respect rate limits and ease debugging; continue past row failures.
5. Confirm the column→field mapping with the user before bulk run; offer a 3-row test run for CSVs of 50+ rows; warn that there is no undo.

## Risks / things needing the owner
Autofill is a paid/Enterprise-gated capability — verify entitlement. Large batches make N API calls and create real designs (cost/quotas). Broad find-and-replace-style mistakes aren't applicable here, but wrong mappings create many bad designs quickly; the approval/mapping confirmation gate is the safeguard. Skipping image fields leaves template defaults.

## Category / tags
design · canva, bulk, autofill, templates, batch, mcp

## Revisions
Single revision: active plugin copy at `C:\Users\a7med\.gemini\config\plugins\canva\skills\bulk-create\SKILL.md`. No inactive duplicate. Skill name in frontmatter: canva-bulk-create.