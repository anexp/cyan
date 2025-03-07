# Syncthing

Ref :-
1. [Archwiki syncthing](https://wiki.archlinux.org/title/Syncthing)

```sh
sudo apt install syncthing
```

Web GUI at http://localhost:8384

## Autostarting syncthing

### System service (on server)
Running Syncthing as a system service ensures that it is running at startup even if the user has no active session, it is intended to be used on a server
```sh
sudo systemctl enable --now syncthing@username
```

### User service: on login (for desktop)

Running Syncthing as a systemd user service ensures that Syncthing only starts after the user has logged into the system (e.g., via the graphical login screen, or ssh).
```sh
systemctl --user enable --now syncthing
```

Systemd service file is at
- `/usr/lib/systemd/user/syncthing.service`
- `/usr/lib/systemd/system/syncthing@.service`


### Syncthing discovery server
https://docs.syncthing.net/users/stdiscosrv.html

```sh
sudo apt install syncthing-discosrv
```

```sh
sudo systemctl enable --now syncthing-discosrv
```

Add the following line to  `/etc/default/syncthing-discosrv`
```
STDISCOSRV_OPTS="-http"
```



## Troubleshooting

### Folder Markers Missing Error

https://forum.syncthing.net/t/how-to-resolve-folder-marker-missing-error/18750


Just create .stfolder inside the shared folder

