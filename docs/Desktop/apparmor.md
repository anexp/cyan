# Apparmor

Ref 
1. [Official Documentation on Gitlab](https://gitlab.com/apparmor/apparmor/-/wikis/Documentation)

May reload with `apparmor_parser` (Not recommended)
```
apparmor_parser /path_to_config
```

But recommended way
```
sudo systemctl reload apparmor.service
```


Allow access to all files in home directory
```
# Allow read and write access to all files and directories in the user's home directory
# @{HOME}/** rw,
```


Allow access to specific file types in home directory
```
# Allow read access to .html, .css, and .js files inside $HOME
@{HOME}/**/*.md r,
@{HOME}/**/*.html r,
@{HOME}/**/*.css r,
@{HOME}/**/*.js r,
```

