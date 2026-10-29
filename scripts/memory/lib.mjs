// Shared helpers for the SIR memory hooks. Plain Node.js 18+, no dependencies.
// Layout assumed: <workspace>/_SIR/scripts/memory/*.mjs, for example D:\Projects\_SIR\scripts\memory\.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

export const SIR_ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
export const WORKSPACE = path.dirname(SIR_ROOT);

// Hook input arrives as one JSON object on stdin.
export function readInput() {
  try {
    const raw = fs.readFileSync(0, 'utf8');
    return raw.trim() ? JSON.parse(raw) : {};
  } catch {
    return {};
  }
}

export function readText(file, max) {
  try {
    const text = fs.readFileSync(file, 'utf8');
    return max && text.length > max ? `${text.slice(0, max)}\n…(cut here; open the file for the rest)` : text;
  } catch {
    return null;
  }
}

export function mtime(file) {
  try {
    return fs.statSync(file).mtimeMs;
  } catch {
    return 0;
  }
}

export function isInside(child, parent) {
  const rel = path.relative(parent, child);
  return rel === '' || (!rel.startsWith('..') && !path.isAbsolute(rel));
}

// Which checkpoint does this session use? A project is any folder under the workspace
// that has .sir/CHECKPOINT.md; everything else under the workspace is the HQ session.
// Returns null outside the workspace, so the hooks stay silent there.
export function resolveContext(cwd) {
  const start = path.resolve(cwd || process.cwd());
  if (!isInside(start, WORKSPACE)) return null;
  for (let dir = start; isInside(dir, WORKSPACE); dir = path.dirname(dir)) {
    const checkpoint = path.join(dir, '.sir', 'CHECKPOINT.md');
    if (fs.existsSync(checkpoint)) {
      return {
        mode: 'project',
        name: path.basename(dir),
        checkpoint,
        stateDir: path.join(dir, '.sir', '.memory'),
        bridge: path.join(dir, '.sir', 'LAST_CONTEXT.md'),
      };
    }
    if (dir === WORKSPACE || path.dirname(dir) === dir) break;
  }
  const ops = path.join(SIR_ROOT, 'ops');
  return {
    mode: 'hq',
    name: 'HQ',
    checkpoint: path.join(ops, 'HQ_CHECKPOINT.md'),
    stateDir: ops,
    bridge: path.join(ops, 'LAST_CONTEXT.md'),
  };
}
