# Docker volume


Ref :- 
1. [Youtube Christan Lempa Migrating Docker Volumes](https://youtu.be/ZEy8iFbgbPA)
2. [Docker Documentation](https://docs.docker.com/storage/volumes/)
3. [Docker CLI cheatsheet](https://github.com/ChristianLempa/cheat-sheets/blob/main/docker/docker.md)
4. [Ansible Playbook](https://github.com/thedatabaseme/docker_backup/tree/master)


## Backup a container

Backup docker data from inside container volumes and package it in a tarball archive. 
```sh
docker run --rm --volumes-from CONTAINER -v $(pwd):/backup busybox tar cvfz /backup/backup.tar CONTAINERPATH
```

## Restore container from backup

Restore the volume with a tarball archive. 
```sh
docker run --rm --volumes-from CONTAINER -v $(pwd):/backup busybox sh -c "cd CONTAINERPATH && tar xvf /backup/backup.tar --strip 1"
```



