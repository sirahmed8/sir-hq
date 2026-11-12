import os
import sys
import json
import re
import subprocess

CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0

ROOT = 'D:/Projects'
sys.path.insert(0, 'D:/Projects/_SIR/plans')
from products import PRODUCTS

dash_path = 'D:/Projects/_SIR/ops/dashboard.html'
with open(dash_path, 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const D = (\{.*?\});\nconst \$ =', text, re.DOTALL)
if not m:
    print('Failed to extract D from dashboard.html')
    sys.exit(1)

dash_data = json.loads(m.group(1))
dash_projects = {p['slug']: p for p in dash_data.get('projects', [])}

print(f"{'SLUG':<28} | {'DASH T/D':<10} | {'RAW DISK T/D':<14} | {'PARSED T/D':<12} | {'COMMIT (DASH vs DISK)':<25} | {'SYNC STATUS':<15}")
print("-" * 115)

discrepancies = []

for p in PRODUCTS:
    slug = p['slug']
    folder = os.path.join(ROOT, p['folder'])
    tasks_file = os.path.join(folder, '.sir', 'TASKS.md')
    if not os.path.exists(tasks_file):
        continue

    dash_p = dash_projects.get(slug, {})
    dash_total = dash_p.get('total', 0)
    dash_done = dash_p.get('done', 0)
    dash_commit = dash_p.get('commit', '')
    dash_sync = dash_p.get('sync', '')

    # Raw disk task count: count all checkboxes
    raw_total = 0
    raw_done = 0
    with open(tasks_file, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            chk = re.match(r'^\s*-\s*\[([ xX])\]', line)
            if chk:
                raw_total += 1
                if chk.group(1).lower() == 'x':
                    raw_done += 1

    # Parsed tasks as done by generate_dashboard
    parsed_total = 0
    parsed_done = 0
    cur_m = None
    with open(tasks_file, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            if re.match(r"## (M\d) (.*)", line):
                cur_m = True
            elif cur_m and (m2 := re.match(r"- \[([ x])\] (T-\d+) \| owner: [^|]+\| (.*)", line)):
                parsed_total += 1
                if m2.group(1) == 'x':
                    parsed_done += 1

    # Git details
    is_private = slug == 'ahome'
    disk_commit = ""
    disk_hash = ""
    disk_sync = ""
    if not is_private and os.path.exists(os.path.join(folder, '.git')):
        try:
            disk_commit = subprocess.run(['git', '-C', folder, 'log', '-1', '--format=%cs'], capture_output=True, text=True, timeout=5, creationflags=CREATE_NO_WINDOW).stdout.strip()
            disk_hash = subprocess.run(['git', '-C', folder, 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True, timeout=5, creationflags=CREATE_NO_WINDOW).stdout.strip()
            status_sb = subprocess.run(['git', '-C', folder, 'status', '-sb'], capture_output=True, text=True, timeout=5, creationflags=CREATE_NO_WINDOW).stdout.strip()
            first_line = status_sb.split('\n')[0] if status_sb else ''
            if 'ahead' in first_line or 'behind' in first_line:
                disk_sync = 'not in sync'
            else:
                disk_sync = 'in sync'
            # Also check for dirty worktree
            lines = [l for l in status_sb.split('\n') if l.strip()]
            dirty = len(lines) > 1
            if dirty:
                disk_sync += f" (dirty: {len(lines)-1} files)"
        except Exception as e:
            disk_sync = f"err: {e}"

    commit_match = (dash_commit == disk_commit) if not is_private else True
    sync_match = (dash_sync == disk_sync.split()[0] if disk_sync else True) if not is_private else True
    task_match = (dash_total == parsed_total) and (dash_done == parsed_done)
    raw_match = (parsed_total == raw_total) and (parsed_done == raw_done)

    status_str = f"{dash_total}/{dash_done}"
    raw_str = f"{raw_total}/{raw_done}"
    parsed_str = f"{parsed_total}/{parsed_done}"
    commit_str = f"{dash_commit} vs {disk_commit}" if not is_private else "withheld (private)"
    sync_str = f"{dash_sync} | {disk_sync}" if not is_private else "withheld (private)"

    print(f"{slug:<28} | {status_str:<10} | {raw_str:<14} | {parsed_str:<12} | {commit_str:<25} | {sync_str:<15}")

    if not task_match:
        discrepancies.append(f"{slug}: Dashboard tasks ({dash_total}/{dash_done}) != Parsed tasks ({parsed_total}/{parsed_done})")
    if not raw_match:
        discrepancies.append(f"{slug}: Parsed tasks ({parsed_total}/{parsed_done}) != Raw regex tasks ({raw_total}/{raw_done})")
    if not commit_match:
        discrepancies.append(f"{slug}: Dashboard commit date ({dash_commit}) != Git disk commit date ({disk_commit})")
    if not sync_match and not is_private:
        discrepancies.append(f"{slug}: Dashboard sync ({dash_sync}) != Git disk sync ({disk_sync})")

print("\nDiscrepancies found:")
for d in discrepancies:
    print(f"  - {d}")
