# Syncthing Server


### Syncthing discovery server
https://docs.syncthing.net/users/stdiscosrv.html

```sh
sudo apt install syncthing-discosrv
```

```sh
sudo systemctl enable --now syncthing-discosrv
```

Add the following line to  `/etc/default/syncthing-discosrv` [Not necessary]
```
STDISCOSRV_OPTS="-http"
```




