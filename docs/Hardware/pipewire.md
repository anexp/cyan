# Pipewire

Install
```
sudo pacman -S pipewire pipewire-pulse pipewire-alsa pipewire-jack pipewire-docs 
sudo pacman -S wireplumber
sudo pacman -S pavucontrol

# Optional
# sudo pacman -S helvum easyeffects
```

I tried adding `wireplumber &` to `~/.config/qtile/initialize_script.sh`
it was having problems
then i removed the line
systemd started wireplumber by default

in cases of problems try 
```
pkill wireplumber
wireplumber & 
```

### Reference

[wireplumber](https://www.youtube.com/watch?v=gOhWDGA8pC8)
[pipewire-media-session(deprecated)](https://www.youtube.com/watch?v=zmNCi9wqiuU)
[linux audio in general](https://youtu.be/HxEXMHcwtlI)



## Uninstall
To uninstall pipwire utilities
```
sudo pacman -S jack2
# Replacement of pipewire-jack

sudo pacman -Rns pipewire-pulse pipewire-alsa pipewire-jack pipewire-docs 
sudo pacman -RnS helvum easyeffects

sudo pacman -Rns wireplumber
sudo pacman -Rns pavucontrol

```

Command history

```

 2069  pkill pipewire
 2070  sudo pacman -S pipewire pipewire-pulse pipewire-alsa pipewire-jack pipewire-docs helvum easyeffects
 2071  sudo pacman -S wireplumber
 2072  sudo systemctl status pipewire-pulse
 2073  sudo systemctl status pipewire-pulse.service
 2074  wireplumber
 2076  ps aux | grep wireplumber
 2077  pactl infop
 2079  nmtui
 2080  alsamixer
 2081  pactl info
 2083  helvum
 2084  pkill wireplumber
 2085  h
 2087  easyeffects
 2088  pipewire
 2089  pacman -sS pipewire
 2090  pavucontrol
 2091  wireplumber


```
