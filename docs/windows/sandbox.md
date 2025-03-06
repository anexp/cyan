# Sandbox

Ref :-
1. [Learn microsoft](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview)

Installation

Ensure that your machine is using Windows 10 Pro or Enterprise, build version 18305 or Windows 11.

Enable virtualization on the machine.

If you're using a physical machine, make sure virtualization capabilities are enabled in the BIOS.

If you're using a virtual machine, you need to enable nested virtualization. If needed, also update the VM to support nested virtualization. Run the following PowerShell commands on the host:

```ps1
Set-VMProcessor -VMName <VMName> -ExposeVirtualizationExtensions $true
Update-VMVersion -VMName <VMName>
```

Use the search bar on the task bar and type Turn Windows Features on or off to access the Windows Optional Features tool. Select Windows Sandbox and then OK. Restart the computer if you're prompted.

If the Windows Sandbox option is unavailable, your computer doesn't meet the requirements to run Windows Sandbox. If you think this analysis is incorrect, review the prerequisite list and steps 1 and 2.

Note

To enable Sandbox using PowerShell, open PowerShell as Administrator and run the following command:
PowerShell

```ps1
Enable-WindowsOptionalFeature -FeatureName "Containers-DisposableClientVM" -All -Online

Locate and select Windows Sandbox on the Start menu to run it for the first time.

Note

Windows Sandbox does not adhere to the mouse settings of the host system, so if the host system is set to use a left-handed mouse, you must apply these settings in Windows Sandbox manually when Windows Sandbox starts. Alternatively, you can use a sandbox configuration file to run a logon command to swap the mouse setting. For an example, see Example 3.

