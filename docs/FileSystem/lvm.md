# Logical Volume Manager

```
sudo vgs
sudo vgdisplay
```

You may need to make a LVM volume group inactive and thus unknown to the kernel.
To deactivate a volume group, use the -a (--activate) argument of the vgchange command.
To deactivates the volume group vg, use this command

```
vgchange -a n vg
```

Increase size of my lvm

```
lvextend -L +10G /dev/vg0/lv_root
```
Now to make df -h recognize this change
```
sudo resize2fs /dev/vg0/lv_root
```
