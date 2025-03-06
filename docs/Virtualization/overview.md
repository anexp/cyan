# Virtualization

Ref :-
1. [Stack Exchange how to open virt manager vm from command line](https://unix.stackexchange.com/questions/704325/how-to-open-virt-manager-vm-from-command-line)

To list all vms
```sh
virsh --connect qemu:///system list --all
```

### Start VM

Virsh
```sh
virsh --connect qemu:///system start "VM-NAME"
```

Virtmanager
```sh
virt-manager --connect qemu:///system --show-domain-console "VM-NAME"
```


### Clipboard sharing

`spice-vdagent`
##### Install 
Debian
```sh
sudo apt install spice-vdagent
```
Arch
```sh
sudo pacman -S spice-vdagent
```
##### Enable daemon (Did not need to do this)
```sh
sudo systemctl enable --now spice-vdagent
```

Reboot the system the clip board sharing should work
Not sure if i have to launch it using
Works fine even without launching
```sh
spice-vdagent
```


