# 3d acceleration

Check
```
glxinfo | grep OpenGL

# Install with
# sudo pacman -S glxinfo
```

Drivers
```
# sudo pacman -S vulkan-intel
# not needed
```


In Display Spice,
set Listen Type to None
Turn on OpenGL which should be in Display Spice Settings

Then in Video Virtio,
set model Virtio
and enable 3d accelartion

Ref 
[ArchWiki](https://bbs.archlinux.org/viewtopic.php?id=273546)

