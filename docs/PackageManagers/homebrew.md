# Home Brew 

### On Linux

#### On Debian

Dependencies
```sh
sudo apt-get install build-essential procps curl file git
```

Install script
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Add the following to .bashrc or .zshrc
```sh
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
```

Remove all
```sh
brew remove --force $(brew list)
```

```sh
brew tap faye/core git@git.srv1.internal:faye/homebrew-core
```

1. https://medium.com/prodopsio/creating-homebrew-taps-for-private-internal-tools-c41363d58ab0
2. https://wheniwork.engineering/creating-a-private-homebrew-tap-with-gitlab-8800c453d893

##### Uninstall package with dependencies

`brew autoremove` removes packages installed as dependencies of other packages
```sh
brew uninstall [formula] ;  brew autoremove
```
