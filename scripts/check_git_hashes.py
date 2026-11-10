import os
import sys
import subprocess

CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0
import json
import re

sys.path.insert(0, 'D:/Projects/_SIR/plans')
from products import PRODUCTS

dash_path = 'D:/Projects/_SIR/ops/dashboard.html'
with open(dash_path, 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const D = (\{.*?\});\nconst \$ =', text, re.DOTALL)
dash_data = json.loads(m.group(1))
dash_projects = {p['slug']: p for p in dash_data.get('projects', [])}

print(f"{'SLUG':<28} | {'DASH COMMIT DATE':<18} | {'DISK DATE':<12} | {'DISK HASH':<10} | {'DISK SUBJECT':<40}")
print('-' * 115)
for p in PRODUCTS:
    slug = p['slug']
    folder = os.path.join('D:/Projects', p['folder'])
    dash_p = dash_projects.get(slug, {})
    dash_commit = dash_p.get('commit', '')
    if slug == 'ahome':
        print(f"{slug:<28} | {'withheld (private)':<18} | {'withheld':<12} | {'withheld':<10} | {'withheld (private)'}")
        continue
    if os.path.exists(os.path.join(folder, '.git')):
        log_out = subprocess.run(['git', '-C', folder, 'log', '-1', '--format=%cs|%h|%s'], capture_output=True, text=True, creationflags=CREATE_NO_WINDOW).stdout.strip()
        parts = log_out.split('|', 2)
        if len(parts) == 3:
            d_date, d_hash, d_subj = parts
            print(f"{slug:<28} | {dash_commit:<18} | {d_date:<12} | {d_hash:<10} | {d_subj[:40]:<40}")
