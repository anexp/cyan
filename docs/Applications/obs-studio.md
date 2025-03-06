# OBS Studio

You have to explicitly ask OBS Studio to use Wayland with the **QT_QPA_PLATFORM** variable

Add this line to **.bashrc** with an if condition to check if **XDG_SESSION_TYPE** is **wayland**
```
export QT_QPA_PLATFORM=wayland
```
