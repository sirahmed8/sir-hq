# netlify-access-control

- Tool: `gemini-plugin` (plugin: `netlify`)
- Category: security
- Source: `C:\Users\a7med\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-access-control\SKILL.md`
- SKILL.md size: 14578 chars
- Identical content to: `encyclopedia/gemini-plugin/netlify--netlify-access-control--copy2.md`

Auto-generated stub: this SKILL.md is byte-identical to `encyclopedia/gemini-plugin/netlify--netlify-access-control--copy2.md`. Read that digest for full details.

Description: Picks the right Netlify site-protection layer and disambiguates the three unrelated "auth" concepts users conflate — app-user login (Netlify Identity), site-load gating (Password Protection / project visibility), and dashboard SAML SSO. Use it when asked to password-protect a site or Deploy Preview, make a project private/public, restrict a site to your team, require SSO to view a site, set up company-wide or internal-app SSO, invite users to a private project, or know which team member made a request to a private site. Also use it for SSO-session symptoms on protected sites: "logged out mid-session", 401s after about an hour, or token expiry/refresh questions. Not for wiring auth code — route app-login setup to netlify-identity.