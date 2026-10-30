<# Creates the new private SIR repos and pushes each project's first commit (plan, agent files, icons). Safe to re-run: skips repos that exist.
   Held back on purpose until they have code: ahome (private home data, repo already exists), sir-jobs and sir-study (personal data). #>
$hold = 'ahome'   # AHome is private and keeps its own repo; every other product gets a new private repo
$items = Get-Content 'D:\Projects\_SIR\plans\repos.json' -Raw -Encoding UTF8 | ConvertFrom-Json
foreach ($p in $items.PSObject.Properties) {
  $v = $p.Value; $dir = "D:\Projects\$($v.folder)"
  if ($hold -contains $p.Name) { "hold: $($v.repo)"; continue }
  if (-not (Test-Path "$dir\.sir")) { "skip (no folder): $($v.folder)"; continue }
  # a renamed old repo keeps answering to its old name (redirect), so compare the real name
  $real = gh repo view "sirahmed8/$($v.repo)" --json name -q .name 2>$null
  if ($LASTEXITCODE -eq 0 -and $real -ieq $v.repo) { "exists: $($v.repo)"; continue }
  if (-not (Test-Path "$dir\.git")) { git -C $dir init -q -b main }
  git -C $dir add -A
  git -C $dir commit -q -m "Initial project: plan, agent files, icon

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
  gh repo create "sirahmed8/$($v.repo)" --private --source $dir --remote origin --push --description "$($v.display)" 2>&1 | Select-Object -Last 1
}
