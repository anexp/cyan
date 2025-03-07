# apt - Advanced Package Manager


## Search 
```sh
apt search <package_name>
```
By default search will  look for a piece of text in the package description

Restrict search to names only
```sh
apt search --names-only <package_name>
```

regex is supported
```sh
apt search ^git$
```


## Download

Download a deb file to the current directory
```
apt download libayatana-indicator-dev
```


## Sources


According to wiki
for contrib and non-free
and backports

href : https://wiki.debian.org/SourcesList


my preference
```
deb http://deb.debian.org/debian bookworm main contrib non-free non-free-firmware
deb-src http://deb.debian.org/debian bookworm main contrib non-free non-free-firmware

deb http://deb.debian.org/debian-security bookworm-security main contrib non-free non-free-firmware
deb-src http://deb.debian.org/debian-security bookworm-security main contrib non-free non-free-firmware

deb http://deb.debian.org/debian bookworm-updates main contrib non-free non-free-firmware
deb-src http://deb.debian.org/debian bookworm-updates main contrib non-free non-free-firmware

# For backports
deb http://deb.debian.org/debian bookworm-backports main contrib non-free non-free-firmware
deb-src http://deb.debian.org/debian bookworm-backports main contrib non-free non-free-firmware
```

using iitkcse mirror
```
deb http://mirror.cse.iitk.ac.in/debian bookworm main contrib non-free non-free-firmware
deb-src http://mirror.cse.iitk.ac.in/debian bookworm main contrib non-free non-free-firmware

deb http://security.debian.org/debian-security bookworm-security main contrib non-free non-free-firmware
deb-src http://security.debian.org/debian-security bookworm-security main contrib non-free non-free-firmware

deb http://mirror.cse.iitk.ac.in/debian bookworm-updates main contrib non-free non-free-firmware
deb-src http://mirror.cse.iitk.ac.in/debian bookworm-updates main contrib non-free non-free-firmware

# For backports
deb http://mirror.cse.iitk.ac.in/debian bookworm-backports main contrib non-free non-free-firmware
deb-src http://mirror.cse.iitk.ac.in/debian bookworm-backports main contrib non-free non-free-firmware
```

fresh install installation

```
dec http://deb.debian.org/debian/ bookworm main non-free-firmware
deb-src http://deb.debian.org/debian/ bookworm main non-free-firmware

dec http://security.debian.org/debian-security bookworm-security main non-free-firmware
deb-src http://security.debian.org/debian-security bookworm-security main non-free-firmware

dec http://deb.debian.org/debian/ bookworm-updates main non-free-firmware
deb-src http://deb.debian.org/debian/ bookworm-updates main non-free-firmware
```


new standard
```
Types: deb
# http://snapshot.debian.org/archive/debian/20231030T000000Z
URIs: http://deb.debian.org/debian
Suites: bookworm bookworm-updates
Components: main
Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg

Types: deb
# http://snapshot.debian.org/archive/debian-security/20231030T000000Z
URIs: http://deb.debian.org/debian-security
Suites: bookworm-security
Components: main
Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg
```
