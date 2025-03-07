# Jupyterlab

Ref:-

1. [dev.to article](https://dev.to/juanbelieni/how-to-run-jupyterlab-on-docker-4n80)
2. [selecting docker image](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html)
3. [dockerizing jupyter notebook](https://www.mirsazzathossain.me/articles/dockerizing-jupyter-notebook)

Add user with 1000 to sudo passwd group
Run the following as root
```sh
docker exec -u root -it jupyterlab bash
```
```sh
username=$(getent passwd 1000 | awk -F: '{print $1}')
printf "$username ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/jupyterlab-user-1000
```

my version
```env
NOTEBOOK_USER="jupu"
JUPYTER_TOKEN="password"
```

```docker-compose
version: '3'
services:
    jupyter:
        image: jupyter/datascience-notebook:latest
        hostname: jupyter
        container_name: jupyter
        restart: unless-stopped
        ports:
            - 8888:8888
        environment:
            - JUPYTER_ENABLE_LAB="yes"
            - JUPYTER_TOKEN=${JUPYTER_TOKEN}
            - NB_UID=1000
            - NB_GID=100
            - NB_USER=${NOTEBOOK_USER}
            - NB_GROUP=users
            - CHOWN_HOME=yes
            - CHOWN_HOME_OPTS=-R
        volumes:
            - /srv/jupyterlab/work:/home/${NOTEBOOK_USER}/work
            # - /srv/jupyterlab/work/environments:/home/${NOTEBOOK_USER}/work/environments
        working_dir: /home/${NOTEBOOK_USER}/work
        user: root
        env_file:
            - .env

```


```docker-compose
version: '3'
services:
    jupyter:
        image: jupyter/datascience-notebook:latest
        container_name: jupyter
        ports:
            - 8888:8888
        environment:
            JUPYTER_ENABLE_LAB: "yes"
            JUPYTER_TOKEN: "password"
```


docker cli
```sh
docker run -p 8888:8888 \
           -e JUPYTER_ENABLE_LAB=yes \
           -e JUPYTER_TOKEN=password \
           --name jupyter \
           -d jupyter/datascience-notebook:latest
```

