# Torctl

[wikihow route traffic through tor](https://www.wikihow.com/Route-All-Network-Traffic-Through-the-Tor-Network)

```sh
git clone https://github.com/BlackArch/torctl
cd torctl
sudo cp -v service/* /etc/systemd/system/
sudo cp -v bash-completion/torctl /usr/share/bash-completion/completions/torctl

```

On Debian
```sh
sed -i 's/start_service iptables//' torctl
sed -i 's/TOR_UID="tor"/TOR_UID="debian-tor"/' torctl
```

```sh
sudo cp -v torctl /usr/local/bin/torctl.
```
