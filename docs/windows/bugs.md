# Bugs

Powershell Invoke-WebRequest The request was aborted Could not create SSL/TLS secure channel

https://bobbyhadz.com/blog/powershell-the-request-was-aborted-could-not-create-ssl-tls

The PowerShell Invoke-WebRequest error "The request was aborted: Could not create SSL/TLS secure channel" occurs because PowerShell uses TLS 1.0 when connecting to websites by default but the site you are making a request to requires TLS 1.1 or TLS 1.2 or SSLv3.

To solve the error, use the SecurityProtocol property to specify that all protocols are supported.

```ps1
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls, [Net.SecurityProtocolType]::Tls11, [Net.SecurityProtocolType]::Tls12, [Net.SecurityProtocolType]::Ssl3
[Net.ServicePointManager]::SecurityProtocol = "Tls, Tls11, Tls12, Ssl3"
```


When you run the command you might get another error:

    "The response content cannot be parsed because the Internet Explorer engine is not available, or Internet Explorer's first-launch configuration is not complete. Specify the UseBasicParsing parameter and try again."

If you get the error rerun the command with the -UseBasicParsing parameter.
shell

```ps1
Invoke-WebRequest -Uri https://nasa.gov -UseBasicParsing
```




### Ps2exe


In wine

ps2exe binary is not in path
it is in
C:\users\username\temp as ps2exe.ps1


### Path in Wine

https://forum.winehq.org/viewtopic.php?t=19457

Using regedit.exe Edit
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment

or use  reg.exe command:
```ps1
reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path
```
to read the current path, and
```ps1
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path /d "newPath" /f
```

to write your new value.

You need admin rights for hsving right acccess in HKLM. If that is a problem, consider modifying the user specific path setting in HKCU\Environment instead.
