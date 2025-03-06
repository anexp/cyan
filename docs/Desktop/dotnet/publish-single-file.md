### Publishing a self-contained single-file .NET 5 executable
May 29, 2021

Assuming you want to target Windows:
```sh
dotnet publish -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true -p:IncludeNativeLibrariesForSelfExtract=true
```

And if you want to reduce the size (taking advantage of trimming):
```sh
dotnet publish -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true -p:IncludeNativeLibrariesForSelfExtract=true -p:PublishTrimmed=True -p:TrimMode=Link
```

If you'd like some background and an explanation of those options then read on.
Background and Motivation

I build a small benchmarking tool (SQLDriver), and after updating to .NET 5 recently I realized that anyone using it may need to install an updated runtime. I'd previously made an effort to keep the executable as easy to download and use as possible (using ILMerge to bundle dependent assemblies into the executable), so wondered how easy things were with .NET 5?
Self-Contained

A self-contained .NET application is one that doesn't rely on there being any shared components on the target machine (such as the .NET runtime). This feature has actually been around for several years, and the only downside is that it can end up publishing a lot of additional files along with the app (which also means a simple console app can be 60MB+).

Getting this to work requires a single flag:
```sh
dotnet publish -c Release -r win-x64 --self-contained true
```
Read more on the Microsoft docs site: Self-contained publishing.
Single-File

Rather than dozens (or hundreds) of files, this option publishes only a handful of files, with the rest being unzipped into memory when the app is launched:
```sh
dotnet publish -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true
```
The reason there isn't a single file (which is what you might expect!) is that only managed DLLs are bundled into the executable, and the native binaries (part of the .NET runtime) are left as separate files. You can have the native binaries bundled by specifying the following:
```sh
dotnet publish -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true -p:IncludeNativeLibrariesForSelfExtract=true
```

In .NET Core 3.x the PublishSingleFile option also bundled native binaries. The IncludeNativeLibrariesForSelfExtract option is new with .NET 5, where the default is to not bundle the native binaries.

Read more on the Microsoft docs site: Single-file deployment and executable.
Trimming

The final step for me was to enable trimming. Available only for self-contained apps, this feature allows bundling of only the assemblies that are used (rather than the entire .NET runtime):
```sh
dotnet publish -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true -p:IncludeNativeLibrariesForSelfExtract=true -p:PublishTrimmed=True
```
We can go one step further and remove unused code from assemblies (rather than whole assemblies only):
```sh
dotnet publish -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true -p:IncludeNativeLibrariesForSelfExtract=true -p:PublishTrimmed=True -p:TrimMode=link
```
The downside to trimming (including the more aggressive link option) is that there are certain scenarios where the build-time analysis may incorrectly identify code as unused, which will result in a runtime error. The docs call out components that can cause trimming problems - and in my case the application was very simple and also very easy to test for correctness.

Read more on the Microsoft docs site: Trim self-contained deployments and executables.
Conclusion

As a result of the self-contained, single-file, and trimming options I was able to get SQLDriver down to a single ~18MB executable that doesn't require anything to be installed on the target machine.


Reference :-
1. https://tjaddison.com/blog/2021/05/publishing-a-self-contained-single-file-net-5-executable/
