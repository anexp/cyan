# Nix package manager

#### Search
```sh
nix-env -qaP --description [package_name]
```
or, not recommended
```sh
nix search nixpkgs [package_name]
```

#### Install
```sh
nix-env -iA [package_name]
```

#### Uninstall
```sh
nix-env --uninstall [package_name]
```
### Channels

```sh
sudo -i nix-channel --list
```

### Collect Garbage / Clean cache
```sh
nix-collect-garbage
```

to remove old generations
```sh
nix-collect-garbage -d
```

```sh
nix run nixpkgs#hello
nix run nixpkgs#virtualbox
```

```sh
nix shell nixpkgs#hello
```

non-free software
```sh
nix run --impure nixpkgs#virtualboxWithExtpack
```

List all packages
```sh
nix-env -qa --installed "*"

```




### Locale

https://unix.stackexchange.com/questions/187402/nix-package-manager-perl-warning-setting-locale-failed

```
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
        LANGUAGE = "",
        LC_ALL = "en_US.UTF-8",
        LC_CTYPE = "en_US.UTF-8",
        LANG = "en_US.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
```

```sh
nix-env -iA nixpkgs.glibcLocales
```

And in your bash profile:
```sh
export LOCALE_ARCHIVE="$(nix-env --installed --no-name --out-path --query glibc-locales)/lib/locale/locale-archive"
```
