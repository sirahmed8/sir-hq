# vercel-tracing

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\vercel-tracing\SKILL.md`
- SKILL.md size: 7306 chars

## What it does

Configure OpenTelemetry tracing for Vercel.

## Structure (headings inside SKILL.md)

- Vercel Tracing
- Reference index
- Setup workflow
- Investigation workflow
- CLI scope
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- 5. Build, deploy to preview or production, exercise a server-executed route, and [inspect its trace](references/inspection.md). Confirm span names and parent relationships with `inspect`, and `service.name` with search JSON. A local exporter check does not prove Vercel collection.

## Key rules (verbatim lines from SKILL.md)

1. 1. Check existing setup: framework and adapter versions, any registered OpenTelemetry provider or Sentry v8+, and framework tracing flags. Extend an existing provider; never register a second one.
2. 5. Change the measured cause, keeping its span. After deploying, compare that span and the whole request across equivalent requests under similar load and collection settings. Report before and after timings, sample counts, errors, and remaining uncertainty.

## Files inside the skill

- `references/capture.md` — "Targeted capture"
- `references/collection.md` — "Collection prerequisites"
- `references/configuration.md` — "Sampling rules reference"
- `references/context-propagation.md` — "Context propagation"
- `references/custom-spans.md` — "Custom spans"
- `references/inspection.md` — "Inspect a trace"
- `references/instrumentation.md` — "Application SDK setup"
- `references/library-spans.md` — "Library spans"
- `references/nextjs.md` — "Next.js instrumentation"
- `references/performance.md` — "Measure and improve performance with custom spans"
- `references/search.md` — "Span search reference"
- `references/sveltekit.md` — "SvelteKit instrumentation"
- `references/troubleshooting.md` — "Missing or incomplete traces"
