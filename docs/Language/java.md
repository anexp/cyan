# Java

##  Debian

### Install
```sh
# For general setup
sudo apt install openjdk-17-jdk openjdk-17-jre
# For minimal setup
sudo apt install openjdk-17-jdk-headless openjdk-17-jre-headless
```

### Switch between multiple java versions
https://askubuntu.com/questions/740757/switch-between-multiple-java-versions

Apt-get won't overwrite the existing java versions.

To switch between installed java versions, use the update-java-alternatives command.

List all java versions:
```sh
update-java-alternatives --list
```
Set java version as default (needs root permissions):
```sh
sudo update-java-alternatives --set /path/to/java/version
```
...where /path/to/java/version is one of those listed by the previous command (e.g. /usr/lib/jvm/java-7-openjdk-amd64).

or, use interactive method
```sh
sudo update-alternatives --config java
```

## Archlinux

Check current version and path to java
```sh
java --version
which java
```

Install jre
```sh
sudo pacman -sS java | grep jre
sudo pacman -S jre-openjdk
```

Install jdk 
```sh
sudo pacman -sS java | grep jdk
sudo pacman -S jdk-openjdk
```

### Switch between multiple versions of java

Install older version of java
```
sudo pacman -S jre8-openjdk
```

Set that as default
```
sudo archlinux-java set java-8-openjdk/jre
```



