# performance-testing

- Tool: `gemini-plugin` (plugin: `postman`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\postman\skills\performance-testing\SKILL.md`
- SKILL.md size: 4319 chars

## What it does

Use when load-testing or benchmarking an API with concurrent virtual users and latency or error thresholds, or when importing or migrating a JMeter `.jmx` plan or a Gatling simulation (Java/Kotlin/Scala/JS/TS) into a Postman collection plus a `postman performance run` configuration. Reuses a collection to probe a chosen failure mode and distinguishes target limits from load-generator limits. Use for requests such as "load test this API", "import my JMeter plan", or "convert my Gatling project to Postman".

## Structure (headings inside SKILL.md)

- Performance Testing
- Importing from JMeter
- Importing from Gatling
- Verification
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. 1. Choose the failure mode before the profile: `fixed` tests sustained

## Files inside the skill

- `references/gatling-import/feeders.md` — "Feeders → data file + distribution"
- `references/gatling-import/injection.md` — "Load model: injection, throttle, duration, assertions → `postman performance run`"
- `references/gatling-import/mapping.md` — "Mapping: requests, EL, checks, protocol, flow, custom code"
- `references/gatling-import/README.md` — "Importing a Gatling project into Postman"
- `references/gatling-import/unsupported.md` — "What can't be carried over, and how to say so"
- `references/jmeter-import/import-report.md` — "Import Report — <TEST PLAN NAME>"
- `references/jmeter-import/mapping-table.md` — "JMeter → Postman mapping table"
- `references/jmeter-import/postman-perf-capabilities.md` — "What Postman performance testing supports (the import target)"
- `references/jmeter-import/README.md` — "Importing a JMeter `.jmx` into Postman"
- `references/jmeter-import/script-translation.md` — "Translating JSR223 / BeanShell scripts to Postman JavaScript"
