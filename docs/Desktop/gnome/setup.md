# Setup for GNOME

Standard compile instructions for GNOME native apps
```sh
git clone https://gitlab.gnome.org/GNOME/console
cd console
meson _build
ninja install -C _build
```

`ninja install -C _build` will automatically prompt for sudo user privileges during install phase
avoid using `sudo ninja install -C _build`

To uninstall
```sh
sudo ninja uninstall -C _build
```


## Reference
1. https://www.debugpoint.com/compile-gnome-source/
2. https://wiki.gnome.org/Projects/DeveloperTools/Installation/Fedora
