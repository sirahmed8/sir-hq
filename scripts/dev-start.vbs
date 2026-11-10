' Silent background launcher for SIR Control Room dashboard server daemon
' Runs pythonw.exe completely hidden (SW_HIDE=0) without console windows or visual interruption
' Checks for existing instance before launching to prevent duplicates
Option Explicit

Dim WshShell, fso, scriptDir, pyScript, cmd, pyw, lockFile, pid
Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

scriptDir = fso.GetParentFolderName(WScript.ScriptFullName)
pyScript = fso.BuildPath(scriptDir, "serve-control-room.py")
lockFile = fso.BuildPath(scriptDir, "..", "ops", "control-room.lock")

' Check if lock file exists and process is still alive
If fso.FileExists(lockFile) Then
    Dim ts, pidStr, proc
    Set ts = fso.OpenTextFile(lockFile, 1) ' ForReading
    pidStr = ts.ReadAll
    ts.Close
    If IsNumeric(pidStr) Then
        pid = CLng(pidStr)
        ' Try to get process - if it exists and is our script, don't launch
        On Error Resume Next
        Set proc = WshShell.Exec("tasklist /FI ""PID eq " & pid & """ /FI ""IMAGENAME eq pythonw.exe"" /FO CSV")
        Dim output
        output = proc.StdOut.ReadAll
        If InStr(output, "serve-control-room.py") > 0 Then
            WScript.Quit ' Another instance is running
        End If
        On Error GoTo 0
    End If
End If

If fso.FileExists("C:\msys64\ucrt64\bin\pythonw.exe") Then
    pyw = "C:\msys64\ucrt64\bin\pythonw.exe"
ElseIf fso.FileExists("C:\Users\a7med\AppData\Local\Python\pythoncore-3.14-64\pythonw.exe") Then
    pyw = "C:\Users\a7med\AppData\Local\Python\pythoncore-3.14-64\pythonw.exe"
ElseIf fso.FileExists("C:\Users\a7med\AppData\Local\Programs\Python\Python312\pythonw.exe") Then
    pyw = "C:\Users\a7med\AppData\Local\Programs\Python\Python312\pythonw.exe"
Else
    pyw = "pythonw.exe"
End If

cmd = """" & pyw & """ """ & pyScript & """"

' Run with window style 0 (hidden) and do not block (bWaitOnReturn = False)
WshShell.Run cmd, 0, False
