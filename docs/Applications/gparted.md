# GParted

#### GParted not working on wayland

Error message
```
Gtk-WARNING **: cannot open display: :0
```

[Stack Overflow response](https://stackoverflow.com/questions/49280000/running-gparted-with-sudo-on-wayland)


You need **xhost**

Install using 
```
sudo pacman -S xorg-xhost
```

To check users which have permissions to display applications on desktop
```
xhost
```

Allow root to display application on desktop
```
xhost +SI:localuser:root
```
