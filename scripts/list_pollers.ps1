Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -match 'telegram|backup_manager|getUpdates|bot' -and $_.Name -match 'node|python' -and $_.CommandLine -notmatch 'list_pollers' } | ForEach-Object {
  "{0} {1} {2}" -f $_.ProcessId, $_.Name, $_.CommandLine.Substring(0,[Math]::Min(170,$_.CommandLine.Length))
}
