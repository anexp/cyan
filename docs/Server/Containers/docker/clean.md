# Clean docker



To remove all Docker containers, volumes, and networks while keeping cached images, you can use a combination of Docker commands and shell scripting. Here's a step-by-step guide to achieve this:

Warning: This will permanently delete all containers, volumes, and networks on your system. Make sure you have backups or are okay with losing this data before proceeding.

Stop and remove all running containers:
```sh
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```

`docker ps -a -q` lists all containers, and `docker stop` stops them, followed by docker rm which removes them.
Remove all Docker volumes:
```sh
docker volume rm $(docker volume ls -q)
```
`docker volume ls -q` lists all volumes, and `docker volume rm` removes them.
Remove all Docker networks:
```sh
docker network rm $(docker network ls -q)
```
`docker network ls -q` lists all networks, and `docker network rm` removes them.
Check that you've successfully removed all containers, volumes, and networks. You can use the following commands to verify:
```sh
docker ps -a
docker volume ls
docker network ls
```
Your system should now be free of containers, volumes, and networks. However, your Docker images should still be cached. To verify this, you can list your Docker images using:
```sh
docker images
```
Now, only your Docker images remain, and everything else has been removed.

In short,
```sh
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker volume rm $(docker volume ls -q)
docker network rm $(docker network ls -q)
```
```sh
docker stop $(docker ps -a -q) ; docker rm $(docker ps -a -q) ; docker volume rm $(docker volume ls -q) ; docker network rm $(docker network ls -q) ;
```
