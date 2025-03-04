# Bridging

```sh
 sudo brctl addbr br0
 brctl show
 sudo brctl addif br0 enp3s0
 sudo ip addr add 10.0.0.4/24 dev br0
 sudo ip link set dev br0 up
```
