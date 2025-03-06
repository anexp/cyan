# Libreoffice

## Build from source

### Dependencies
```sh
sudo pacman -S --needed 'base-devel' 'git' 'ccache' 'ant' 'apr' 'beanshell' 'bluez-libs' 'clucene' \
                        'coin-or-mp' 'cppunit' 'curl' 'dbus-glib' \
                        'desktop-file-utils' 'doxygen' 'flex' 'gcc-libs' \
                        'gdb' 'glm' 'gobject-introspection' 'gperf' 'gpgme' \
                        'graphite' 'gst-plugins-base-libs' 'gtk3' \
                        'harfbuzz-icu' 'hicolor-icon-theme' 'hunspell' \
                        'hyphen' 'icu' 'java-environment' 'junit' \
                        'lcms2' 'libabw' 'libatomic_ops' 'libcdr' 'libcmis' \
                        'libe-book' 'libepoxy' 'libepubgen' 'libetonyek' \
                        'libexttextcat' 'libfreehand' 'libgl' 'libjpeg' \
                        'liblangtag' 'libmspub' 'libmwaw' 'libmythes' \
                        'libnumbertext' 'libodfgen' 'liborcus' 'libpagemaker' \
                        'libqxp' 'libstaroffice' 'libtommath' 'libvisio' \
                        'libwpd' 'libwpg' 'libwps' 'libxinerama' 'libxrandr' \
                        'libxslt' 'libzmf' 'lpsolve' 'mariadb-libs' \
                        'mdds' 'nasm' 'neon' 'nspr' 'nss' 'pango' \
                        'plasma-framework5' 'poppler' 'postgresql-libs' \
                        'python' 'qt5-base' 'redland' 'sane' 'serf' 'sh' \
                        'shared-mime-info' 'ttf-liberation' 'unixodbc' \
                        'unzip' 'xmlsec' 'zip' 'gtk4' 'qt6-base' 'zxing-cpp' \
                        'abseil-cpp'
```

### Compile 

The git repo is about 6GB large so download time can be very high
```sh
git clone https://gerrit.libreoffice.org/core
cd core
```

```sh
./autogen.sh --help
./autogen.sh
```

```sh
make
make check
```


Reference:-
1. [BuildingOnLinux][https://wiki.documentfoundation.org/Development/BuildingOnLinux)
2. [Official PKGBUILD](https://gitlab.archlinux.org/archlinux/packaging/packages/libreoffice-fresh/-/blob/main/PKGBUILD)

