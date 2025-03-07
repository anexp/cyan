# Flatpak-builder


Install dependencies

```sh

flatpak install flathub org.freedesktop.Platform//22.08 org.freedesktop.Sdk//22.08

```


Build flatpak
```sh

flatpak-builder --user --install --force-clean build-dir manifest.yml

```
