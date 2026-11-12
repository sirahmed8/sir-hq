# Replace every contact in iCloud Contacts with a vCard file by driving the VISIBLE Chrome window like a program (owner order 2026-11-12).
# Needs the iCloud Contacts tab to be the active tab of the visible Chrome window (ui_navigate.ps1 does that).
# Usage: powershell -File icloud_replace.ps1 -File D:\Projects\_SIR\_local\contacts\final_apple.vcf -Expect 613
param([string]$File, [int]$Expect = 0)
Add-Type -AssemblyName UIAutomationClient
Add-Type -AssemblyName UIAutomationTypes
Add-Type -AssemblyName System.Windows.Forms
$UIA = [System.Windows.Automation.AutomationElement]

function Get-Chrome {
  $root = $UIA::RootElement
  $wins = $root.FindAll([System.Windows.Automation.TreeScope]::Children, [System.Windows.Automation.Condition]::TrueCondition)
  foreach ($w in $wins) { if ($w.Current.Name -like "iCloud Contacts*Google Chrome*" -and $w.Current.ClassName -eq "Chrome_WidgetWin_1") { return $w } }
  return $null
}
function Find-All($win, $name, $typeMatch) {
  $all = $win.FindAll([System.Windows.Automation.TreeScope]::Descendants, [System.Windows.Automation.Condition]::TrueCondition)
  $hits = @()
  foreach ($e in $all) { if ($e.Current.Name -eq $name -and ($typeMatch -eq "" -or $e.Current.ControlType.ProgrammaticName -match $typeMatch)) { $hits += $e } }
  return $hits
}
function Invoke-Named($name, $typeMatch = "", $last = $false) {
  $win = Get-Chrome
  if (-not $win) { throw "iCloud window not found" }
  $hits = Find-All $win $name $typeMatch
  if ($hits.Count -eq 0) { throw "not found: $name" }
  $e = if ($last) { $hits[$hits.Count - 1] } else { $hits[0] }
  $e.GetCurrentPattern([System.Windows.Automation.InvokePattern]::Pattern).Invoke()
}
function Contacts-Count {
  $win = Get-Chrome
  if (-not $win) { return -1 }
  $all = $win.FindAll([System.Windows.Automation.TreeScope]::Descendants, [System.Windows.Automation.Condition]::TrueCondition)
  foreach ($e in $all) { if ($e.Current.Name -match "^All Contacts\s+(\d+)$") { return [int]$Matches[1] } }
  return 0
}

$win = Get-Chrome
if (-not $win) { Write-Output "iCloud window not found"; exit 1 }
try { $win.SetFocus() } catch {}
Start-Sleep -Milliseconds 800
$before = Contacts-Count
Write-Output "before: $before"
if ($before -gt 0) {
  try { Invoke-Named "Select" "Button" } catch {}
  Start-Sleep -Milliseconds 1200
  $win = Get-Chrome
  $items = $win.FindAll([System.Windows.Automation.TreeScope]::Descendants, (New-Object System.Windows.Automation.PropertyCondition($UIA::ControlTypeProperty, [System.Windows.Automation.ControlType]::ListItem)))
  if ($items.Count -gt 1) { try { $items[1].SetFocus() } catch {}; Start-Sleep -Milliseconds 400; try { $items[1].GetCurrentPattern([System.Windows.Automation.SelectionItemPattern]::Pattern).Select() } catch { try { $items[1].GetCurrentPattern([System.Windows.Automation.InvokePattern]::Pattern).Invoke() } catch {} } }
  Start-Sleep -Milliseconds 800
  [System.Windows.Forms.SendKeys]::SendWait("^a")
  Start-Sleep -Milliseconds 1200
  Invoke-Named "More options" "Button"
  Start-Sleep -Milliseconds 1000
  Invoke-Named "Delete" "MenuItem|Button|ListItem"
  Start-Sleep -Milliseconds 1200
  Invoke-Named "Delete" "Button" $true
  Start-Sleep -Seconds 8
  Write-Output ("after delete: " + (Contacts-Count))
}
Invoke-Named "Add" "Button"
Start-Sleep -Milliseconds 1000
Invoke-Named "Import vCard" "MenuItem|Button|ListItem"
Start-Sleep -Seconds 3
[System.Windows.Forms.SendKeys]::SendWait($File)
Start-Sleep -Milliseconds 800
[System.Windows.Forms.SendKeys]::SendWait("{ENTER}")
Start-Sleep -Seconds 20
$after = Contacts-Count
Write-Output "after import: $after (expected $Expect)"
if ($Expect -gt 0 -and [math]::Abs($after - $Expect) -le 2) { Write-Output "OK" } else { Write-Output "CHECK" }
