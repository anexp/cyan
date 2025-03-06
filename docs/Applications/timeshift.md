# Timeshift


Create explicit mounts
```
UUID=uuid_value /var/lib/docker/btrfs           btrfs   rw,noatime,space_cache=v2,compress=zstd,ssd,discard=async,subvol=@docker 0       0
UUID=uuid_value /var/lib/lxd/storage-pools           btrfs   rw,noatime,space_cache=v2,compress=zstd,ssd,discard=async,subvol=@lxd 0       0
```
