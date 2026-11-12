# omniroute-resilience-gateway

- Tool: `claude`
- Category: ops
- Source: `C:\Users\a7med\.claude\skills\omniroute-resilience-gateway\SKILL.md`
- SKILL.md size: 1908 chars

## What it does

Use when routing AI model calls through a gateway that must fail over to secondary providers on rate limits or quota exhaustion.

## Structure (headings inside SKILL.md)

- OmniRoute Resilience Gateway (Multi-Provider Model Routing)
- 1. Gateway Routing Architecture
- 2. Failover & Routing Policies
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - When a provider returns `429 Too Many Requests` or `RESOURCE_EXHAUSTED`, mark that provider's circuit as `OPEN` for the duration specified in the `Retry-After` header.
2. - Standardize request/response payloads to the OpenAI-compatible or Anthropic Messages schema so client harnesses require zero code changes when switching models.

## Files inside the skill

- (SKILL.md only)
