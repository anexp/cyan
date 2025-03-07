# VNC 


Set VNC password
```sh
vncpasswd --service
```

```sh
sudo systemctl restart vncserver-x11-serviced
sudo systemctl reload vncserver-x11-serviced
```



Set up SSH tunnel to use VNC

```sh
 ssh -L 5900:localhost:5900 user@remoteip
```

## Rasbperrypi

uses proprietary realvnc by default
```sh
sudo systemctl status vncserver-x11-serviced
sudo systemctl disable --now vncserver-x11-serviced
```

## Tighvnc

```sh
sudo apt install tighvncserver
```

tighvncserver
tighvncpasswd  (to set the password)



## TigerVNC

Press <F8> for context menu
