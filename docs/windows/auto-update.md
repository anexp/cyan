# Auto Update

# Disable
Right-Click on Start icon and Click on Run
Or Use Super + R to open up run window

Type "services.msc"

Select any application
and press w (this will narrow down the items to those starting with w)
Scroll down or press down arrow

Right-Click on Windows Update 

Set "Disabled", then Apply then Ok



# Permanent Disable

In Run window type "regedit"

Go to Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows

Right-Click on Windows => New => Key
New Key "WindowsUpdate"

Right-Click on "WindowsUpdate" => New => Key
New Key "AU"

Create new 32-bit DWORD "NoAutoUpdate" and set its value to 1

[YouTube video](https://www.youtube.com/watch?v=qFIdyzpNHBw)





