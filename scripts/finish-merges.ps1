<#
 FINISH THE REORGANIZATION (run once by Ahmed; agents are not allowed to stop running programs).
   pwsh -NoProfile -File D:\Projects\_SIR\scripts\finish-merges.ps1
 BEFORE: close Antigravity / VS Code / Cursor windows that have D:\Projects or one of its folders open (they lock folders so Windows cannot move them), and close Explorer windows inside D:\Projects.
 What it does: stops the old SIR AI app and SIR PowerSync (old projects may stop); moves SIR AI to its v1 name and creates the new SIR AI folder;
 moves AHome into SIR Home\legacy\AHome and repoints its daemons (stops and restarts them, verifies port 8090); merges Optimizer, Obour Academic Hub,
 Laptop manager, Jobs and sirahmed8 into their new products; rebuilds icons and Desktop shortcut folders.
#>
$ErrorActionPreference = 'Continue'
Set-Location 'D:\Projects'
Write-Output '== 1. stop old apps'
$keys = 'SIR Optimizer', 'D:\Projects\SIR AI'
Get-CimInstance Win32_Process | ForEach-Object {
  $t = "$($_.CommandLine) $($_.ExecutablePath)"
  if ($_.Name -notin 'bash.exe', 'powershell.exe', 'pwsh.exe' -and $_.ProcessId -ne $PID -and ($keys | Where-Object { $t.Contains($_) })) { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }
}
Start-Sleep -Seconds 2

Write-Output '== 2. SIR AI: old app becomes v1, new project folder is created'
if ((Test-Path 'D:\Projects\SIR AI') -and -not (Test-Path 'D:\Projects\SIR AI\.sir')) {
  try {
    Move-Item 'D:\Projects\SIR AI' 'D:\Projects\old projects\SIR AI (v1)' -ErrorAction Stop
    $env:PYTHONIOENCODING = 'utf-8'
    python 'D:\Projects\_SIR\plans\make_folders.py' | Out-Null
    'new SIR AI folder created'
  } catch { "SIR AI still locked: $($_.Exception.Message)" }
}

Write-Output '== 3. AHome -> SIR Home\legacy\AHome (daemons repointed)'
if (Test-Path 'D:\Projects\AHome') {
  $new = 'D:\Projects\SIR Home\legacy\AHome'
  $procs = Get-CimInstance Win32_Process -Filter "Name='python.exe'" | Where-Object { $_.CommandLine -like '*\AHome\*' }
  $procs | ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }
  Start-Sleep -Seconds 2
  New-Item -ItemType Directory -Force 'D:\Projects\SIR Home\legacy' | Out-Null
  try {
    Move-Item 'D:\Projects\AHome' $new -ErrorAction Stop
    foreach ($f in 'ahome-service-supervisor.ps1', 'jarvis_agy_bridge.py', 'launch_sanctuary_stack.vbs', 'launch_silent_core.vbs', 'register-startup-daemons.ps1') {
      $p = "$new\infra-daemons\$f"
      if (Test-Path $p) {
        $t = [IO.File]::ReadAllText($p)
        $n = $t.Replace('D:\Projects\AHome', $new).Replace('D:/Projects/AHome', 'D:/Projects/SIR Home/legacy/AHome')
        if ($n -ne $t) { [IO.File]::WriteAllText($p, $n, (New-Object Text.UTF8Encoding($false))) }
      }
    }
    $lnkPath = Join-Path $env:APPDATA 'Microsoft\Windows\Start Menu\Programs\Startup\OurSanctuary Daemon Stack.lnk'
    if (Test-Path $lnkPath) {
      $l = (New-Object -ComObject WScript.Shell).CreateShortcut($lnkPath)
      $l.Arguments = "`"$new\infra-daemons\launch_sanctuary_stack.vbs`""; $l.WorkingDirectory = "$new\infra-daemons"; $l.Save()
    }
    Start-Process wscript.exe -ArgumentList "`"$new\infra-daemons\launch_sanctuary_stack.vbs`"" -WindowStyle Hidden
    Start-Sleep -Seconds 25
    'port 8090 listening: ' + [bool](Get-NetTCPConnection -LocalPort 8090 -State Listen -ErrorAction SilentlyContinue)
  } catch {
    "AHome move failed ($($_.Exception.Message)); restarting from the old path"
    if (Test-Path 'D:\Projects\AHome\infra-daemons\launch_sanctuary_stack.vbs') { Start-Process wscript.exe -ArgumentList '"D:\Projects\AHome\infra-daemons\launch_sanctuary_stack.vbs"' -WindowStyle Hidden }
  }
}

Write-Output '== 4. merge the remaining old projects into their new products'
& 'D:\Projects\_SIR\scripts\merge-legacy.ps1'

Write-Output '== 5. icons and Desktop folders'
& 'D:\Projects\_SIR\scripts\make-icons-and-desktop.ps1'

Write-Output '== 6. what is still at the top level of D:\Projects'
(Get-ChildItem D:\Projects -Directory | Where-Object { $_.Name -notlike 'SIR *' -and $_.Name -notin 'old projects', '_SIR' } | Select-Object -ExpandProperty Name) -join '; '
