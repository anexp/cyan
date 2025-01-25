# Windows and Linux Dual Boot - Time mismatch

```powershell
# Set RealTimeIsUniversal to 1
New-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\TimeZoneInformation" -Name "RealTimeIsUniversal" -Value 1 -PropertyType DWord -Force

# Optional: Verify the value is set correctly
Get-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\TimeZoneInformation" -Name "RealTimeIsUniversal"

# To remove the value:
# Remove-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\TimeZoneInformation" -Name "RealTimeIsUniversal" -Force
```
