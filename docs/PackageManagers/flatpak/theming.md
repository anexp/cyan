# Flatpak

#### Sources
- [Reddit post](https://www.reddit.com/r/flatpak/comments/y9jmqj/the_general_flatpak_qt_and_gtk_theming_guide/)

- [Its FOSS post](https://itsfoss.com/flatpak-app-apply-theme/)


## Qt

Necessary Programs
You need to install (1) Kvantum Manager with your distribution package manager, and (2) the Kvantum Theme you wish to apply (it affects QT apps for both your distribution and Flatpak packages).

Filesystem Permissions
```
sudo flatpak override --filesystem=xdg-config/Kvantum:ro
```
Why this command?

Not sure, but apparently it gives access to Kvantum configuration files, including the picked theme and its tweaks (such as transparency).

Environment Variables
```
sudo flatpak override --env=QT_STYLE_OVERRIDE=kvantum
```
Why this command?

Also not sure enough, but I think it forces QT apps to pick the theme from Kvantum. Even with this, some apps won't obey, such as Krita.

Runtimes
Obtained through Flathub only with the CLI, must be searched with flatpak install RUNTIME_NAME, which are:
```
org.kde.KStyle.Kvantum	
org.kde.PlatformTheme.QGnomePlatform
```
Which branch? I am not sure, but for org.kde.KStyle.Kvantum branches 5.15 and 5.15-21.08 should be installed. For org.kde.PlatformTheme.QGnomePlatform, branches 5.15-21.08 and 5.15-22.08 should get the work done.



## Gtk
