# nftables

Ref :-
1. https://linuxhandbook.com/iptables-vs-nftables/
2. https://youtu.be/_A-Q6yTMX0g
2. [Redhat port forwarding using nftables](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/sec-configuring_port_forwarding_using_nftables)

## Install

```sh
sudo apt install nftables
```

To make sure that the nftables starts automatically when your system reboots:
```sh
sudo systemctl enable nftables.service
```


On Debian
Initial `/etc/nftables.conf`

```
#!/usr/sbin/nft -f

flush ruleset

table inet filter {
	chain input {
		type filter hook input priority filter;
	}
	chain forward {
		type filter hook forward priority filter;
	}
	chain output {
		type filter hook output priority filter;
	}
}

```


Chack if nftables.conf is valid

```sh
sudo nft -c -f /etc/nftables.conf
```

Reload
```sh
sudo systemctl restart nftables
```


```
chain input {
		type filter hook input priority filter;

		# allow from loopback
		iifname lo accept;

		# established/related connections
		ct state established,related accept;

		# invalid connections drop
		ct state invalid drop;

		# no ping floods
		ip6 nexthdr icmpv6 icmpv6 type echo-request limit rate 2/second accept;
		ip protocol icmp icmp type echo-request limit rate 2/second accept;

		tcp dport ssh accept;
		tcp dport {http,https,5900} accept;

        # allow lxdbr0
		iifname "lxdbr0" accept;
        # allow virbr0
		iifname "virbr0" accept;

		policy drop;

	}

```


```sh
sudo nft list ruleset
```



### Portforwarding

Add to `/etc/sysctl.conf`
```
net.ipv4.ip_forward = 1
```

Restart sysctl
```sh
sudo systemctl restart systemd-sysctl
```

Table type defaults to 'ip' meaning ip4 addresses

```

table nat {
    chain prerouting {
        type nat hook prerouting priority dstnat;
        iif eth0 ip daddr 10.0.0.2 tcp dport {9019} dnat to 10.4.156.113:22;
        iif eth0 ip daddr 10.0.0.2 tcp dport {9020} dnat to 10.4.156.113:80;
    }
    chain postrouting {
        type nat hook postrouting priority srcnat;
        oif eth0 masquerade;
    }
}


```


LXD provides network forward command but that ip address was not getting hit
port forward directly to the ip address accessible by the machine running lxd

say host1 is running lxd container1 at ip1
and you create a network forward for that at ip2

normally you would want to proxy through ip2
for examples applications like nginx

howwver if using nftables portforwarding hit at ip1

