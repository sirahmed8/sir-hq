# redesign-screen

Tools: gemini-plugin (mobbin). Source: C:\Users\a7med\.gemini\config\plugins\mobbin\skills\redesign-screen\SKILL.md (202 lines) + references/{scoping-round,scope-and-preserve,variations,collections,taste,before-after-board,report,reference-board,answering-a-challenge}.md

## Summary
Redesigns an existing screen using REAL product screens (Mobbin) as structural evidence: scope the target and freeze what must survive, search/lock references grouped by direction, plan max-5 moves each backed by cited screens, apply inside the product's own design system, verify against a six-check job walk, and report with a before/after image. Explore mode builds one variation per direction instead.

## When to use / not use
Use when someone has an existing screen (codebase, image, design file, live page) and wants a better version grounded in real-app precedent. NOT for greenfield design, copy changes alone, or when Mobbin tools aren't connected — the skill explicitly refuses to run on memory.

## Inputs, outputs, dependencies
Input: a source screen + optional user words/references/collections + mode flag (--explore/--targeted). Output: edits in the source's own form (code, design frame, PNG) + before/after render + evidence-cited report. Needs: Mobbin MCP (search_screens/search_sections/search_flows, list_collections/get_collection_contents), the job-walk method, plain-writing report style.

## Key rules
1. Evidence discipline: every claim cites the source, user's words, or a named Mobbin screen with mobbin_url; strength is stated (2+ products = precedent, 1 = example, 0 = labelled opinion). No "most apps", no remembered research, no claimed behavioral outcomes.
2. Structure from references, look from the user's design: take the reference's decisions, never its colors/typeface/copy; build only from the product's own design system tokens.
3. One direction taken whole — never mix two structural directions; max 5 moves, one per ticked problem, each with a roll call of screens showing that exact decision.
4. Freeze the baseline BEFORE searching: domain, design system, copy/data, everything outside target, user-requested preserves; problem list capped at 5, overflow goes to a Deferred record.
5. Verify by re-walking the render through the six job checks (path leads, info beside decisions, nothing missing, labels true, states complete, platform minimums) + 3 render checks, max 3 fix rounds; a failing move gets cut, not patched around.

## Risks / owner items
- Hard dependency on Mobbin connectivity and on reading every reference image — partial reads are explicitly forbidden.
- "Take the side whole" concentrates risk: a wrong direction choice propagates through all moves.
- Explore mode produces mockups only; applying a picked variation is a second pass.
- Taste/tone rules assume Western product-design conventions; the skill is Mobbin-centric.

## Category and tags
design, web — mobbin, redesign, design-research, evidence-based, ux.

## Revision note
Single plugin revision; the most procedurally rigorous skill in the slice (8 reference files, strict evidence taxonomy).
