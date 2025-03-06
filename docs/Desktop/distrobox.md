# Distrobox

Ref:-
1. [Run GNOME session under distobox](https://github.com/89luca89/distrobox/blob/main/docs/posts/run_latest_gnome_kde_on_distrobox.md)

# Run full desktop session

```sh

sudo umount /run/systemd/system
sudo rmdir /run/systemd/system
sudo ln -s /run/host/run/systemd/system /run/systemd
sudo mkdir /run/dbus
sudo ln -s /run/host/run/dbus/system_bus_socket /run/dbus/

```


/etc/profile.d/fix_tmp.sh
```
chown -f -R $USER:$USER /tmp/.X11-unix
```

for KDE add to ~/.profile
```sh
if [ -f /usr/libexec/kactivitymanagerd ]; then
  /usr/libexec/kactivitymanagerd & disown
fi
```


With fedora dnf, pass the following pre init hook
```
echo 'fastestmirror=true' >> /etc/dnf/dnf.conf ; echo 'max_parallel_downloads=10' >> /etc/dnf/dnf.conf ;

```
