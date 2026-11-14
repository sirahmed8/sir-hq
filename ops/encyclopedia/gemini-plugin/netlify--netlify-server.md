# netlify-server

- Tool: `gemini-plugin` (plugin: `netlify`)
- Category: data
- Source: `C:\Users\a7med\.gemini\config\plugins\netlify\skills\netlify-server\SKILL.md`
- SKILL.md size: 18555 chars

## What it does

Build and deploy a long-lived Node.js backend on Netlify Server (Early Access) from netlify/server/index.ts. Use this skill whenever someone wants to run an Express, Fastify, Hono or Koa app on Netlify as it is, add a backend or REST/GraphQL API that keeps database pools and caches warm, build real-time features such as chat, live dashboards or multiplayer with WebSockets or Server-Sent Events, or stream AI responses and run agent loops. It also covers background work after responding with waitUntil, startup and graceful shutdown hooks, load-aware health checks, edge caching of server responses, region/size/scale settings, local testing with netlify dev, reading server logs with netlify logs or log drains, and debugging a server that gets no requests, fails to start, drops database connections after a minute, or returns 429/500/501/502.

## Structure (headings inside SKILL.md)

- Netlify Server
- Reach for this / avoid this
- Entry file and detection
- Examples
- Background work after responding
- WebSockets (handler/Fetchable)
- WebSockets (`ws` on a self-started server)
- Server-Sent Events / streaming
- Client reconnect
- Lifecycle hooks
- Edge caching
- Context (`context` arg or `getContext()`)
- Configuration
- Routing
- Instances and lifecycle
- Limits
- Errors
- Local dev and logs
- Netlify house rules (server)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - `cookies.get(name)` / `.set(options)` / `.delete(name|options)` follow CookieStore semantics.
- - A production deploy publishes only after its new server has started. If the server fails to start, the deploy isn't published and the old one keeps serving.
- - Local differences from production:
- - Use the **Server** page under **Cloud compute**. It opens in Live mode (last hour) and shows production by default, and you can switch branches to see branch deploys or Deploy Previews.

## Key rules (verbatim lines from SKILL.md)

1. - `onStart` must be called while the entry file loads. **Calling it later throws.**
2. - A health hook that throws never stops the instance. Health hooks don't run locally.
3. - **Environment variables:** use `process.env` with variables scoped to **Functions**. Values are fixed at deploy time, so **redeploy after changes**.
4. - Functions are cheaper for rarely used backends, because instances idle for 5 min before stopping.
5. - Once-only work can run twice or never. Use a scheduled function and record completion.

## Files inside the skill

- (SKILL.md only)
