# Dualbooting Windows and Arch Linux


### Reference

Medium article by John Fajardoo
1. [Dual boot Arch Linux and Windows the right way](https://medium.com/swlh/dual-boot-arch-linux-and-windows-the-right-way-7f59969f7525)
2. [I installed Arch Linux now what](https://medium.com/@fajardocj/i-installed-arch-linux-now-what-b032ebe8be06)

Stop Windows from messing up the system clock
This is a subtle, but very annoying problem and can drive you insane if you don’t realize what’s going on. Let’s say you live in an area that has a time zone of GMT-4 and it’s 2PM in your local time. This means that in a GMT area it’s 6PM, so that’s a no brainer, right?

So you set the time to 2pm on your Linux partition and live happily ever after. Then you boot windows for two hours of gaming. It’s now 4PM. Time to get back to work, so you go to your Linux partition and it says it’s 12PM. How come?

The problem lies in the different ways both operating systems handle the computer’s clock time. In Linux, the system is configured to use the UTC standard -that is, to use GMT with no offset- and then apply the offset at the OS level, so your computer’s clock has to actually be set to 8PM so that Linux applies that -4 offset itself so it can correctly display 4PM.

Windows, on the other hand, assumes that the computer’s clock is using the local standard, so it will keep “correcting” the discrepancies.

You could use the local time on both, but the correct practice is to have the hardware clock running in UTC and have both operating systems apply their respective offsets.

I didn’t mention any of this in the last part, so let’s take care of this now. Boot into Arch and fire up a terminal window, then enter

```sh
sudo timedatectl set-local-rtc 0
```

Now reboot into Windows and
```ps1
REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation" /v RealTimeIsUniversal /t REG_DWORD /d 1 /f
```

Or,

click on start > run. Then type **regedit** and press enter. Now navigate the left pane tree until you reach this route:

**HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation**
Right click on TimeZoneInformation, click on **new > qword** and enter **RealTimeIsUniversal** as the name and **1** as the value. If Windows complains about the clock needing to resync, let it do it. That’s it, now your computer’s clock is on UTC and both Linux and Windows correctly apply their offsets.

https://askubuntu.com/questions/169376/clock-time-is-off-on-dual-boot

```ps1
sc config w32time start= disabled
```


