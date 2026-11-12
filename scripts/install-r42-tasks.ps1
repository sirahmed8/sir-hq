# Registers the r42 free-agent team as Windows background tasks (independent of any chat).
# Round times are :00 and :30 only (OWNER_DEFAULTS 12). Each round pauses while a game runs and runs at
# below-normal priority (handled inside scripts/r42_rounds.py).
# Run: powershell -ExecutionPolicy Bypass -File D:\Projects\_SIR\scripts\install-r42-tasks.ps1
$ErrorActionPreference = "Stop"
$py = "C:\Users\a7med\AppData\Local\Python\pythoncore-3.14-64\pythonw.exe"
if (-not (Test-Path $py)) { $py = (Get-Command pythonw.exe).Source }
$root = "D:\Projects\_SIR"
$script = Join-Path $root "scripts\r42_rounds.py"

$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries `
  -StartWhenAvailable -RestartCount 3 -RestartInterval (New-TimeSpan -Minutes 5) `
  -ExecutionTimeLimit (New-TimeSpan -Hours 2) -MultipleInstances IgnoreNew

# name, job, first run, repeat interval (0 = once a day)
$tasks = @(
  @{ n = "SIR_HQ_Verifier";     job = "verifier";     at = "00:30"; every = 2 },
  @{ n = "SIR_HQ_Scouts";       job = "scouts";       at = "04:00"; every = 0 },
  @{ n = "SIR_HQ_Review";       job = "review";       at = "00:00"; every = 2 },
  @{ n = "SIR_HQ_NotifyFails";  job = "notify-fails"; at = "00:45"; every = 2 },
  @{ n = "SIR_HQ_NotifyDaily";  job = "notify-daily"; at = "21:00"; every = 0 }
)

foreach ($t in $tasks) {
  $existing = Get-ScheduledTask -TaskName $t.n -ErrorAction SilentlyContinue
  if ($existing) { Unregister-ScheduledTask -TaskName $t.n -Confirm:$false }
  $action = New-ScheduledTaskAction -Execute $py -Argument "`"$script`" $($t.job)" -WorkingDirectory $root
  if ($t.every -gt 0) {
    $trigger = New-ScheduledTaskTrigger -Once -At $t.at `
      -RepetitionInterval (New-TimeSpan -Hours $t.every) -RepetitionDuration (New-TimeSpan -Days 3650)
  } else {
    $trigger = New-ScheduledTaskTrigger -Daily -At $t.at
  }
  Register-ScheduledTask -TaskName $t.n -Action $action -Trigger $trigger -Settings $settings `
    -Description "SIR r42 free-agent team: $($t.job) (verifier, scouts, review, notifications)" | Out-Null
  Write-Host "registered $($t.n) at $($t.at) every $($t.every)h"
}

Get-ScheduledTask | Where-Object { $_.TaskName -like "SIR_HQ_*" } |
  Select-Object TaskName, State | Format-Table -AutoSize | Out-String -Width 120
