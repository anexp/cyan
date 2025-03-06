# Mount 

## Debian

```sh
sudo modprobe nbd
sudo qemu-nbd -c /dev/nbd0 /path_to/sample.qcow2
lsblk
sudo udisksctl mount -b /dev/nbd0p1
```



## Untested

### On ArchLinux



Yes, it is possible to mount a qcow2 file used by virt-manager as a file system on the host. Here are the general steps:

    Install the necessary packages:
        qemu-utils (for qemu-nbd command)
        libguestfs-tools (for guestmount command)

    Make sure the qemu-nbd kernel module is loaded:

sudo modprobe nbd

Export the qcow2 image from virt-manager:

    Open virt-manager and select the virtual machine whose qcow2 file you want to mount
    Click on "Show virtual hardware details"
    Select the disk and click on "Edit"
    Check the "Export disk image" option and select a location to save the image

Attach the qcow2 image to a network block device (nbd):

bash

sudo qemu-nbd -c /dev/nbd0 /path/to/qcow2/image

Verify that the nbd device is available:

lsblk

Mount the nbd device using guestmount:

bash

    sudo guestmount -a /dev/nbd0 -i /mnt/qcow2

Now, you should be able to access the qcow2 file system at /mnt/qcow2 on the host system. Remember to unmount the file system and disconnect the nbd device when you're done:

bash

sudo umount /mnt/qcow2
sudo qemu-nbd -d /dev/nbd0

User
i am on Arch what packages should i install
ChatGPT

On Arch Linux, you can install the necessary packages using pacman, the package manager for Arch Linux. Here are the commands to install the required packages:

sudo pacman -S qemu libguestfs

This will install the qemu-utils package (which includes the qemu-nbd command) and the libguestfs-tools package (which includes the guestmount command) on your Arch Linux system.

Once these packages are installed, you can follow the steps I provided earlier to mount a qcow2 file used by virt-manager as a file system on your host.

