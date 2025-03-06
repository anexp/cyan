# Docker Swarm


https://docs.docker.com/engine/swarm/stack-deploy/

Init
```sh
sudo docker swarm init --advertise-addr <IP_ADDRESS>
```

Deploy docker compose file to stack using swarm
```sh
sudo docker stack deploy -c docker-compose.yml --detach=true <STACK_NAME>
```

Remove stack
```sh
sudo docker stack rm <STACK_NAME>
```


Remove stopped containers automatically

https://stackoverflow.com/questions/61501344/docker-swarm-how-to-remove-stopped-containers

```sh
sudo docker swarm update --task-history-limit 2
```
