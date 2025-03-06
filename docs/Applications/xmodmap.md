# Xmod 

### Swap Caps lock and Escape keys
```
xmodmap -e "keycode 9 = Caps_Lock"; xmodmap -e "keycode 66 = Escape"

```

### Undo the swap action

```
xmodmap -e "keycode 66 = Caps_Lock"; xmodmap -e "keycode 9 = Escape"

```
