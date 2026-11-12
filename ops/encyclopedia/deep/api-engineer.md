# api-engineer

Source read: `C:\Users\a7med\.gemini\config\plugins\postman\skills\api-engineer\SKILL.md` (gemini-plugin revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
An API engineering skill that designs, builds, and tests REST APIs following best practices. It helps design endpoint structures, generate OpenAPI specifications, implement request validation, and write automated tests. The skill enforces REST constraints, produces consistent error responses, and generates test suites that can be run against the implemented API. It aims to reduce the friction between API design and implementation.

## When to use / when NOT
Use when designing a new API or refactoring an existing one — the skill ensures consistency and adherence to REST principles. Do NOT use for quick, undocumented endpoint additions without design review — the skill will flag deviations from REST best practices and request a proper design. Do NOT skip the test generation step; the skill produces test skeletons that serve as contract testing foundation.

## Inputs, outputs, tools
- Inputs: API design requirements, endpoint list, data models, authentication method.
- Outputs: OpenAPI 3.0 specification, request validation code (Zod, Yup, or Joi), test suite (pytest or Jest), design review report with violations and recommendations.
- Tools: OpenAPI Editor, Postman, code generators (openapi-generator), test frameworks (pytest, Jest). MCP: gemini-plugin connector.

## 5 most important rules
1. **Always design with versioning in the URL** — the skill enforces `/v1/`, `/v2/` patterns and will reject version-less endpoint designs.
2. **Use consistent error response format** — the skill generates a standard error schema (`error: { message, code, timestamp, path }`) that all endpoints must follow.
3. **Generate validation code for request bodies** — the skill outputs Zod (JS/TS), Pydantic (Python), or Schema (Ruby) schemas that validate incoming data before it reaches your handler.
4. **Write tests that exercise the full request lifecycle** — the skill creates tests that cover valid data, invalid data, authentication failures, and edge cases.
5. **Run the design review report before implementing** — the skill lists all deviations from best practices; address these before writing any code.

## Risks / owner notes
Skipping the design review and implementing directly can lead to inconsistent APIs that are difficult to maintain. The owner should address all design violation recommendations before implementation. Generated test suites may need customization for your specific framework; the skill provides skeletons that require adapter code.

## Category / tags
api · design, development, openapi, testing, rest, validation, code-generation

## Revisions
The gemini-plugin copy is the only revision available; no codex, claude, or kilo versions exist. This is the canonical source for this skill.