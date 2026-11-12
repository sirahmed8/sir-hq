# daemons

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\daemons\SKILL.md`
- SKILL.md size: 13594 chars

## What it does

Configure and deploy long.

## When to use (from skill text)

- | Run code on a schedule | Cron Jobs (`⤳ skill: vercel-functions`) | Time-based trigger |

## Structure (headings inside SKILL.md)

- Vercel Daemons
- What It Is
- When to Use Daemons
- Quick Start
- worker/Dockerfile
- Configuration Reference
- Lifecycle and Scaling
- Graceful Shutdown
- worker/worker.py
- Consuming Vercel Queues From a Daemon
- Environment Variables and OIDC
- Local Development
- Logs and Observability
- Build Output API
- Limits
- Common Pitfalls
- References
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **Production only during the beta.** Daemons run only for the production deployment. Preview deployments do not start daemons; test changes by running the image locally.
- - **Rollout**: when a deployment becomes production (deploy, promote, Instant Rollback, or a completed rolling release), Vercel starts the new instances and sends `SIGTERM` to the previous deployment's instances. For a short time both versions run at once, so both must be able to consume the same qu
- - **Image, command, and environment variables** belong to the deployment. Change them with a new production deployment.
- - **Scaling with `vercel.json`**: change `instances` and deploy to production. The map replaces the previous one; regions removed from it stop.

## Key rules (verbatim lines from SKILL.md)

1. - **Production only during the beta.** Daemons run only for the production deployment. Preview deployments do not start daemons; test changes by running the image locally.
2. - **Rollout**: when a deployment becomes production (deploy, promote, Instant Rollback, or a completed rolling release), Vercel starts the new instances and sends `SIGTERM` to the previous deployment's instances. For a short time both versions run at once, so both must be able to consume the same qu
3. 2. **Testing on a preview**: daemons never start for preview deployments during the beta. Deploy to production or run the image locally.
4. 5. **No SIGTERM handling**: the process is killed 30 seconds after `SIGTERM` (the default) unless `terminationGracePeriodSeconds` is raised. Make jobs idempotent and acknowledge only after completion.

## Files inside the skill

- (SKILL.md only)
