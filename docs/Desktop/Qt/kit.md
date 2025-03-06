# Kit

Setup kit for qt creator

https://www.youtube.com/watch?v=eZ-HOc2P_EI


For qt5
```sh
sudo apt install qtbase5-dev qt5-qmake
```
https://superuser.com/questions/850029/could-not-find-a-configuration-file-for-package-ecm-that-is-compatible-with-re
```sh
sudo apt install extra-cmake-modules
```

https://stackoverflow.com/questions/64882226/which-dev-packages-are-needed-to-build-a-qtquick-application-on-ubuntu-20-04
```sh
sudo apt install qtdeclarative5-dev
```

https://stackoverflow.com/questions/50103959/error-when-trying-to-import-quickcontrols

```sh
sudo apt-get install qtbase5-dev
## provides Core, Sql and Widgets
sudo apt-get install qtdeclarative5-dev
## provides Quick and Qml
sudo apt-get install qtmultimedia5-dev
## provides Multimedia
sudo apt-get install qtquickcontrols2-5-dev
## provides QuickControls2

```


Flatpak
```
flatpak install org.kde.Sdk/x86_64/5.15-22.08
```
Qt webengine

https://discourse.flathub.org/t/distributing-a-qt-app-in-a-flatpak-with-webengine/5224/3

https://github.com/flathub/io.qt.qtwebengine.BaseApp

