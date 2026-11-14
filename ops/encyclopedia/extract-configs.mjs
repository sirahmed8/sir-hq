// Extract MCP server / plugin NAMES only (no secrets) per tool into mcp-inventory.json
import fs from 'node:fs';
import path from 'node:path';

const HOME = 'C:/Users/a7med';
const APPDATA = process.env.APPDATA || `${HOME}/AppData/Roaming`;
const out = {};

function readJson(p) { try { return JSON.parse(fs.readFileSync(p, 'utf8')); } catch { return null; } }
function readJsonc(p) {
  try {
    const raw = fs.readFileSync(p, 'utf8');
    // Strip // and /* */ comments only outside strings
    let stripped = '';
    let inStr = false, quote = '', esc = false;
    for (let i = 0; i < raw.length; i++) {
      const c = raw[i], n = raw[i + 1];
      if (inStr) {
        stripped += c;
        if (esc) { esc = false; }
        else if (c === '\\') { esc = true; }
        else if (c === quote) { inStr = false; }
      } else {
        if (c === '"' || c === "'") { inStr = true; quote = c; stripped += c; }
        else if (c === '/' && n === '/') { while (i < raw.length && raw[i] !== '\n') i++; stripped += '\n'; }
        else if (c === '/' && n === '*') { i += 2; while (i < raw.length && !(raw[i] === '*' && raw[i + 1] === '/')) i++; i++; }
        else { stripped += c; }
      }
    }
    stripped = stripped.replace(/,(\s*[}\]])/g, '$1');
    return JSON.parse(stripped);
  } catch (e) { return { __parseError: String(e).slice(0, 120) }; }
}

// Claude: top-level mcpServers + per-project mcpServers names + plugins
{
  const j = readJson(`${HOME}/.claude.json`);
  const names = new Set();
  if (j && j.mcpServers) Object.keys(j.mcpServers).forEach(k => names.add(k));
  if (j && j.projects) for (const [proj, pv] of Object.entries(j.projects)) {
    if (pv && pv.mcpServers) Object.keys(pv.mcpServers).forEach(k => names.add(`${k} (project:${proj})`));
  }
  out.claude = { mcpServers: [...names].sort() };
  const plugins = readJson(`${HOME}/.claude/plugins/installed_plugins.json`);
  if (plugins) {
    const list = plugins.plugins && typeof plugins.plugins === 'object' && !Array.isArray(plugins.plugins)
      ? Object.keys(plugins.plugins)
      : [];
    out.claude.plugins = [...new Set(list)].sort();
  }
}

