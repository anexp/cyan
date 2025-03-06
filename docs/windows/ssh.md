# SSH

Ref :
1. [IT bros Windows](https://theitbros.com/ssh-into-windows/)

Install OpenSSH server
```ps1
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
```

or DISM (untested)
```ps1
dism /Online /Add-Capability /CapabilityName:OpenSSH.Server~~~~0.0.1.0
```

Check if OpenSSH server is installed
```ps1
Get-WindowsCapability -Online | ? Name -like 'OpenSSH.Server*'
```

Uninstall OpenSSH server
```ps1
Remove-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
```

Check the status of ssh-agent and sshd services using the PowerShell Get-Service command:
```ps1
Get-Service -Name *ssh*
```
ssh into windows computer

By default, both services are stopped and not added to the automatic startup. Run the following commands to start OpenSSH services and configure autostart for them:
```ps1
Start-Service sshd

Set-Service -Name sshd -StartupType 'Automatic'

Start-Service ssh-agent

Set-Service -Name ssh-agent -StartupType 'Automatic'
```

###  Use powershell as default shell on ssh login

- https://superuser.com/questions/1799896/how-to-configure-powershell-for-openssh-instead-of-cmd
- https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_server_configuration#configuring-the-default-shell-for-openssh-in-windows

First enter powershell session using 
```ps1
poweshell.exe
```

Then,

```ps1
New-ItemProperty -Path "HKLM:\SOFTWARE\OpenSSH" `
                 -Name DefaultShell `
                 -Value "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" `
                 -PropertyType String `
                 -Force
```

### Public Key authentication

Edit `C:\ProgramData\ssh\sshd_config`
as mentioned in [youtube video](https://www.youtube.com/watch?v=9dhQIa8fAXU)

Enable public authentication by adding
```
PubkeyAuthentication yes
```

Disable password authentication by adding
```
PasswordAuthentication no
```


Comment out the following lines as they cause problems in Windows 10/11 servers
```
# Match Group administrators
       # AuthorizedKeysFile __PROGRAMDATA__/ssh/administrators_authorized_keys
```

Copy your public keys to 
`$Env:USERPROFILE\.ssh/authorized_keys`


Restart the ssh server service
```ps1
Restart-Service sshd
```

