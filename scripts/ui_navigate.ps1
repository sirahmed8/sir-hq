# Drive the VISIBLE Chrome window like a program (owner order 2026-11-12): put a URL into the address bar and press Enter.
# Usage: powershell -File ui_navigate.ps1 -Url "https://www.icloud.com/contacts"
param([string]$Url)
Add-Type -AssemblyName UIAutomationClient
Add-Type -AssemblyName UIAutomationTypes
Add-Type -AssemblyName System.Windows.Forms
$root = [System.Windows.Automation.AutomationElement]::RootElement
$wins = $root.FindAll([System.Windows.Automation.TreeScope]::Children, [System.Windows.Automation.Condition]::TrueCondition)
$target = $null
foreach ($w in $wins) { if ($w.Current.Name -like "*Google Chrome*" -and $w.Current.ClassName -eq "Chrome_WidgetWin_1") { $target = $w; break } }
if (-not $target) { Write-Output "chrome window not found"; exit 1 }
$all = $target.FindAll([System.Windows.Automation.TreeScope]::Descendants, [System.Windows.Automation.Condition]::TrueCondition)
$bar = $null
foreach ($e in $all) { if ($e.Current.ControlType.ProgrammaticName -match "Edit" -and $e.Current.Name -match "Address") { $bar = $e; break } }
if (-not $bar) { Write-Output "address bar not found"; exit 2 }
try { $target.SetFocus() } catch {}
Start-Sleep -Milliseconds 500
$bar.SetFocus()
Start-Sleep -Milliseconds 300
$bar.GetCurrentPattern([System.Windows.Automation.ValuePattern]::Pattern).SetValue($Url)
Start-Sleep -Milliseconds 300
[System.Windows.Forms.SendKeys]::SendWait("{ENTER}")
Write-Output "navigated"
