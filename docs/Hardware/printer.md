# Printers

For specific drivers
[ArchWiki CUPS/Printer-specific_problems](https://wiki.archlinux.org/title/CUPS/Printer-specific_problems)


#### CUPS
```
sudo pacman -S cups
sudo systemctl enable cups
sudo systemctl start cups
```

#### lp group
```
sudo usermod -a $USER -G lp
# newgrp lp
```

Cups web interface opens at  **[https://localhost:631](https://localhost:631)**
Login as root and provide root password

#### GUI for CUPS
```
sudo pacman -S system-config-printer
```
Can be launched with
```
system-config-printer
```

#### For our canon printer - Canon G3010 series

```
sudo pacman -S gutenprint foomatic-db-ppds
/usr/bin/cups-genppdupdate
sudo systemctl restart cups
sudo systemctl status cups

```

#### Ghostscript
Ghostscript is needed by the printer to parse info
```
sudo pacman -S ghostsript
```

(Not sure if its needed)
For avahi
```
sudo pacman -S avahi
```

Common dependencies
```
sudo pacman -S dbus
sudo pacman -S python-dbus pygtk
sudo pacman -S python-dbus
```

avahi-daemon
```
sudo avahi-daemon
```

avahi-discover
```
avahi-discover
```

#### Reference

- [Distrotube video](https://www.youtube.com/watch?v=jnmCbEWNV1w&pp=ygUScHJpbnRlciBhcmNoIGxpbnV4)
- [Lakur.tech article](https://lakur.tech/2021/09/16/adding-a-hp-printer-on-arch-linux/)

Notes 

Management of cups is done over the cups web interface, listening on port 631. Go to https://localhost:631, click on Administration located in the top menu bar, and select “Add Printer” in the Printers section. This will ask you for your credentials, which is your local root account. Enter root as user and your root password as password and proceed.

In the following list, you’ll see some printers that could be added now. Select the desired printer and continue.
