# Gsettings Keyboard bindings

### GUI mode
```
gnome-control-center keyboard
```

### CLI method

To get keyboard bindings using gsettings in a Linux terminal, you can use the following command:
```
gsettings get org.gnome.desktop.wm.keybindings <keybinding>
```

Replace <keybinding> with the name of the keybinding you want to retrieve.
For example, to retrieve the keybinding for switching windows, use the following command:

```
gsettings get org.gnome.desktop.wm.keybindings switch-windows
```

This will output the current value of the keybinding in the terminal. 
If the keybinding has been modified from the default, the output will be the new binding.
If the keybinding has not been modified, the output will be the default binding.

You can also use the list-keys and list-recursively options with gsettings to list all the available keybindings for a schema and its sub-schemas, respectively.
For example:


```
gsettings list-keys org.gnome.desktop.wm.keybindings

gsettings list-recursively org.gnome.desktop.wm.keybindings
```

These commands will output a list of all available keybindings in the terminal.




### Custom key bindings
Get all custom keybindings
```
gsettings get org.gnome.settings-daemon.plugins.media-keys custom-keybindings
```

Get
```
gsettings get org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ name
gsettings get org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ command
gsettings get org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ binding
```
Set
```
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ name "Gnome terminal"
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ command "gnome-terminal"
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ binding "<Primary><Alt>t"
```

