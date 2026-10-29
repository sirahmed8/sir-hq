<# MERGE step: physically moves each old project (code, .git, structure) into its new merged product as `legacy\<old name>`,
   so the AI that builds the new product sees every source in one place. At the end of a product (plan M6) the finished
   `legacy\*` folders move to D:\Projects\old projects\. Close apps/terminals/editors that use an old folder first.
   Re-run any time: it skips what is already in place and reports what is still locked. #>
$map = [ordered]@{
 'SIR Hagoozat'                 = @('Hagoozat Elite','11Players','EGFootball5')
 'SIR Business'                 = @('SIR Restaurant','SIR Market','SIR Pharmacy','SIR Library')
 'SIR Controller'               = @('SIR Controller (v1)','SIR Optimizer')
 'SIR Laptop Manager'           = @('antigravity-agent-suite')
 'SIR Obour Hub'                = @('Obour Academic Hub')
 'SIR Negm Furniture'           = @('Negm Furniture')
 'SIR Odysseus'                 = @('Odysseus app')
 'SIR Content Creation Studio'  = @('SIR Content Creation Studio (v1)')
 'SIR ModPack'                  = @('SIR ModPack (v1)')
 'SIR Mods for GTA V'           = @('SIR Mods for GTA V (v1)')
 'SIR AI'                       = @('SIR AI (v1)')
}
# where an old folder may currently be: old projects\<name>, or still at D:\Projects\<name> (deferred because it was in use)
$alias = @{ 'SIR Controller (v1)'='SIR Controller'; 'SIR Content Creation Studio (v1)'='SIR Content Creation Studio'; 'SIR ModPack (v1)'='SIR ModPack'; 'SIR Mods for GTA V (v1)'='SIR Mods for GTA V'; 'SIR AI (v1)'='SIR AI' }
foreach ($new in $map.Keys) {
  $root = "D:\Projects\$new"
  if (-not (Test-Path "$root\.sir")) { continue }
  New-Item -ItemType Directory -Force "$root\legacy" | Out-Null
  foreach ($old in $map[$new]) {
    $dst = "$root\legacy\$old"
    if (Test-Path $dst) {
      if ((Get-Item $dst -Force).LinkType) { cmd /c rmdir "`"$dst`"" | Out-Null } else { "have: $new\legacy\$old"; continue }
    }
    $src = $null
    foreach ($cand in "D:\Projects\old projects\$old", "D:\Projects\$($alias[$old])", "D:\Projects\$old") {
      if ((Test-Path $cand) -and $cand -ne $root -and -not (Test-Path "$cand\.sir")) { $src = $cand; break }
    }
    if (-not $src) { "not found (already merged elsewhere?): $old"; continue }
    try {
      Move-Item -LiteralPath $src -Destination $dst -ErrorAction Stop
      Remove-Item "$dst\RETIRED.md" -Force -ErrorAction SilentlyContinue
      "merged: $old -> $new\legacy"
    } catch { "LOCKED, close what uses it and re-run: $old ($($_.Exception.Message))" }
  }
  $names = Get-ChildItem "$root\legacy" -Directory -ErrorAction SilentlyContinue | ForEach-Object { "- ``$($_.Name)``" }
  Set-Content "$root\legacy\README.md" ("# legacy: the old projects this product replaces`n`nThis is a MERGE project. Each folder below is a complete old project (code, git history, structure, assets). Read the inventory in D:\Projects\_SIR\ops\inventory\ and the plan in ..\.sir\PLAN.md, then port everything of value into the new structure (apps/, packages/) with clean architecture and high quality code, fully configured, tested, deployed and pushed in production mode. Do not edit legacy code except to read it. When the plan's milestone M6 is complete, move each folder here to D:\Projects\old projects\ (a script step in M6).`n`n" + ($names -join "`n") + "`n") -Encoding UTF8
  $gi = "$root\.gitignore"; $have = if (Test-Path $gi) { Get-Content $gi } else { @() }
  foreach ($n in 'legacy/','desktop.ini','.sir/dev.*','_quarantine/') { if ($have -notcontains $n) { Add-Content $gi $n } }
}
