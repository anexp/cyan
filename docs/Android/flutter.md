# Flutter

```sh
sudo apt install cmake ninja-build libgtk-3-dev
```

Flutter was installed on /opt/flutter

In case you encounter problems using Flutter as regular user, add your user into the group flutterusers:
```
gpasswd -a ${USER} flutterusers
```
Re-login your terminal in to the group flutterusers:
```
newgrp flutterusers
```
Run the following command to see if there are any dependencies you need to install to complete the setup (for verbose output, add the -v flag):
```
flutter doctor
```
Optional dependencies for flutter
```
    android-sdk
    android-studio
    intellij-idea-community-edition
    intellij-idea-ultimate-edition
    ninja [installed]
    perl [installed]
```
Flutter create template application
```
flutter create --template app --overwrite .
```
Run
```
flutter run lib/main.dart
```

Check out the official documentation
[Documentation](https://docs.flutter.dev/reference/flutter-cli)
