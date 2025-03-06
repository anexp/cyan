# borg

Ref:-
1. [Borg backup central repo](https://borgbackup.readthedocs.io/en/stable/deployment/central-backup-server.html)

In ~/.ssh/authorized_keys add entry
```
command="cd /path/to/directory; borg serve --restrict-to-path /path/to/directory",restrict ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC...
```

like
```
command="cd /home/backup/repos/<client fqdn>; borg serve --restrict-to-path /home/backup/repos/<client fqdn>",restrict <keytype> <key> <host>
```

Then manually initialize repo
```sh
borg init backup@backup01.srv.local:pictures
```
