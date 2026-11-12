# Windows UI Automation helper: find a Chrome window by title part, then list or invoke elements by name. Used when a page needs a real click (native file picker).
# Usage: powershell -File ui_invoke.ps1 -Window "iCloud" -List            (lists clickable element names)
#        powershell -File ui_invoke.ps1 -Window "iCloud" -Click "Import vCard"
param([string]$Window, [string]$Click = "", [switch]$List)
Add-Type -AssemblyName UIAutomationClient
Add-Type -AssemblyName UIAutomationTypes
$root = [System.Windows.Automation.AutomationElement]::RootElement
$wins = $root.FindAll([System.Windows.Automation.TreeScope]::Children, [System.Windows.Automation.Condition]::TrueCondition)
$target = $null
foreach ($w in $wins) { if ($w.Current.Name -like "*$Window*" -and $w.Current.ClassName -eq "Chrome_WidgetWin_1") { $target = $w; break } }
if (-not $target) { Write-Output "window not found"; exit 1 }
$all = $target.FindAll([System.Windows.Automation.TreeScope]::Descendants, [System.Windows.Automation.Condition]::TrueCondition)
Write-Output ("elements: " + $all.Count)
if ($List) {
  $i = 0
  foreach ($e in $all) {
    $n = $e.Current.Name
    if ($n -and $e.Current.ControlType.ProgrammaticName -match "Button|MenuItem|Hyperlink|ListItem") {
      Write-Output ($e.Current.ControlType.ProgrammaticName.Replace("ControlType.", "") + " | " + $n.Substring(0, [Math]::Min(40, $n.Length)))
      $i++
      if ($i -ge 40) { break }
    }
  }
}
if ($Click) {
  foreach ($e in $all) {
    if ($e.Current.Name -eq $Click) {
      try { $e.GetCurrentPattern([System.Windows.Automation.InvokePattern]::Pattern).Invoke(); Write-Output "invoked"; exit 0 } catch { Write-Output ("invoke failed: " + $_.Exception.Message); exit 2 }
    }
  }
  Write-Output "element not found"
  exit 3
}
