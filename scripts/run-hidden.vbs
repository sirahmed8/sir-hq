' Usage: wscript run-hidden.vbs "<command line>"  - starts a command with no window
Set sh = CreateObject("WScript.Shell")
sh.Run WScript.Arguments(0), 0, False
