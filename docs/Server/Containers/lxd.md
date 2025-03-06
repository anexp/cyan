# LXD

Ref :-

1. [Archwiki LXD page](https://wiki.archlinux.org/title/LXD)

### Install

Apt method
```sh
sudo apt install lxd
```

Add regular user to lxd group
```sh
sudo gpasswd -a $USER lxd
```

Enable lxd service and socket
```sh
sudo systemctl enable --now lxd.service
sudo systemctl enable --now lxd.socket
```

### Commands

List remotes
```sh
lxc remote list
```

List all images in remote images:
```sh
lxc image list images:
```

List remotes with name "debian" in name
```sh
lxc image list images: debian
```
or
```sh
lxc image list images: ubuntu focal
```

```sh
lxc list
```

```sh
lxc launch images:debian/12 deb1
```

```sh
lxc exec deb1 bash
```

```sh
lxc stop deb1
```

```sh
lxc start deb1
```

```sh
lxc restart deb1
```

```sh
lxc delete deb1
```

```sh
lxc snapshot deb1 deb1_snapshot
```

```sh
lxc info deb1
```

Delete snapshot
```sh
lxc delete deb1/deb1_snapshot
```

Restore from a snapshot
```sh
lxc restore deb1 deb1_snapshot
```

Start on boot
```sh
lxc config set deb1 boot.autostart 1
```

Set memory limit
```sh
lxc config set deb1 limits.memory 1GB
```

Show config
```sh
lxc config show deb1
```

Delay autostart by 30s
```sh
lxc config set deb1 boot.autostart.delay 30
```

Autostart order (priority)
```sh
lxc config set deb1 boot.autostart.order 8
```


### Tricks

#### Run docker inside lxd
ref : https://discourse.ubuntu.com/t/how-to-run-docker-inside-lxd-containers/26730

```sh
lxc config set CONTAINER_NAME security.nesting=true security.syscalls.intercept.mknod=true security.syscalls.intercept.setxattr=true
```

```sh
lxc profile create docker
lxc profile set docker security.nesting=true security.syscalls.intercept.mknod=true security.syscalls.intercept.setxattr=true
```

To add to docker profile
```sh
lxc profile add CONTAINER_NAME docker
```

RLIMIT
https://discuss.linuxcontainers.org/t/error-setting-rlimits-type-8-operation-not-permitted-unknown-in-lxd-container/9976/4

```sh
lxc config set CONTAINER_NAME limits.kernel.memlock unlimited
```

#### Network forwards

[Network forwards](https://www.youtube.com/watch?v=B-Uzo9WldMs)

```sh
lxc network forward list lxdbr0
```

```sh
lxc network forward create lxdbr0 ip_address_on_host
```

```sh
lxc network forward edit lxdbr0 ip_address_on_host
```

```
config:
    target_address: ip_address_of_container
```

```
ports
- description: netcat
  protocol: tcp
  listen_port: 1234
  target_address: ip_address_of_container
```


```
config:
  target_address: ip_address_of_container
ports
- description: netcat
  protocol: tcp
  listen_port: port_of_host
  target_port: port_of_container
  target_address: ip_address_of_container
```


### External storage

Ref:-
1. https://www.youtube.com/watch?v=XdEugVsYp4U

```sh
lxc config device add CONTAINER_NAME DEVICE_NAME disk source=HOST_PATH path=CONTAINER_PATH
```

Allow lxd daemon to remap my host user id (say 1000)
```sh
echo "root:1000:1" | sudo tee -a /etc/subuid /etc/subgid
```

Remap host id
map host id 1000 on LXD HOST to host id 1001 on LXD CONTAINER
```sh
lxc config set CONTAINER_NAME raw.idmap "both 1000 1001"
```


#### Using btrfs

⚠️ Docker will not run well with the default zfs file system

Btrfs is one of the storage pools Docker supports natively, so we should create a new btrfs storage pool and we will call it “docker”:

```sh
lxc storage create docker btrfs
```
Now we can create a new LXD instance and call it “demo”:
```sh
lxc launch images:ubuntu/20.04 demo
```
We can proceed and create a new storage volume on the “docker” storage pool created earlier:
```sh
lxc storage volume create docker demo
```

We will attach it to the “demo” container and call the device being added as “docker”. Source volume is “demo” we created earlier, and we want that volume to be used for /var/lib/docker:
```sh
lxc config device add demo docker disk pool=docker source=demo path=/var/lib/docker
```



### LXDware Web ui

Works only in amd64 not aarch64
```sh
podman run -d --name dashboard -p 8961:80 -v /srv/lxdware:/var/lxdware --restart=always docker.io/lxdware/dashboard:latest
```



### No outgoing internet access


#### Approach 1
https://discuss.linuxcontainers.org/t/containers-do-not-have-outgoing-internet-access/10844/3

Add to `/etc/sysctl.conf` or `/etc/sysctl.d/99-sysctl.conf` (which is just a symlink of former)

```
net.ipv4.conf.all.forwarding=1
````

```sh
sudo systemctl restart systemd-sysctl
```

#### Approach 2

Run as root
```sh
for ipt in iptables iptables-legacy ip6tables ip6tables-legacy; do $ipt --flush; $ipt --flush -t nat; $ipt --delete-chain; $ipt --delete-chain -t nat; $ipt -P FORWARD ACCEPT; $ipt -P INPUT ACCEPT; $ipt -P OUTPUT ACCEPT; done
```

iptables package causes this issue
iptables is dependency of both docker and ufw



### Full Desktop

ref : https://ubuntu.com/tutorials/how-to-launch-an-instantly-functional-linux-desktop-vm-with-lxd#3-lets-do-one-more--archlinux-desktop-vm

Ubuntu Desktop
```sh
lxc launch images:ubuntu/22.04/desktop ubuntu --vm -c limits.cpu=4 -c limits.memory=4GiB --console=vga
```

Archlinux Desktop (disable secure boot)
```sh
lxc launch images:archlinux/desktop-gnome archlinux --vm -c security.secureboot=false -c limits.cpu=4 -c limits.memory=4GiB --console=vga
```

Connect to it afterwards
```sh
lxc console ubuntu --type vga
```



### Docker and LXD

No internet in lxd containers

Add to /etc/sysctl.conf
```
net.ipv4.ip_forward=1
```

https://wiki.debian.org/LXD



### Remote change

https://discourse.ubuntu.com/t/is-lxc-image-list-images-doesnt-return-anything-does-canonical-have-an-alternative-image-server-yet/42798/13

https://discourse.ubuntu.com/t/new-lxd-image-server-available-images-lxd-canonical-com/43824

```sh
lxc remote add images-canonical https://images.lxd.canonical.com --protocol=simplestreams
```
