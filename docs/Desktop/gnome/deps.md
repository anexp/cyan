# Dependencies

gtk-doc-scan
pacman : gtk-doc

rst2man
pacman : python-docutils


## Dependencies

### Console

dnf

yaml-1 -> libyaml-devel-0.2.5-12.fc39
gperf -> gperf
liblz4 -> lz4-devel ! liblzf-devel
gnutls -> gnutls-devel-3.8.2-2.fc39
libgtop-2.0 -> libgtop2-devel-2.41.2-1.fc39

Running
libvte-2.91-gtk4.so.0 ->  vte291-gtk4-devel-0.74.1-1.fc39 ! vte291-devel-0.74.1-1.fc39

aur vte-notification-common


### Evince

 ERROR: Dependency "libhandy-1" not found, tried pkgconfig and cmake
 pacman : libhandy


Not necessary
pacman 
libspectre gspell


### gnome-contacts

pacman : libportal-gt4 folks

does not work with evolution

(gnome-contacts:68019): gnome-contacts-WARNING **: 00:06:44.460: contacts-esd-setup.vala:34: Couldn't load EDS SourceRegistry: Error calling StartServiceByName for org.gnome.evolution.dataserver.Sources5: Unit evolution-source-registry.service not found.

### gnome-maps

pacman: gjs


needs libshumate 1.2-alpha

### gnome-nibbles

pacman : gsound libgnome-games-support-2

### gnome-builder

pacman : libdex libpanel gtksourceview5  jsonrpc-glib libpeas-2 template-glib vte3 vte4 webkitgtk-6.0 cmark llvm d-spy editorconfig-core-c libgit2-glib
d-spy is a debugger for gnome
cmark is needed for libcmark
vte3 and vte4 provide a way for embedding terminal emulator
