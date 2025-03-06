# Groups


To add current user to power group
```
sudo gpasswd -a $USER power
```

To remove current user from power group
```
sudo gpasswd -d $USER power
```

Log out and log back in for the changes to take effect.

To list all the existing groups
```
cat /etc/group
```
