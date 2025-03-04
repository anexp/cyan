# efibootmgr

List entries
```sh
efibootmgr -v
```

Create entry
```sh
# Not Verified
# efibootmgr -c  -d /dev/sda -p 1 -L LinuxMint -l /EFI/ubuntu/grubx64.efi


# Verified
# Recommended
sudo efibootmgr --create --disk=/dev/sda --part=4 --label="fedora_ssd" --loader='\EFI\fedora\shimx64.efi'
#
# This also works
sudo efibootmgr --create --disk=/dev/sda --part=4 --label="fedora_ssd2" --loader='EFI\fedora\shimx64.efi'
#
```


Windows
```sh
sudo efibootmgr --create --disk=/dev/nvme0n1 --part=1 --label="windows_test" --loader='\EFI\Microsoft\Boot\bootmgfw.efi'
```
for windows path can also be `\EFI\Boot\BootX64.efi`

Both seem to work fine
'part' should specify the partition number of the EFI parition (FAT32) vfat filesystem

Delete entry
```sh
sudo efibootmgr -B -b boot_number_to_be_deleted
```
or
```sh
sudo efibootmgr --delete-bootnum --bootnum 0
```
 when passing the boot entry number we are not requested to include the padding 0s. If the bootnum is 000A just write A



## Boot from a specific entry

First run (maybe as root)
```sh
efibootmgr -v
```

Set the entry for one time boot
```sh
sudo efibootmgr -n XXXX
```
or
```sh
sudo efibootmgr --bootnext XXXX
```

Reboot
```sh
sudo reboot
```


## Reference
- [youtube](https://youtu.be/MN-Q5h2Iv8A)
- [linuxconfig.org](https://linuxconfig.org/how-to-manage-efi-boot-manager-entries-on-linux)
- [boot from a specific boot entry](https://unix.stackexchange.com/questions/674996/how-to-reboot-on-a-specific-device-from-command-line)
