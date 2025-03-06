# Qemu-img


Kali image

Unzip
```
sudo pacman -S p7zip
7z x kali-linux-2023.1-qemu-amd64.7z
```

Create 
```
qemu-img create -f qcow2 MyDisk.qcow2 50G
```
Increase size of size of disc image
```
qemu-img resize MyDisk.qcow2 +5G
 ```
To shrink large disk image
```
qemu-img resize --shrink kali-linux-2023.1-qemu-amd64.qcow2 -10G

```
