# api-documentation

Source read: `C:\Users\a7med\.gemini\config\plugins\postman\skills\api-documentation\SKILL.md` (gemini-plugin revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
An API documentation skill that creates and maintains human-readable documentation for REST APIs. It takes OpenAPI/Swagger files and generates interactive documentation, client SDKs in multiple languages, and developer guides. The skill can also reverse-engineer documentation from living API traffic, keeping docs in sync with code changes. It supports multiple output formats (HTML, Markdown, PDF) and can publish to internal doc sites or CDNs.

## When to use / when NOT
Use when you need to generate or update API documentation for a team or project. Do NOT maintain documentation manually if the API changes frequently — the skill keeps docs in sync with the living specification. Do NOT skip the example generation step; the skill creates curl examples and client code snippets that are the most valuable part of the documentation for developers.

## Inputs, outputs, tools
- Inputs: OpenAPI/Swagger YAML/JSON file, output format (html, markdown, pdf), publication target (internal CDN, internal wiki).
- Outputs: interactive HTML documentation, client SDKs (TypeScript, Python, Java), markdown summary, publication-ready files.
- Tools: Swagger UI, OpenAPI generator scripts, Node.js for format conversion, MkDocs for publication, CDN upload. MCP: gemini-plugin connector.

## 5 most important rules
1. **Always keep the OpenAPI source file version-controlled** — the skill regenerates docs from this source; if it's lost, the docs cannot be regenerated.
2. **Generate client SDKs for the languages your team uses** — the skill supports TypeScript, Python, Java, Go, and Ruby; generate only the ones you need to avoid bloat.
3. **Include real request/response examples** — the skill creates curl commands and response schemas; these are the fastest way for developers to understand endpoint usage.
4. **Publish to an internal doc site with search** — the skill can output to MkDocs, Docusaurus, or a simple HTML file; searchable docs are essential for developer adoption.
5. **Update docs on every API change** — integrate the skill into your CI pipeline so that every PR that modifies the OpenAPI spec triggers doc regeneration.

## Risks / owner notes
The most common failure is forgetting to update the OpenAPI source file; the skill will regenerate docs from whatever is in the source, which may be stale. The owner should enforce that PRs must update the OpenAPI file before merging. Generated SDKs may require additional configuration (auth settings, base URL) before they are production-ready.

## Category / tags
api · documentation, openapi, developer-experience, sdk, sdk-generation, publishing

## Revisions
The gemini-plugin copy is the only revision available; no codex, claude, or kilo versions exist. This is the canonical source for this skill.