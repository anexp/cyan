# Sound

user must be added to the audio group
```sh
sudo usermod -aG audio $USER
# sudo usermod -aG audio NameOfUser
```
check
```sh
cat /proc/asound/cards
ls -l /dev/snd/
sudo dmesg | grep -E 'snd|sof'
```

firmware and alsa
```sh
sudo pacman -S sof-firmware
sudo pacman alsa-ucm-conf
sudo pacman -S alsa-firmware
sudo pacman -S alsa-utils
```

for pipewire (recommended)
```sh
sudo pacman -S pipewire pipewire-pulse pipewire-alsa pipewire-docs
sudo pacman -S wireplumber
# pipewire-jack is old prefer jack2
# sudo pacman -S pipewire-jack # not recommended
sudo pacman -S jack2 # recommended
```

for pulseaudio (not recommended)
```sh
sudo pacman -S pulseaudio
```

for pipewire check [./pipewire.md]

for pipewire check [./pulseaudio.md]


unmute
```sh
amixer sset Master unmute
amixer sset Speaker unmute
amixer sset Headphone unmute
```

optional
```sh
amixer -D pulse sset Master 100%
```

using alsamixer
```sh
alsamixer
```


Command history
```sh
cat /proc/asound/cards
ls -l /dev/snd/
sudo dmesg ] grep -E 'snd|sof'
sudo pacman -S sof-firmware
sudo dmesg | grep -E 'snd|sof'
sudo dmesg ] grep -E 'snd|sof'
sudo dmesg | grep -E 'snd|sof'
sudo pacman alsa-ucm-conf
sudo pacman -S alsa-ucm-conf
sudo dmesg | grep -E 'snd|sof'
sudo pacman -S alsa-ucm-conf
sudo dmesg | grep -E 'snd|sof'
amixer sset Master unmute
amixer sset Speaker unmute
amixer sset Headphone unmute
alsamixer
speaker-test -c 2
sudo pacman -S alsa-firmware
sudo dmesg | grep -E 'snd|sof'
alsamixer
amixer sset Master unmute
sudo pacman -S alsa-utils
sudo dmesg | grep -E 'snd|sof'
sudo pacman -S sof-bin
amixer sset Master unmute
reboot
alsamixer
alsamixer
sudo pacman -S alsa-utils
amixer sset Master unmute
alsamixer
clear
amixer sset Master unmute
amixer sset Speaker unmute
amixer sset Headphone unmute
amixer -D pulse sset Master 100%
amixer sset Speaker unmute
sudo pacman -S alsa-utils
amixer sset Speaker unmute
amixer sset Headphone unmute
sudo pacman -S sof-bin
sudo dmesg | grep -E 'snd|sof'
sudo pacman alsa-ucm-conf
sudo pacman -S alsa-firmware
sudo pacman -S sof-firmware
sudo dmesg | grep -E 'snd|sof'
reboot
sudo pacman -S pulseaudio
sudo dmesg | grep -E 'snd|sof'
alsamixer
alsamixer
alsamixer
cat /etc/group
cat /etc/group | grep audio
usermod -aG audio admin_user
sudo usermod -aG audio admin_user
groups
reboot
```
