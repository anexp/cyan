# Xorg tricks

## Using ssh session

First, check which DISPLAY you want to manipulate using 
```sh
echo $DISPLAY
```

### xdotool

```sh
DISPLAY=:1 xdotool getactivewindow type 'your text here'
```

### xclip

```sh
echo "your text here" | xclip -d :1 -sel clip
```sh
