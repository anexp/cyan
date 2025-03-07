# Ufw

Enable systemd service ufw
```sh
sudo systemctl enable ufw
```

Status
```sh
sudo ufw status
# number each
sudo ufw status numbered
```

Enable (Do this after allowing ssh)
```sh
sudo ufw enable
```

Outgoint allow
```sh
sudo ufw default allow outgoing
```

Incoming deny
```sh
sudo ufw default deny incoming
```


Allow ssh, http, https or any port number for that matter

```sh
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https

# or fine grained
sudo ufw allow ssh/tcp
```

