# netlify-server

- Tool: `gemini-plugin` (plugin: `netlify`)
- Category: data
- Source: `C:\Users\a7med\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-server\SKILL.md`
- SKILL.md size: 18555 chars
- Identical content to: `encyclopedia/gemini-plugin/netlify--netlify-server.md`

Auto-generated stub: this SKILL.md is byte-identical to `encyclopedia/gemini-plugin/netlify--netlify-server.md`. Read that digest for full details.

Description: Build and deploy a long-lived Node.js backend on Netlify Server (Early Access) from netlify/server/index.ts. Use this skill whenever someone wants to run an Express, Fastify, Hono or Koa app on Netlify as it is, add a backend or REST/GraphQL API that keeps database pools and caches warm, build real-time features such as chat, live dashboards or multiplayer with WebSockets or Server-Sent Events, or stream AI responses and run agent loops. It also covers background work after responding with waitUntil, startup and graceful shutdown hooks, load-aware health checks, edge caching of server responses, region/size/scale settings, local testing with netlify dev, reading server logs with netlify logs or log drains, and debugging a server that gets no requests, fails to start, drops database connections after a minute, or returns 429/500/501/502.