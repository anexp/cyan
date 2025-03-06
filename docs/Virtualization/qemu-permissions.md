# Qemu permissions

[Youtube link](https://invidious.snopyta.org/watch?v=jWySqo6u2l0)

Edit 
```
sudo nvim /etc/libvirt/qemu.conf
```


Add the following lines
```
user = "your_current_user"
group = "libvirt"
```

Then restart libvirtd daemon
```
sudo systemctl restart libvirtd
systemctl status libvirtd
``
