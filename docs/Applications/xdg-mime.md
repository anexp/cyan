# xdg-mime

Ref :- 
1. [Arch Wiki xdg-utils](https://wiki.archlinux.org/title/Xdg-utils)


Determine a file's MIME type:
Here, there must be an actual file named photo.jpeg to do this
```sh
xdg-mime query filetype photo.jpeg
```
output
```
image/jpeg
```


To check the current default program for opening MP4 files.
```
xdg-mime query default video/mp4
```

If you want to change the default program,
use the 
```sh
xdg-mime default <application.desktop> video/mp4 
```
command, where `<application.desktop>` is the desktop file for the program you want to use.
For example, to set VLC as the default program,
you can use the command 
```sh
xdg-mime default org.videolan.VLC.desktop video/mp4.
```

Note that the desktop file for the application you want to set as default should be located in the `/usr/share/applications/` directory.
```
cd /usr/share/applications
```
If the desktop file is located in a different directory,
you can specify the full path to the desktop file in the xdg-mime default command.


## Default browser

Get
```sh
xdg-settings get default-web-browser
```

Set
```sh
xdg-settings set default-web-browser io.gitlab.librewolf-community.desktop
```