// Codex: ~/.codex/config.toml mcp_servers.* & plugins.*
{
  try {
    const t = fs.readFileSync(`${HOME}/.codex/config.toml`, 'utf8');
    const mcpServers = [...new Set([...t.matchAll(/^\[mcp_servers\.([^.\]\r\n]+)\]/gm)].map(m => m[1]))].sort();
    const plugins = [...new Set([...t.matchAll(/^\[plugins\."?([^"\]\r\n]+)"?\]/gm)].map(m => m[1]))].sort();
    out.codex = { mcpServers, plugins };
  } catch { out.codex = { mcpServers: [], plugins: [] }; }
}

// opencode + kilo jsonc (mcp section names only, including nested mcp.servers.*)
for (const [tool, p] of [['opencode', `${HOME}/.config/opencode/opencode.jsonc`], ['kilo', `${HOME}/.config/kilo/kilo.jsonc`]]) {
  const j = readJsonc(p);
  const keys = [];
  if (j && j.mcp && typeof j.mcp === 'object') {
    for (const [k, v] of Object.entries(j.mcp)) {
      if (k === 'servers' && v && typeof v === 'object') {
        for (const sk of Object.keys(v)) keys.push(sk);
      } else {
        keys.push(k);
      }
    }
  }
  out[tool] = {
    mcpServers: [...new Set(keys)].sort(),
    instructions: Array.isArray(j?.instructions) ? j.instructions : [],
    parseError: j?.__parseError || null
  };
}

// gemini: settings.json + config/mcp_config.json + plugins.json + plugin.json files
{
  const names = new Set();
  const s = readJson(`${HOME}/.gemini/settings.json`);
  if (s && s.mcpServers) Object.keys(s.mcpServers).forEach(k => names.add(k));
  const mc = readJson(`${HOME}/.gemini/config/mcp_config.json`);
  if (mc) {
    if (mc.mcpServers) Object.keys(mc.mcpServers).forEach(k => names.add(k));
    if (mc.servers) Object.keys(mc.servers).forEach(k => names.add(k));
  }
  const pj = readJson(`${HOME}/.gemini/config/plugins.json`);
  if (pj) out.geminiPluginsJson = pj;
  const pluginsDir = `${HOME}/.gemini/config/plugins`;
  const plist = [];
  if (fs.existsSync(pluginsDir)) for (const d of fs.readdirSync(pluginsDir).sort()) {
    const pdir = path.join(pluginsDir, d);
    const pj2 = readJson(path.join(pdir, 'plugin.json'));
    const mcps = new Set();
    if (pj2 && pj2.mcpServers) {
      if (typeof pj2.mcpServers === 'string') {
        const mj = readJson(path.join(pdir, pj2.mcpServers));
        if (mj) Object.keys(mj.mcpServers || mj.servers || mj).forEach(k => mcps.add(k));
      } else if (typeof pj2.mcpServers === 'object') {
        Object.keys(pj2.mcpServers).forEach(k => mcps.add(k));
      }
    }
    for (const cand of ['.mcp.json', 'mcp_config.json', '.antigravity-plugin/mcp_config.json']) {
      const mj = readJson(path.join(pdir, cand));
      if (mj) Object.keys(mj.mcpServers || mj.servers || mj).forEach(k => mcps.add(k));
    }
    if (pj2 || mcps.size) {
      plist.push({
        plugin: d,
        name: pj2?.name || d,
        description: String(pj2?.description || '').slice(0, 160),
        mcpServers: [...mcps].sort()
      });
    }
  }
  out.gemini = { mcpServers: [...names].sort(), plugins: plist };
  for (const cand of [`${HOME}/.gemini/antigravity/mcp_config.json`, `${HOME}/.gemini/antigravity/config/mcp_config.json`]) {
    const j = readJson(cand);
    if (j) out.antigravityMcp = { file: cand, keys: Object.keys(j.mcpServers || j.servers || j).sort() };
  }
}

// devin
{
  const d = readJson(`${HOME}/AppData/Local/devin/cli/mcp/descriptions.json`);
  const dc = readJson(`${APPDATA}/devin/config.json`);
  const descEntries = d && typeof d === 'object'
    ? Object.entries(d).map(([id, v]) => ({ id: id.slice(0, 12), description: v?.description || '' }))
    : [];
  out.devin = {
    mcpDescriptions: descEntries,
    appDataMcpServers: dc && dc.mcpServers ? Object.keys(dc.mcpServers) : [],
    mcpNote: 'No custom user/project mcpServers configured; builtin skills (declarative-repo-setup, upload-secrets) + reads workspace .agents/skills and ~/.agents/skills'
  };
}

// cline
{
  const cands = [`${HOME}/.cline/data/settings/cline_mcp_settings.json`, `${APPDATA}/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`];
  const found = {};
  for (const c of cands) { const j = readJson(c); if (j) found[c] = j.mcpServers ? Object.keys(j.mcpServers) : Object.keys(j); }
  out.cline = { mcpSettings: found };
}

// kimi config.toml
{
  try {
    const t = fs.readFileSync(`${HOME}/.kimi-code/config.toml`, 'utf8');
    const names = [...t.matchAll(/^\[mcp_servers\.([\w-]+)\]/gm)].map(m => m[1]);
    const other = [...t.matchAll(/^\[([\w.-]+)\]/gm)].map(m => m[1]).filter(x => !x.startsWith('mcp_servers'));
    out.kimi = { mcpServers: names, sections: [...new Set(other)] };
  } catch { out.kimi = { error: 'unreadable' }; }
}

// windsurf/cursor
{
  const cands = {
    windsurf: [`${HOME}/.codeium/windsurf/mcp_config.json`, `${HOME}/.codeium/mcp_config.json`],
    cursor: [`${HOME}/.cursor/mcp.json`, `${HOME}/.cursor/settings.json`],
  };
  for (const [tool, files] of Object.entries(cands)) {
    const found = {};
    for (const f of files) { const j = readJson(f); if (j) found[f] = j.mcpServers ? Object.keys(j.mcpServers) : Object.keys(j); }
    out[tool] = { files: found };
  }
}

// goose
out.goose = { note: 'goose.exe installed via WinGet links; no ~/.config/goose or AppData config found' };

// workspace MCP configs
{
  const m1 = readJson('D:/Projects/.mcp.json');
  const m2 = readJson('D:/Projects/.agents/mcp_config.json');
  out.workspaceMcp = {
    'D:/Projects/.mcp.json': m1 && m1.mcpServers ? Object.keys(m1.mcpServers).sort() : [],
    'D:/Projects/.agents/mcp_config.json': m2 && m2.mcpServers ? Object.keys(m2.mcpServers).sort() : [],
    note: 'Retired AgentsRoom-* entries cleaned 2026-11-14'
  };
}

fs.writeFileSync('D:/Projects/_SIR/ops/encyclopedia/mcp-inventory.json', JSON.stringify(out, null, 1), 'utf8');
console.log('written mcp-inventory.json');
for (const [k, v] of Object.entries(out)) console.log(k, '=>', JSON.stringify(v).slice(0, 200));
