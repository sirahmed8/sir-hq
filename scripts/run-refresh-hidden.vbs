' Silent background launcher for SIR Control Room telemetry refresh
' Runs pythonw.exe completely hidden (SW_HIDE=0) without console windows or visual interruption
Option Explicit

Dim WshShell, fso, scriptDir, pyScript, cmd, pyw
Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

scriptDir = fso.GetParentFolderName(WScript.ScriptFullName)
pyScript = fso.BuildPath(scriptDir, "refresh-control-room.py")

If fso.FileExists("C:\msys64\ucrt64\bin\pythonw.exe") Then
    pyw = "C:\msys64\ucrt64\bin\pythonw.exe"
ElseIf fso.FileExists("C:\Users\a7med\AppData\Local\Python\pythoncore-3.14-64\pythonw.exe") Then
    pyw = "C:\Users\a7med\AppData\Local\Python\pythoncore-3.14-64\pythonw.exe"
Else
    pyw = "pythonw.exe"
End If

cmd = """" & pyw & """ """ & pyScript & """"

' Run with window style 0 (hidden) and do not block (bWaitOnReturn = False)
WshShell.Run cmd, 0, False
