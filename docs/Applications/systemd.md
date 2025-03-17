# Systemd

rclone-mount-ro@.service
```
# Credits: kabili207 - https://gist.github.com/kabili207/2cd2d637e5c7617411a666d8d7e97101

[Unit]
Description=rclone: Remote FUSE filesystem for cloud storage config %i
Documentation=man:rclone(1)
After=network-online.target
Wants=network-online.target 
AssertPathIsDirectory=%h/remote-mnt/%i

[Service]
Type=notify
ExecStart=/usr/bin/rclone mount --read-only %i: %h/remote-mnt/%i
ExecStop=/bin/fusermount -u %h/remote-mnt/%i

[Install]
WantedBy=default.target
```

rclone-mount@.service
```
# Credits: kabili207 - https://gist.github.com/kabili207/2cd2d637e5c7617411a666d8d7e97101

[Unit]
Description=rclone: Remote FUSE filesystem for cloud storage config %i
Documentation=man:rclone(1)
After=network-online.target
Wants=network-online.target 
AssertPathIsDirectory=%h/remote-mnt/%i

[Service]
Type=notify
ExecStart=/usr/bin/rclone mount %i: %h/remote-mnt/%i
ExecStop=/bin/fusermount -u %h/remote-mnt/%i

[Install]
WantedBy=default.target
```
