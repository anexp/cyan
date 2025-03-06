# gnome settings

get
```
gsettings get org.gnome.desktop.interface gtk-theme
gsettings get org.gnome.desktop.interface icon-theme
```

set 
```
gsettings set org.gnome.desktop.interface gtk-theme Adwaita-dark
gsettings set org.gnome.desktop.interface icon-theme Adwaita-dark
```

To set the title bar button order for the GNOME window manager (Mutter, Metacity)
```
gsettings set org.gnome.desktop.wm.preferences button-layout ':minimize,maximize,close'
```

Install Xorg
```
sudo pacman -S xorg
```
To check if you are running Wayland or Xorg
```
echo $XDG_SESSION_TYPE
```

A ridiculous but fun way to know if you are using Wayland on GNOME

Press Alt + F2, type 'r' and press enter
Normally, it restarts the Normally it restarts the GNOME shell.
But it won’t work in Wayland. It will display ‘restart is not available on Wayland’
