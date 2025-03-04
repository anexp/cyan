# Android Development

Help website
[Link](https://dev.to/nabbisen/start-flutter-2-in-arch-linux-4ab6)

```
sudo pacman -Sy dart
```

optionally, install android-tools so that you can use adb aka Android Debug Bridge and so on.
```
sudo pacman -Sy android-tools
```

ArchWiki android
[Link](https://wiki.archlinux.org/title/android)

Install Flutter using AUR
```
git clone https://aur.archlinux.org/flutter.git
cd flutter
makepkg -si
cd ..
```

Install Android Studio
```
git clone https://aur.archlinux.org/android-studio.git
cd android-studio
makepkg -si
cd ..
```

 Set permissions for Flutter

Add permission on /opt/flutter which is created in installing flutter:
```
sudo gpasswd -a <your-user> flutterusers
```

Run flutter doctor with --android-licenses option to install Android licenses. You will be asked if you accept them:
```
flutter doctor --android-licenses
```

After accepting all of them, run flutter doctor without any options, which will be successful:
```
flutter doctor
```


