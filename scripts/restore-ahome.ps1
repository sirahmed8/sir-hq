<# AHome is the private project of Ahmed and Habiba: it keeps its own name and is NOT merged into a SIR product.
   Moves D:\Projects\SIR Home\legacy\AHome back to D:\Projects\AHome, repoints its daemons and restarts them, verifies port 8090. #>
$new = 'D:\Projects\AHome'
$old = 'D:\Projects\SIR Home\legacy\AHome'
if (-not (Test-Path $old)) { "nothing to move (AHome is already at $new): " + (Test-Path $new); exit 0 }
Get-CimInstance Win32_Process -Filter "Name='python.exe'" | Where-Object { $_.CommandLine -like '*\SIR Home\legacy\AHome\*' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }
Start-Sleep -Seconds 2
Move-Item -LiteralPath $old -Destination $new
foreach ($f in 'ahome-service-supervisor.ps1', 'jarvis_agy_bridge.py', 'launch_sanctuary_stack.vbs', 'launch_silent_core.vbs', 'register-startup-daemons.ps1') {
  $p = "$new\infra-daemons\$f"
  if (Test-Path $p) {
    $t = [IO.File]::ReadAllText($p)
    $n = $t.Replace($old, $new).Replace('D:/Projects/SIR Home/legacy/AHome', 'D:/Projects/AHome')
    if ($n -ne $t) { [IO.File]::WriteAllText($p, $n, (New-Object Text.UTF8Encoding($false))); "repointed $f" }
  }
}
$lnkPath = Join-Path $env:APPDATA 'Microsoft\Windows\Start Menu\Programs\Startup\OurSanctuary Daemon Stack.lnk'
if (Test-Path $lnkPath) {
  $l = (New-Object -ComObject WScript.Shell).CreateShortcut($lnkPath)
  $l.Arguments = "`"$new\infra-daemons\launch_sanctuary_stack.vbs`""; $l.WorkingDirectory = "$new\infra-daemons"; $l.Save(); 'startup shortcut repointed'
}
Start-Process wscript.exe -ArgumentList "`"$new\infra-daemons\launch_sanctuary_stack.vbs`"" -WindowStyle Hidden
Start-Sleep -Seconds 25
'port 8090 listening: ' + [bool](Get-NetTCPConnection -LocalPort 8090 -State Listen -ErrorAction SilentlyContinue)
foreach ($n in 'telegram_gateway_bot.py', 'firebase_bridge.py', 'web_push_delivery.py') {
  $up = Get-CimInstance Win32_Process -Filter "Name='python.exe'" | Where-Object { $_.CommandLine -like "*$n*" }
  "{0}: {1}" -f $n, $(if ($up) { 'running' } else { 'not running' })
}
'git status of AHome (should be clean): ' + @(git -C $new status --short).Count + ' changed files'
