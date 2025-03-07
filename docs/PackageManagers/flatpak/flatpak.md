# Flatpak on arch linux

Install flatpak
```
sudo pacman -S flatpak
```

The installation of flatpak will, by default, add the official Flathub repository as a system-wide installation. To add the official repo with a per-user configuration:

Add flathub remote repo link for per-user installation (Recommended)
```
flatpak remote-add --if-not-exists --user flathub https://dl.flathub.org/repo/flathub.flatpakrepo
```

Add flathub remote repo link for system-wide installation (Not Recommended)
Dangerous
It will ask for password everytime you try to install something
```
# system-wide installation
# flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

To delete a remote flatpak repository do:

```
flatpak remote-delete name
```

where name is the name of the remote repository to be deleted.
List repositories

To list all the added repositories do:
```
flatpak remotes
```

Search
```
flatpak search <whatever you want to search>
```

Install gnome-extensions-manager
```
flatpak install flathub com.mattjakeman.ExtensionManager
```

Flatpak packages are stored in
```
/var/lib/flatpak/repo
```

### Flathub

libflatpak libappstream

https://hub.flathub.org/repo/appstream/x86_64/appstream.xml.gz


## Beta

In addition to the existing stable repository Flathub offers a repository for beta builds. This isn’t meant to be used for nightly builds, but for releases that has some level of testing and are expected to mostly work and be usable to non-developer end-users.

Adding flathub-beta:
```sh
flatpak remote-add --if-not-exists --user flathub-beta https://flathub.org/beta-repo/flathub-beta.flatpakrepo
```
Note: --if-not-exists is not really needed

Install an application:
```sh
flatpak install flathub-beta org.godotengine.Godot
```
Note: --user installs the application for only the current user, others cannot see/use the app!

Alternatively, you can use a flatpakref, which are generated for each app:
```sh
flatpak install https://flathub.org/beta-repo/appstream/org.godotengine.Godot.flatpakref
```
If you install both the beta and the stable version of an app then they will be installed in parallel. However, only one will be showed in the menus. You can switch which one is currently showed like this:
```sh
flatpak make-current org.godotengine.Godot *[beta|stable]*
```
But from the command line you can always start any installed version explicitly, like this:
```sh
flatpak run --branch=beta org.godotengine.Godot
```
or

flatpak run org.godotengine.Godot//beta

Removing flathub-beta:
```sh
flatpak remote-delete flathub-beta
```

Reference
1. https://discourse.flathub.org/t/how-to-use-flathub-beta/2111


## NVIDIA

https://www.youtube.com/watch?v=cTNkb-qG0Dc&t=678

For obs studio and kdenlive
```
_GLX_VENDOR_LIBRARY_NAME=nvidia
_NV_PRIME_RENDER_OFFLOAD=1
```


# Flathub

https://hub.flathub.org/stats/ the source of all, but custered by days

https://flathub.org/api/v2/docs#/app/get_stats_for_app_stats__app_id__get

https://flathub.org/api/v2/stats/app-id
