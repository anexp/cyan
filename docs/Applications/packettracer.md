# Cisco Packet Tracer

### Install
Dependencies

```sh
sudo apt install -y \
    libqt5networkauth5 libqt5xml5 \
	libqt5script5 libqt5scripttools5 libqt5multimedia5 \
	libqt5websockets5 libqt5sql5 \
    libqt5webengine5 libqt5webenginewidgets5 \
	libqt5texttospeech5
```

cp missing libraries
```sh
cd /opt/pt/bin
sudo cp -v libssl.so.1.1 libcrypto.so.1.1 /usr/lib/x86_64-linux-gnu/
```

#### Library missing resolution detail (just explanation no need to run these commands)

If you check out the libraries required by using this command:
```sh
cd /opt/pt/bin
ldd Packettracer
```

you'll see all the libraries inclunding the missing ones
So to solve this problem just copy the library missing like :

```sh
sudo cp /opt/pt/bin/libname /usr/lib/x86_64-linux-gnu/
```



### Does not work


Install libssl1.0.0 (does  not work)
```sh
wget https://packages.debian.org/jessie/amd64/libssl1.0.0/download
dpkg -i libssl1.0.0_1.0.1t-1+deb8u6_amd64.deb
```
