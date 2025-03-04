# ADB

Install Flutter
```
git clone https://aur.archlinux.org/flutter.git
cd flutter/
makepkg -si
gpasswd -a ${USER} flutterusers
sudo gpasswd -a darklord flutterusers
man newgrp
```

install android-studio
```
git clone https://aur.archlinux.org/android-studio.git
cd android-sdk/
makepkg-si
```


install android-sdk
```
git clone https://aur.archlinux.org/android-sdk.git
cd android-sdk/
makepkg -si
```

Android-sdk group
```
sudo groupadd android-sdk

```

install android-sdk-platform tools
```
git clone https://aur.archlinux.org/android-sdk-platform-tools.git
cd android-sdk-platform-tools/
makepkg -si
```

install android-sdk-cmdline-tools-latest
```
git clone https://aur.archlinux.org/android-sdk-cmdline-tools-latest.git
cd android-sdk-cmdline-tools-latest.git
makepkg -si
```
Restart adb server
```
adb kill-server
adb start-server
```

Adb
```
adb devices
adb shell
```

No analytics(telemetry)
```
flutter config --no-analytics
```

Flutter provides a command to update the Android SDK path
```
flutter config --android-sdk <path-to-your-android-sdk-path>A
```
Android-sdk AUR is installed at /opt/android-sdk/
so, use 
```
flutter config --android-sdk /opt/android-sdk/
```
Download android toolchain
```
flutter doctor --android-licenses
```

You need to source /etc/profile or relogin to add the Android Emulator to your path
```
. /etc/profile
```
and press Enter