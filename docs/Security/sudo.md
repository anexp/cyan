# Sudo

For group add a percentage % sign before the group name


```
# Allow members of group sudo to execute any command
%sudo	ALL=(ALL:ALL) ALL
```


```
# Allow members of group sudo to execute any command without password
%sudo	ALL=(ALL) NOPASSWD:ALL
```


For a user with passwordless sudo
```
# User ansible to execute any command without password
ansible ALL=(ALL) NOPASSWD: ALL
```
