# SSH


Ref :-
1. [Stack Overflow User match SSH keypair](https://superuser.com/questions/1425859/how-to-use-ssh-config-with-matches-for-users)
2. [Ssh config for matching users](https://superuser.com/questions/1425859/how-to-use-ssh-config-with-matches-for-users
)

Ssh tunnel
```sh
ssh -N -L client_port:target_server_ip_hostname:target_server_port user:ip_hostname
```

-N flag is to prevent an ssh shell


Remove host key
```sh
ssh-keygen -f "$HOME/.ssh/known_hosts" -R "deb1-vm"
```

Connect without messing up ~/.ssh/known_hosts
```sh
ssh -v -o UserKnownHostsFile=$(mktemp) -i ~/.ssh/private_key_name -p port_no username@remote_op
```

To login using password authentication
```sh
ssh -o PreferredAuthentications=password user@hostname
```


Correct permissions
```sh
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```


Login and execute a single command
```
command="cd /path/to/directory; borg serve --restrict-to-path /path/to/directory",restrict ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC...
```



## raspberrypi

```
ssh-keygen  -t rsa -b 4096 -C "comment" -N "" -f ~/.ssh/raspberrypi_rsa
ssh-copy-id -i ~/.ssh/raspberrypi_rsa.pub pi@raspberrypi
```


Then make changes to ~/.ssh/config file



### Mount sftp remote with rclone without config

```sh
rclone mount \
	--sftp-host 1.2.3.4 \
	:sftp:/remote/path \
	/path/to/mount \
	--volname "MyVol01" \
	--allow-non-empty \
	--sftp-key-file /path/to/id_rsa \
	--sftp-user user \
	--sftp-shell-type unix \
	--sftp-md5sum-command md5sum \
	--sftp-sha1sum-command sha1sum
```
