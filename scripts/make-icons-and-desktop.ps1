<#
 Creates, for every product folder that already has a `.sir` directory:
   - a unique icon (monogram on the product colour): assets\brand\icon.png/.ico and folder.ico
   - desktop.ini so the folder shows that icon in Explorer (D:\Projects\<folder>)
   - scripts\dev-start.ps1/.vbs (hidden background `npm run dev`) and scripts\dev-stop.ps1/.vbs
   - a Desktop folder with the same icon and 3 shortcuts: open project, start dev, stop dev
 Colours and monograms: D:\Projects\_SIR\plans\brand.json . Re-run after adding a product. Safe to run repeatedly.
#>
$ErrorActionPreference = 'Stop'
$magick = 'C:\Program Files\ImageMagick-7.1.2-Q16-HDRI\magick.exe'
$font = 'C:/Windows/Fonts/segoeuib.ttf'
$brand = Get-Content 'D:\Projects\_SIR\plans\brand.json' -Raw -Encoding UTF8 | ConvertFrom-Json
$desktop = [Environment]::GetFolderPath('Desktop')
$sh = New-Object -ComObject WScript.Shell
$oldBox = Join-Path $desktop '_old shortcuts'
# One tidy hub on the Desktop (same layout as D:\Projects): Desktop\SIR Projects\<project>\{open, start dev, stop dev}
$hubDir = Join-Path $desktop 'SIR Projects'
New-Item -ItemType Directory -Force $hubDir | Out-Null
$hubIco = Join-Path $hubDir 'icon.ico'
& $magick -size 256x256 xc:none -fill '#0F172A' -draw 'roundrectangle 8,8 247,247 52,52' -font $font -pointsize 96 -fill white -gravity center -annotate +0+4 'SIR' -define icon:auto-resize=256,128,64,48,32,16 $hubIco
$hini = Join-Path $hubDir 'desktop.ini'
if (Test-Path $hini) { attrib -h -s $hini }
Set-Content $hini "[.ShellClassInfo]`r`nIconResource=$hubIco,0`r`n" -Encoding Unicode
attrib +h +s $hini; attrib +r $hubDir
# retire stale Desktop folders of projects that moved to old projects (reversible: moved, not deleted)
foreach ($n in 'SIR Restaurant','SIR Market','SIR Pharmacy','SIR Library','Hagoozat Elite','11Players','EGFootball5','Negm Furniture','Odysseus','Antigravity Agent Suite','Obour Academic Hub','SIR Optimizer','SIR Controller','SIR Content Creation Studio','SIR ModPack','SIR Mods for GTA V') {
  $d = Join-Path $desktop $n
  if ((Test-Path $d) -and -not (Test-Path (Join-Path $d '.sir-shortcuts'))) {
    New-Item -ItemType Directory -Force $oldBox | Out-Null
    Move-Item -LiteralPath $d -Destination (Join-Path $oldBox $n) -Force
    "moved stale Desktop folder: $n"
  }
}
foreach ($prop in $brand.PSObject.Properties) {
  $slug = $prop.Name; $b = $prop.Value
  $proj = "D:\Projects\$($b.folder)"
  if (-not (Test-Path "$proj\.sir")) { "skip (no new project folder yet): $($b.folder)"; continue }
  New-Item -ItemType Directory -Force "$proj\assets\brand","$proj\scripts" | Out-Null
  $png = "$proj\assets\brand\icon.png"; $ico = "$proj\assets\brand\icon.ico"
  $src = Join-Path $proj 'assets/brand/source.png'
  if (Test-Path $src) {
    # AI-generated logo from agy: round the corners and build the multi-size icon
    & $magick $src -resize 256x256 '(' -size 256x256 xc:none -fill white -draw 'roundrectangle 0,0 255,255 56,56' ')' -compose DstIn -composite $png
  } else {
    # temporary placeholder (monogram) until generate-icons-agy.ps1 has produced the real logo
    & $magick -size 256x256 xc:none -fill $b.color -draw 'roundrectangle 8,8 247,247 52,52' -font $font -pointsize 118 -fill white -gravity center -annotate +0+6 $b.mono $png
  }
  & $magick $png -define icon:auto-resize=256,128,64,48,32,16 $ico
  # function icons: the project icon with a green play badge (start) or a red stop badge (stop)
  $icoStart = Join-Path $proj 'assets\brand\icon-start.ico'; $icoStop = Join-Path $proj 'assets\brand\icon-stop.ico'
  & $magick $png '(' -size 256x256 xc:none -fill white -draw 'circle 192,192 192,250' -fill '#16A34A' -draw 'circle 192,192 192,242' -fill white -draw 'polygon 172,160 172,224 224,192' ')' -composite -define icon:auto-resize=256,128,64,48,32,16 $icoStart
  & $magick $png '(' -size 256x256 xc:none -fill white -draw 'circle 192,192 192,250' -fill '#DC2626' -draw 'circle 192,192 192,242' -fill white -draw 'roundrectangle 166,166 218,218 6,6' ')' -composite -define icon:auto-resize=256,128,64,48,32,16 $icoStop
  if (Test-Path "$proj\folder.ico") { attrib -r -s -h "$proj\folder.ico" }
  Copy-Item $ico "$proj\folder.ico" -Force
  # folder icon on D:
  $ini = "$proj\desktop.ini"
  if (Test-Path $ini) { attrib -h -s $ini }
  Set-Content $ini "[.ShellClassInfo]`r`nIconResource=folder.ico,0`r`n" -Encoding Unicode
  attrib +h +s $ini; attrib +s "$proj\folder.ico"; attrib +r $proj
  # background dev scripts
  $start = @'
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root
New-Item -ItemType Directory -Force "$root\.sir" | Out-Null
$log = "$root\.sir\dev.log"
if (-not (Test-Path "$root\package.json")) { "No package.json yet. Build the project first (see .sir/PLAN.md)." | Set-Content $log; exit 0 }
if (Test-Path "$root\.sir\dev.pid") { $old = Get-Content "$root\.sir\dev.pid" -ErrorAction SilentlyContinue; if ($old -and (Get-Process -Id $old -ErrorAction SilentlyContinue)) { "already running ($old)" | Set-Content $log; exit 0 } }
$p = Start-Process cmd.exe -ArgumentList '/c','npm run dev' -WorkingDirectory $root -WindowStyle Hidden -RedirectStandardOutput $log -RedirectStandardError "$root\.sir\dev.err.log" -PassThru
$p.Id | Set-Content "$root\.sir\dev.pid"
'@
  $stop = @'
$root = Split-Path -Parent $PSScriptRoot
$pidFile = "$root\.sir\dev.pid"
if (Test-Path $pidFile) { $id = Get-Content $pidFile; if ($id) { taskkill /PID $id /T /F | Out-Null }; Remove-Item $pidFile -Force }
# also stop node processes started from this folder
Get-CimInstance Win32_Process -Filter "Name='node.exe'" | Where-Object { $_.CommandLine -like "*$root*" } | ForEach-Object { taskkill /PID $_.ProcessId /T /F | Out-Null }
'@
  Set-Content "$proj\scripts\dev-start.ps1" $start -Encoding UTF8
  Set-Content "$proj\scripts\dev-stop.ps1" $stop -Encoding UTF8
  foreach ($k in 'start','stop') {
    Set-Content "$proj\scripts\dev-$k.vbs" ("CreateObject(""WScript.Shell"").Run ""powershell.exe -NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File """"$proj\scripts\dev-$k.ps1"""""", 0, False") -Encoding ASCII
  }
  # Desktop folder with the same icon and 3 shortcuts
  $loose = Join-Path $desktop $b.folder
  $dd = Join-Path $hubDir $b.folder
  if ((Test-Path (Join-Path $loose '.sir-shortcuts')) -and -not (Test-Path $dd)) { Move-Item -LiteralPath $loose -Destination $dd -Force }
  New-Item -ItemType Directory -Force $dd | Out-Null
  $marker = Join-Path $dd '.sir-shortcuts'
  if (-not (Test-Path $marker)) { New-Item -ItemType File $marker | Out-Null; attrib +h $marker }
  Copy-Item $ico (Join-Path $dd 'icon.ico') -Force
  $dini = Join-Path $dd 'desktop.ini'
  if (Test-Path $dini) { attrib -h -s $dini }
  Set-Content $dini "[.ShellClassInfo]`r`nIconResource=$dd\icon.ico,0`r`n" -Encoding Unicode
  attrib +h +s $dini; attrib +r $dd
  $links = @(
    @{name=$b.display;                    target='explorer.exe'; args="`"$proj`""; icon=$ico},
    @{name="Start $($b.display) dev";     target='wscript.exe';  args="`"$proj\scripts\dev-start.vbs`""; icon=$icoStart},
    @{name="Stop $($b.display) dev";      target='wscript.exe';  args="`"$proj\scripts\dev-stop.vbs`""; icon=$icoStop}
  )
  foreach ($l in $links) {
    $lnk = $sh.CreateShortcut((Join-Path $dd "$($l.name).lnk"))
    $lnk.TargetPath = $l.target; $lnk.Arguments = $l.args; $lnk.WorkingDirectory = $proj; $lnk.IconLocation = "$($l.icon),0"; $lnk.Save()
  }
  "ok: $($b.folder)  [$($b.mono) $($b.color)]"
}
# refresh the Explorer icon cache so the new icons show at once
try { & ie4uinit.exe -show } catch {}
