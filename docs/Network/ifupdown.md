# ifupdown

Ref :
1. [linuxhandbook](https://linuxhandbook.com/ifup-ifdown-ifquery/)
2. [debian wiki networking](https://wiki.debian.org/NetworkConfiguration)

Associated systemd service `networking`

Reload
```sh
sudo systemctl reload networking
```

edit `/etc/network/interfaces` file

To source other files
```
source /etc/network/interfaces.d/*
```

To configure loopback
```
# The loopback network interface
auto lo
iface lo inet loopback
```

static ip for ethernet connection
```
# Ethernet connection
auto enp3s0
   iface enp3s0 inet static
       address 10.0.0.1/24
````


configure wifi directly
```
# The primary network interface
# allow-hotplug wlp0s20f3
# iface wlp0s20f3 inet dhcp
# 	wpa-ssid coffee_house_network_ssid
# 	wpa-psk  wifi_password_in_plain_text
```

Using DHCP to automatically configure the interface
```
    auto eth0
    allow-hotplug eth0
    iface eth0 inet dhcp
```
For DHCPv6 (used for IPv6), append also the following iface stanza
```
    iface eth0 inet6 dhcp
```

Alternatively, IPv6 can be autoconfigured using stateless address autoconfiguration, or SLAAC, which is specified using auto instead of dhcp in the inet6 stanza:
```
    iface eth0 inet6 auto
```


## Bridging
```sh
auto br0
iface br0 inet static
        address 10.0.0.5/24
        # gateway 10.0.0.1
        bridge_ports eth0 eth1

```



