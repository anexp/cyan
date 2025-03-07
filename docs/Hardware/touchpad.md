# Touchpad

Archwiki (https://wiki.archlinux.org/title/Touchpad_Synaptics)

It works on Arch Linux KDE Xorg
with two extra packages **xf86-input-libinput** and **xf86-input-synaptics**

In my case, xf86-input-libinput was already installed

My touchpad's tap to click action was not working, but the pointer on screen was moving

I just had to install **xf86-input-synaptics** from standard Arch Repository and it started working

```sh
pacman -sS xf86-input-libinput
sudo pacman -S xf86-input-libinput
```

```sh
pacman -sS xf86-input-synaptics
sudo pacman -S xf86-input-synaptics
```

You can tweak touch pad options in KDE using **System Settings** 

On Debian 12

```sh
sudo apt install xserver-xorg-input-synaptics
```


Add to `/etc/X11/xorg.conf.d/70-synaptics.conf`
```
Section "InputClass"
    Identifier "touchpad"
    Driver "synaptics"
    MatchIsTouchpad "on"
        Option "TapButton1" "1"
        Option "TapButton2" "3"
        Option "TapButton3" "2"
        Option "VertEdgeScroll" "on"
        Option "VertTwoFingerScroll" "on"
        Option "HorizEdgeScroll" "on"
        Option "HorizTwoFingerScroll" "on"
        Option "CircularScrolling" "on"
        Option "CircScrollTrigger" "2"
        Option "EmulateTwoFingerMinZ" "40"
        Option "EmulateTwoFingerMinW" "8"
        Option "CoastingSpeed" "0"
        Option "FingerLow" "30"
        Option "FingerHigh" "50"
        Option "MaxTapTime" "125"
EndSection
```


