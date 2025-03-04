# SSH

## Config ~/.ssh/config file

```
# Github.com
Host github.com
  User git
  PreferredAuthentications publickey
  # IdentityFile ~/.ssh/github_user1
  IdentityFile ~/.ssh/github_user2
```

```
# AUR
Host aur.archlinux.org
  User aur
  PreferredAuthentications publickey
  IdentityFile ~/.ssh/aur
```

```
# homeserver.internal
Match user articuno host "homeserver.internal"
    IdentityFile ~/.ssh/homeserver_internal_articuno

```

You may omit the user field
```
# Test VM
Match host "some-vm.internal"
    PreferredAuthentications password

```


