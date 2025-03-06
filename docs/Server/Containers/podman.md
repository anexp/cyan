# Podman


## Systemd Service for restart

ref - https://github.com/containers/podman/issues/10539

For autorestarting containers on startup enable podman-restart systemd service
```sh
sudo systemctl enable --now podman-restart
```
For user
```sh
systemctl --user enable --now podman\
```


## List all containers
```sh
podman ps -a
```

## Remove all containers
```sh
podman rm -af
```

## Pull from docker.io

for mongo:latest
```sh
podman pull docker.io/library/mongo
```
for searxng
```sh
podman pull docker.io/searxng/searxng
```

## Run

In Detached mode
```sh
podman run -d  mongo
```
Most flags are passed as key value pairs

Setting name of container
```sh
podman run -d --name=mongo mongo
```

Setting environment variables

We are using the -e flag twice since we are setting two environment variables
```sh
podman run -d -e MONGODB_INITDB_ROOT_USERNAME=admin -e MONGODB_INITDB_ROOT_PASSWORD=password
```

Ports
Maps host's port 2717 to container's port 27017
```sh
podman run -p 2717:27017 --name mongo mongo
```

Volumes
Maps host's ~/mongo-db-test directory to container's /data/db directory
```sh
podman run -v ~/mongo-db-test:/data/db --name mongo mongo
```

Run in interactive mode
```sh
podman run -it mongo
```

Delete container after running
```sh
podman run -it --rm mongo
```

Replace container with existing name
```sh
podman run -it --rm --name=mongo mongo
```

Restart Policy
options no,always
```sh
podman run --restart=always mongo 
```





## Exec

-it flag for interactive
```sh
podman exec -it <container-name> /bin/bash
```

## Attach  (does not create a different process)

```sh
podman attach <container-name>
```


## Compose

Create a file docker-compose.yml
Run the following command in the directory containing the file
```sh
podman-compose up -d
```


## Crontab (not recommended anymore)

For regular users

To run /usr/bin/podman container start --all
The user needs to be logged in

This is because of daemon less nature of podman

ref : https://linuxhandbook.com/autostart-podman-containers/

Think : Following command enable linger for root user not regular user
```sh
sudo loginctl enable-linger
```
