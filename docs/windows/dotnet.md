# dotnet

Ref:-
1. [Learn Microsoft install dotnet](https://learn.microsoft.com/en-us/dotnet/core/install/windows?tabs=net60)

```ps1
winget install Microsoft.DotNet.SDK.7
winget install Microsoft.DotNet.DesktopRuntime.7
# winget install Microsoft.DotNet.AspNetCore.7
winget install Microsoft.DotNet.Runtime.7
```

Add to path
```ps1
Add-EnvPath -Path 'C:\Program Files\dotnet\' -Container "User"
```
