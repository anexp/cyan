# Tcp dump

Say, to capture tcp packets sent by host1 to host3 using ping
and host2 is the intermediary

Run tcpdump in host2

```sh
sudo tcpdump -envi wg0 host 8.8.8.8
```
wg0 is the interface
8.8.8.8 is the ip address of host3
