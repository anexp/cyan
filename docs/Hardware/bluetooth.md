# Bluetooth

Install 
```
sudo  pacman -S bluez bluez-utils
```

Daemon 
```
systemctl status bluetooth
sudo systemctl enable --now bluetooth
```

Control
```
bluetoothctl
```

Scan
```
scan on
```

Connect
```
connect mac_address
```
