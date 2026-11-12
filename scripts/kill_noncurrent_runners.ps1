# Kill free-tool runners working on projects that are planning-only (owner 2026-11-12). Run from a file so it never matches itself.
$cur = 'sir-ai|sir-jobs|sir-study|sir-laptop-manager|sir-portfolio|r58-|r61-'
Get-CimInstance Win32_Process | Where-Object {
  $_.CommandLine -match 'Continue task r60-build-sir-[a-z-]+|cli-run2.sh r60-build-sir-[a-z-]+' -and
  $_.ProcessId -ne $PID -and $_.Name -ne 'powershell.exe'
} | ForEach-Object {
  $m = [regex]::Match($_.CommandLine, 'r60-build-(sir-[a-z-]+)').Groups[1].Value
  if ($m -and $m -notmatch '^(sir-ai|sir-jobs|sir-study|sir-laptop-manager|sir-portfolio)$') {
    taskkill /PID $_.ProcessId /T /F | Out-Null; "killed $($_.ProcessId) $m"
  }
}
