# Virtualization on Debian

Ref 
1. [Youtube Install KVM on Debian 11 server](https://www.youtube.com/watch?v=cUCHzAotkWk)

## Install

```sh
sudo apt install -y qemu-system libvirt-daemon-system virt-manager
```

Add the user to libvirt group
```sh
sudo systemctl enable --now libvirtd
sudo usermod -aG libvirt $USER
```

No need to add the user to libvirt-qemu group


### Windows VMs with qcow2

For Windows VMs, with already created qcow2 images
Use **manual install** not **local install media(iso/cdrom)**
because for local install media it would expect an iso file however we are giving it a qcow2 image
so use **manual install**
