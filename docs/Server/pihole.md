# PiHole

Ref
1. [Insall Pi-hole](https://docs.pi-hole.net/main/basic-install/)

# Install

If you can access rawgithubusercontent
```sh
curl -sSL https://install.pi-hole.net | bash
```

```sh
git clone --depth 1 https://github.com/pi-hole/pi-hole.git Pi-hole
cd "Pi-hole/automated install/"
sudo bash basic-install.sh
```

Port forward port 53  for nameserver (Mandatory)

Port forward port 80 using ssh to access  web console

To access web console
Go to ip-address/admin or (localhost:port/admin if using ssh tunnel)


To make dns queries to a particular dns server  (for verification/testing) for a particular domain
```sh
dig @1.1.1.1 google.com
dig @ip-address domain.tld
```


/etc/nftables.conf for port forwarding
```
table nat {
    chain prerouting {
        type nat hook prerouting priority dstnat;
        iif eth0 ip daddr 192.168.29.209 tcp dport {53} dnat to 10.7.12.240:53;
        iif eth0 ip daddr 192.168.29.209 udp dport {53} dnat to 10.7.12.240:53;
    }
    chain postrouting {
        type nat hook postrouting priority srcnat;
        oif eth0 masquerade;
        oif lxdbr0 masquerade;
    }
}

```


