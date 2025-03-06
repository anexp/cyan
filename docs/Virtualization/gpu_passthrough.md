# NVIDIA GPU Passthrough 



In `/etc/default/grub`

Its a good practise to remove `quiet` to get verbose output during boot which can be useful during troubleshooting

On Debian
```
GRUB_CMDLINE_LINUX_DEFAULT="intel_iommu iommu=pt vfio-pci.ids=10de:25a0,10de:2291"
```

On Arch
```
GRUB_CMDLINE_LINUX_DEFAULT="loglevel=3 intel_iommu=on vfio-pci.ids=10de:25a0,10de:2291"
```
loglevel=3 is added just to get more verbose output during bootup it has no impact on iommu


Check Device IDs

```sh
# Get device ids
lspci -nn | grep NVIDIA

# For kernel modules
lspci -k 
```


Check if iommu is enabled
```sh
dmesg | grep -i -e DMAR -e IOMMU
```

On Debian, add to `/etc/modules`
On Arch, add to `/etc/modules-load.d/vfio.conf`
```
vfio
vfio_iommu_type1
vfio_pci
vfio_virqfd
```

Add to `/etc/modprobe.d/vfio.conf`
```
options vfio-pci ids=10de:25a0,10de:2291
softdep nvidia pre: vfio-pci
```

Add to `/etc/modprobe.d/blacklist.conf`
```
blacklist radeon
blacklist nouveau
blacklist nvidia
```

The following bash script should allow you to see how your various PCI devices are mapped to IOMMU groups.
If it does not return anything, you either have not enabled IOMMU support properly or your hardware does not support it. 
```bash
shopt -s nullglob
for g in $(find /sys/kernel/iommu_groups/* -maxdepth 0 -type d | sort -V); do
    echo "IOMMU Group ${g##*/}:"
    for d in $g/devices/*; do
        echo -e "\t$(lspci -nns ${d##*/})"
    done;
done;
```

Install Virtio Drivers from [fedorapeople website](https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/latest-virtio)
[Website](https://pve.proxmox.com/wiki/Windows_VirtIO_Drivers) Under subsection **Downloading Wizard in the VM** 
download **virtio-win-guest-tools.exe**

### Mouse not working
After NVIDIA drivers if windows cannot grab mouse, change display to virtio from QXL


Ref :-
1. [TechHut Proxmox GPU Passthrough](https://www.youtube.com/watch?v=S6jQx4AJlFw)
2. [Mental Outlaw GPU Passthrough](https://www.youtube.com/watch?v=KVDUs019IB8)
3. [ArchWiki PCI passthrough via OVMF](https://wiki.archlinux.org/title/PCI_passthrough_via_OVMF)
4. [Unix stackexchange](https://unix.stackexchange.com/questions/311445/pci-passthrough-vfio-pci-ignores-ids-of-devices#576665)



#### General

To build image (on Arch)
```sh
sudo mkinitcpio  linux linux-zen
```

Update grub
```sh
sudo grub-mkconfig -o /boot/grub/grub.cfg
```
