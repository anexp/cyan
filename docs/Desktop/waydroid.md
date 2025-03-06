# Waydroid

Ref:-
1. [install waydroid on desktop](https://docs.waydro.id/usage/install-on-desktops)
2. [waydroid in vm without 3d acceleration](https://docs.waydro.id/faq/get-waydroid-to-work-through-a-vm)

# Get Waydroid to work through a VM
This also applies to any unsupported GPU's as well (like nVidia)
You can force Waydroid to run without GPU acceleration by modifying the waydroid configuration file:
```sh
nano /var/lib/waydroid/waydroid.cfg
```
Add the following lines in the [properties] section:
```
ro.hardware.gralloc=default
ro.hardware.egl=swiftshader
```
Apply the configuration with:
```sh
sudo waydroid upgrade -o
```

Restart waydroid container
```sh
sudo systemctl restart waydroid-container
```
