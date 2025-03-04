# GRUB

Main grub configuration file is `/etc/default/grub`

### Default Entry = Last Saved
```
GRUB_SAVEDEFAULT=true
GRUB_DEFAULT=saved
```
> Note :
> 1. Comment out entries such as **`GRUB_DEFAULT=0`** for this to take effect
> 2. This does not work if `/boot` partition is in btrfs or lvm filesystem

### Detect other bootable OSes

Activate os-prober
```
GRUB_DISABLE_OS_PROBER=false
```

### Console

For a TUI,
```
GRUB_TERMINAL=console
```

### Update grub.cfg

On Debian
```sh
sudo update-grub
```

On Arch/Fedora (Even Debian)
```sh
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

### Add custom entry

> Note :
> Place custom grub entries in **/etc/grub.d/** not in /etc/default/grub.d/

To add custom menus and submenus edit the file `/etc/grub.d/40_custom`

### Examples

#### Standard

```
# "Shutdown" menu entry
menuentry "System shutdown" {
	echo "System shutting down..."
	halt
}

# "Restart" menu entry
menuentry "System restart" {
	echo "System rebooting..."
	reboot
}

# "UEFI Firmware Settings" menu entry
if [ ${grub_platform} == "efi" ]; then
	menuentry 'UEFI Firmware Settings' --id 'uefi-firmware' {
		fwsetup
	}
fi
```

#### Chainloading a different EFI paritition

```
if [ "${grub_platform}" == "efi" ]; then
	menuentry "Debian on Different SSD" {
		savedefault
		insmod part_gpt
		insmod fat
		insmod chain
		search --no-floppy --fs-uuid --set=root AB12-CD34
		chainloader /EFI/debian/grubx64.efi
	}
fi
```

#### Windows grub entry

```
menuentry 'Windows Boot Manager (on /dev/nvme0n1p1)' --class windows --class os $menuentry_id_option 'osprober-efi-541A-B5FD' {
	savedefault
	insmod part_gpt
	insmod fat
	search --no-floppy --fs-uuid --set=root 541A-B5FD
	chainloader /EFI/Microsoft/Boot/bootmgfw.efi
}

```


### Nvidia

Video portion is not needed
just add `nvidia_drm.modeset=1`
```
GRUB_CMDLINE_LINUX_DEFAULT="quiet nvidia_drm.modeset=1 video=eDP-1:1920x1080 video=HDMI-1-0:1920x1080e"
```

