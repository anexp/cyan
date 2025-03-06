# Awesome window manager


In minimum arch install awesome could not load fonts

To get the error message run 
```
# startx 2>~/error.txt
# or

startx 2>/home/${USER}/error.txt
```

Install the font: Make sure that the "sans" font is installed on your system.
You can install it by using the following command:

```
sudo pacman -S ttf-dejavu
```

This command installs the DejaVu fonts, which includes the "sans" font.
