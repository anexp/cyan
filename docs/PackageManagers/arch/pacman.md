# Pacman 

[link](https://itsfoss.com/pacman-command/)

To list installed packages which are not present in the official repository
AUR packages or other third party repositories
```
pacman -Qm 
```

To see where packaes are installed
```
pacman -Ql
```


### Cache - Space problem

[link](https://discovery.endeavouros.com/articles/root-partition-full-dont-panic-clear-pacmans-cache-first/2020/03/)

When you install a package with Pacman, it stores all downloaded packages in
```
/var/cache/pacman/pkg/ 
```

The package manager doesn’t remove old and uninstalled packages 
automatically by default.

To check how many packages are in the paccache
```
ls /var/cache/pacman/pkg/ | wc -l
```

To know how much space the cache is taking
```
du -sh /var/cache/pacman/pkg/
```

To clear the cache, except the last three versions of each package by typing
```
sudo paccache -r
```

To clear the cache from your uninstalled packages
```
sudo paccache -ruk0
```
U in this command stands for all the uninstalled package

### Uninstall total cache (Caution Danger)

Another method to clear uninstalled packages is using
```
sudo pacman -Sc
```
Or to completely remove it use
```
sudo pacman -Scc
```
Just be careful with cleaning the cache and packages with this command,
it seems tempting to use it, but once deleted there’s no turning back.

