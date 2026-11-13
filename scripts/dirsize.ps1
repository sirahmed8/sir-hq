param([string]$Root)
Get-ChildItem -LiteralPath $Root -Force -Directory -ErrorAction SilentlyContinue | ForEach-Object {
  $out = robocopy $_.FullName NUL /L /S /NJH /NJS /NDL /NC /NS /BYTES /R:0 /W:0 2>$null
  $sum = ($out | ForEach-Object { if ($_ -match '^\s*(\d+)\s') { [int64]$Matches[1] } } | Measure-Object -Sum).Sum
  [pscustomobject]@{ GB = [math]::Round($sum/1GB,2); Path = $_.FullName }
} | Sort-Object GB -Descending | Select-Object -First 8 | Format-Table -AutoSize | Out-String -Width 200
