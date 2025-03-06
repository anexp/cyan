# Wix

Ref:-
1. [wixtoolset update](https://wixtoolset.org/docs/releasenotes/#update-the-wix-net-tool)
2. [Create first msi using wix](https://www.alexandrumarin.com/wix-tutorials-create-your-first-basic-msi/)
3. [Wix toolset preview by creater of wix](https://robmensching.com/blog/posts/2021/5/17/wix-toolset-v4-preview.0/)

## Installation

First. install dotnet framework

To install WiX for the first time as a .NET tool:
```ps1
dotnet tool install --global wix
```
To update your .NET tool installation of WiX v4:
```ps1
dotnet tool update --global wix
```
To verify Wix.exe was successfully installed or updated:
```ps1
wix --version
```

AdditionalTools
```ps1
winget install WixToolset.AdditionalTools
```

## Commands

```ps1
wix convert your.wxs
wix build your.wxs -o your.msi
```

New Guid
```ps1
New-Guid
```


Msiexec

install
```ps1
msiexec /i dojo.msi /l*v install.txt
```

uninstall
```ps1
msiexec /x dojo.msi /l*v uninstall.txt
```

### Heat

```
dotnet add package WixToolset.Heat --version 4.0.2
```
