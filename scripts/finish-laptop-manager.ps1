$top = 'D:\Projects\Laptop manager'
$dst = 'D:\Projects\SIR Laptop Manager\legacy\Laptop manager'
# the one name that exists in both places: keep both, nothing overwritten
$a = "$top\.claude\worktrees\personal-os-charter\.git"
if (Test-Path $a) { Move-Item -LiteralPath $a -Destination "$dst\.claude\worktrees\personal-os-charter\.git.duplicate-from-merge"; 'kept the duplicate worktree pointer as .git.duplicate-from-merge' }
# remove only EMPTY leftover directories, deepest first (never recursive on anything with files)
Get-ChildItem $top -Recurse -Directory -Force -ErrorAction SilentlyContinue | Sort-Object { $_.FullName.Length } -Descending | ForEach-Object {
  if (-not (Get-ChildItem $_.FullName -Force -ErrorAction SilentlyContinue)) { Remove-Item $_.FullName -Force -ErrorAction SilentlyContinue }
}
'top-level Laptop manager now holds: ' + ((Get-ChildItem $top -Force -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Name) -join ', ')
'legacy has .git: ' + (Test-Path "$dst\.git") + ' ; entries: ' + @(Get-ChildItem $dst -Force).Count
