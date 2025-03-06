# Encrypted USB


### Create an encrypted usb drive

Create an partition say /dev/sdd1


Make the partition encrypted, you will be prompted for a password which later be used for encryption and decryption
```sh
sudo cryptsetup luksFormat /dev/sdd1
```

```sh
sudo cryptsetup open /dev/sdd1 privateDrive
```
Now, there will be /dev/mapper/privateDrive

Make a filesystem
```sh
sudo mkfs.ext4 /dev/mapper/privateDrive
```

Mount it somewhere, as if /dev/mapper/privateDrive was a regular partiion on a drive
```sh
sudo mount /dev/mapper/privateDrive /mnt/mnt-point
```
Edit files as much you want in /mnt/mnt-point

Once, you are done editing files in your encrypted drive
```sh
sudo umount /mnt/mnt-point
```

Close the encrypted drive
```sh
sudo cryptsetup close privateDrive
```



### Changing password

For a single password,
```sh
sudo  cryptsetup luksChangeKey /dev/sdX
```
