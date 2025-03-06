
# Network in KVM

Ref 
1. [YouTube How to Install KVM and Configure Bridge Network in Debian12](https://youtu.be/KFVe0-B2yLI)

```sh
sudo virsh net-start default
sudo virsh net-autostart default
sudo virsh net-list --all
sudo modprobe vhost_net
```


add to /etc/modules
```
vhost_net
```

