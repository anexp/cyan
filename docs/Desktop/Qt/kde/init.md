# Setup KDE dev

```sh
mkdir -p ~/kde/src
cd ~/kde/src
git clone https://invent.kde.org/sdk/kdesrc-build.git
cd kdesrc-build
./kdesrc-build --initial-setup
```


For zsh
```sh
autoload -U +X compinit && compinit
autoload -U +X bashcompinit && bashcompinit
```
