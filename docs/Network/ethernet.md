# Direct Ethernet 

To see information about a particular interface
```sh
ip addr show dev eth0
```

To assign the IP address broadcast address (subnet mask manually)
```sh
sudo ip addr flush dev eth0
sudo ip addr add 10.0.0.2/24 brd 10.0.0.255 dev eth0
```



Ref : 
1. [ArchWiki networking IP address](https://wiki.archlinux.org/title/Network_configuration#IP_addresses)
2. [Ask Ubuntu](https://askubuntu.com/questions/22835/how-to-network-two-ubuntu-computers-using-ethernet-without-a-router/)
