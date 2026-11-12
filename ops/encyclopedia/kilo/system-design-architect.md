# system-design-architect (claude/codex/kilo/cursor/windsurf/opencode copies)

## Summary
system-design-architect is a SIR-authored architecture skill presenting "28 Production Scaling Blueprints" synthesized from enterprise-scale systems (the visible portion indexes five canonical patterns). It teaches the standard layered scaling architecture — GeoDNS/Anycast → edge CDN → L7 reverse proxy → distributed rate limiter → stateless auto-scaling app cluster → distributed cache → primary DB with read replicas/sharding → message broker → async workers — then details named blueprints: distributed rate limiting (token/leaky bucket/sliding window via Redis Lua), distributed caching (cache-aside/write-through/write-behind, LRU/LFU, stampede mutexes), real-time messaging (the "WhatsApp pattern": WebSocket gateways, Redis pub/sub presence, ACK + store-and-forward), video streaming (the "YouTube pattern": presigned chunked uploads, parallel FFmpeg-to-HLS workers, CDN edge caching) and geospatial routing (the "Google Maps pattern": S2/geohash/quadtrees, contraction hierarchies, A*/bidirectional Dijkstra). Caveat: the title advertises 28 blueprints but the document only expands 5; treat the remaining 23 as referenced-but-unwritten.

## When to use / when NOT
Use when designing or reviewing a large-scale system: choosing between rate-limit algorithms, cache strategies, message-broker topologies, streaming pipelines or geo-indexing. Do NOT use for small CRUD apps (over-engineering), for product/UI design, or as a substitute for reading current vendor docs on the specific technology chosen.

## Inputs, outputs, tools
- Inputs: the system's scale targets, traffic shape, consistency needs and existing stack.
- Outputs: an architecture recommendation: component diagram, algorithm/pattern choices with trade-offs, and capacity considerations.
- Tools: none executable; pure design knowledge. Pairs with database-reliability-transactions, modern-app-engineering and cloud skills for implementation.

## 5 most important rules
1. Start from the canonical layered diagram; justify each layer's necessity rather than adding components by default.
2. Rate limiting: pick the algorithm by traffic shape — token bucket for bursts, leaky bucket for smoothing, sliding window for accuracy; implement distributed state in Redis via atomic Lua.
3. Caching: choose the invalidation strategy explicitly (cache-aside vs write-through vs write-behind) and always plan for stampede protection.
4. Real-time systems need explicit delivery semantics: ACKs, presence via pub/sub, and offline store-and-forward queues.
5. Video at scale = presigned direct-to-cloud uploads + async parallel transcoding to HLS/DASH + edge CDN; never route media bytes through app servers.

## Risks / things needing the owner
Design patterns are only as good as the numbers behind them; the skill gives patterns, not capacity math — real sizing needs load estimates the owner may not have. Choosing managed services (Kafka, Spanner, Cloud CDN) has cost implications that touch the no-budget rule; flag costs before committing to a blueprint. Nothing else needs the owner.

## Category / tags
cloud · system-design, scalability, architecture, caching, messaging, streaming

## Revisions
Six copies exist (claude, codex, kilo, cursor, windsurf, opencode). They carry the same blueprint content with only frontmatter description wording differing. Best revision: the claude copy (used here); identical substance across all six.
