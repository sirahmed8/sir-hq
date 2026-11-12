# system-design-architect

- Tool: `codex`
- Category: design
- Source: `C:\Users\a7med\.codex\skills\system-design-architect\SKILL.md`
- SKILL.md size: 2432 chars

## What it does

Large-scale system design patterns: distributed caching, rate limiters, message brokers, and high-scale backends.

## Structure (headings inside SKILL.md)

- System Design Architect (28 Production Scaling Blueprints)
- 1. Core System Scaling Pillars
- 2. Blueprint Architectural Index
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - Algorithms: Token Bucket (bursts allowed), Leaky Bucket (smooth outflow), Sliding Window Counter.

## Key rules (verbatim lines from SKILL.md)

1. 1. **Distributed Rate Limiter**:
2. - Algorithms: Token Bucket (bursts allowed), Leaky Bucket (smooth outflow), Sliding Window Counter.
3. - Redis atomic lua scripts for distributed consistency across multiple application instances.

## Files inside the skill

- (SKILL.md only)
