import subprocess
import sys

CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0
import json

repos = [
    ('AHome (private repo)', 'sirahmed8/ahmed-and-habiba'),
    ('SIR HQ', 'sirahmed8/sir-hq'),
    ('SIR Jobs', 'sirahmed8/sir-jobs'),
    ('SIR Study', 'sirahmed8/sir-study'),
    ('SIR Optimizer', 'sirahmed8/sir-optimizer'),
]

for name, r in repos:
    res = subprocess.run(['gh', 'run', 'list', '-R', r, '--limit', '2', '--json', 'databaseId,conclusion,status,headBranch,headSha,createdAt,name'], capture_output=True, text=True, creationflags=CREATE_NO_WINDOW)
    if res.returncode == 0:
        runs = json.loads(res.stdout)
        print(f'{name} ({r}):')
        for run in runs:
            db_id = run.get('databaseId')
            st = run.get('status')
            conc = run.get('conclusion')
            br = run.get('headBranch')
            sha = (run.get('headSha') or '')[:7]
            created = run.get('createdAt')
            print(f'   ID: {db_id} | Status: {st} | Conclusion: {conc} | Branch: {br} | Commit: {sha} | Date: {created}')
    else:
        print(f'{name} ({r}): ERROR: {res.stderr}')
