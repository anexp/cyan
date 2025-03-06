# 

Ref :-
1. [ps1 to exe adamtheautomator](https://adamtheautomator.com/ps1-to-exe/)

Install

```ps1
Install-Module ps2exe
```

```ps1
## Use the full command name
Invoke-ps2exe .\source.ps1 .\target.exe

## Use the alias
ps2exe .\source.ps1 .\target.exe
```

Hiding console 

When running target.exe, a typical PowerShell console will appear. Most of the time, you don’t want to see this. To prevent that, you can use the NoConsole parameter when creating the EXE, as shown below.
```ps1
Invoke-ps2exe "D:\Test\Get-LatestAppLog.ps1" "D:\Test\Get-LatestAppLog.exe" -noConsole
```
