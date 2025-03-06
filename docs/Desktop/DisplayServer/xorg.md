# xorg

## Regenerate xorg config

If nvidia-xconfig messes up your /etc/X11/xorg.conf

First backup
```
sudo cp /etc/X11/xorg.conf /etc/X11/xorg.conf.bak
```

Regenerate using

```sh
# display :2 was used because there was no active display server there
sudo Xorg :2 -configure
sudo cp /root/xorg.conf.new /etc/X11/xorg.conf

```



## Cannot open two xorg sessions

[reddit suggession](https://www.reddit.com/r/klippers/comments/uly2j6/cannot_open_virtual_console_2_and_any_commands_to/)
[github gist](https://gist.github.com/alepez/6273dc5220c1c5ec5f3f126e739d58bf)

```sh
 sudo usermod -a -G tty pi
```
reboot

if it's still failing then
```sh
sudo $EDITOR /etc/X11/Xwrapper.config
```
add a new line with
```
needs_root_rights=yes
```


#### Alternate 2

```sh
sudo apt-get install xserver-xorg-legacy
```

Edit /etc/X11/Xwrapper.config

```
allowed_users=anybody
needs_root_rights=yes
```
