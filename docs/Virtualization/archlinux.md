# VIRTUALIZATION on ARCH LINUX

Ref :-
1. [Link to Tutorial](https://dev.to/rshalford/setting-up-virtual-machines-on-arch-linux-5gl3)



## In Short 


```sh

LC_ALL=C lscpu | grep Virtualization

sudo pacman -S --needed qemu libvirt virt-manager
sudo pacman -S --needed bridge-utils dnsmasq 
sudo pacman -S --needed dmidecode
# sudo pacman -S iptables-nft

sudo systemctl enable --now libvirtd
sudo systemctl status libvirtd
sudo usermod -a $USER -G libvirt

```

To check if libvirtd is missing anything
```sh
sudo systemctl status libvirtd
sudo systemctl restart libvirtd
```



## Explanation

 Setting up virtual machines on Arch Linux
#archlinux
#linux
#systems
#tutorial

Virtualisation is an incredibly useful tool, even for personal use. Personally, I use virtual machines for different purposes: testing out operating systems or Linux distributions without having to install them to bare metal; install my own software to test compatibility; try out the latest hyped about desktop environment or window manager. And as time goes on, I find more things to add to the list of uses.

    Whilst typing this up, I read about how I can use a virtual Debian install to install (not live load) a Debian distribution onto a USB drive. So I can carry around an operating system with persistent storage, and plug it into any PC.

Note: This article will be focussing on how to run virtual machines on Arch Linux.
KVM

Kernel-based Virtual Machine (KVM), is a hypervisor - an emulator or sorts - that comes baked into the Linux kernel. So if you run Linux, you will have this module included. And what this means to you the user is that you can quickly setup up your system for managing VMs.

But even if KVM is included in the Linux kernel installed on your computer, you first need to check whether your CPU has virtualisation support.
```sh
LC_ALL=C lscpu | grep Virtualization
```
Depending on which team you opted to support, the output will vary, but either output will confirm you support KVM.

AMD
```
Virtualization:                  AMD-V
```
Intel
```
Virtualization:                  VT-x
```
With the confirmation that virtualisation is supported, you will probably want to install some packages to make installing and managing VMs a lot more user friendly.
Virtualisation made easy
```sh
sudo pacman -S qemu libvirt iptables-nft dnsmasq virt-manager
```
    All the below installations in one.

QEMU

QEMU is an emulator and virtualiser that can use KVM for virtualisation, by using Hardware-assisted virtualisation with your CPU. But with the qemu package alone, you will not be able to use a GUI to manage your VMs, or make their sessions have persistent settings. Meaning that to make things run, you will need to use the command-line every time.
```sh
sudo pacman -S qemu
```
Libvirt

To overcome these hurdles, it is recommended to install libvirt, a meta-package that contains the tools for managing your VMs in a convenient way. To do this package justice in knowing what it provides, I'd recommend viewing it's Arch Wiki page.
```sh
sudo pacman -S libvirt
```
Libvirt daemon

Next you will need to enable and start the libvirt daemon. This will create some necessary symlinks and also enable the virtlogd.service.
```sh
sudo systemctl enable libvirtd
```
Created symlink /etc/systemd/system/multi-user.target.wants/libvirtd.service → /usr/lib/systemd/system/libvirtd.service.
Created symlink /etc/systemd/system/sockets.target.wants/virtlockd.socket → /usr/lib/systemd/system/virtlockd.socket.
Created symlink /etc/systemd/system/sockets.target.wants/virtlogd.socket → /usr/lib/systemd/system/virtlogd.socket.
Created symlink /etc/systemd/system/sockets.target.wants/libvirtd.socket → /usr/lib/systemd/system/libvirtd.socket.
Created symlink /etc/systemd/system/sockets.target.wants/libvirtd-ro.socket → /usr/lib/systemd/system/libvirtd-ro.socket.

Then just enable and start the service.
```sh
sudo systemctl enable --now libvirtd
```
Libvirt group

To allow non-sudo user access to the newly enabled libvirt daemon, you should now add the necessary users to the libvirt user group.
```sh
sudo usermod -aG libvirt $USER
```
Internet

You'll probably want to add internet connectivity to your future VM instances. Allowing you to browse the web or download and install software on another operating system.

Typically for personal use, you would want to create a virtual network that uses on the host system's network connectivity. This means installing two more packages. iptables-nft to replace iptables - that comes with a base install of Arch Linux - and dnsmasq, a DNS forwarder and DHCP server.
```sh
sudo pacman -S iptables-nft dnsmasq
```
Virtual Machine Manager

The GUI client I'd recommend using to manage your VMs is Virtual Machine Manager, or simply virt-manager. A brilliant bit of free software developed by Red Hat (they also help develop libvirt).

This program allows the user to; create, start, edit, pause and stop VMs. Whilst providing performance metrics for individual VMs.
```sh
sudo pacman -S virt-manager
```


