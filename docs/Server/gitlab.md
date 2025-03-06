# Gitlab Self Hosted

Ref:-
1. [Gitlab on raspberrypi](https://docs.gitlab.com/omnibus/settings/rpi.html)
2. [Install gitlab on raspberrypi official](https://about.gitlab.com/install/#raspberry-pi-os)
3. [Install gitlab on raspberrypi unoffical](https://about.gitlab.com/blog/2022/03/14/installing-gitlab-on-raspberry-pi-64-bit-os/)
4. [Gitlab on arm64](https://github.com/zengxs/gitlab-arm64)

Check initial_root_password
```sh
docker exec -it gitlab_web_1 grep 'Password:' /etc/gitlab/initial_root_password
```

### Server

.env
```
GITLAB_HOME=/srv/gitlab
```

```docker-compose
version: '3.6'
services:
  web:
    image: 'docker.io/gitlab/gitlab-ce:latest'
    # image: 'docker.io/zengxs/gitlab:latest'
    restart: always
    hostname: 'gitlab-web'
    # hostname: 'gitlab.domain.tld'
    environment:
      GITLAB_OMNIBUS_CONFIG: |
        external_url 'https://gitlab.domain.tld'
        # Add any other gitlab.rb configuration here, each on its own line
        # Nginx reverse proxy
        nginx['listen_port'] = 80
        nginx['listen_https'] = false
        # Disable Usage Statistics
        gitlab_rails['usage_ping_enabled'] = false
        # Enable lfs
        gitlab_rails['lfs_enabled'] = true
        # Reduce the number of running workers to the minimum in order to reduce memory usage
        puma['worker_processes'] = 2
        sidekiq['max_concurrency'] = 9
        # Turn off monitoring to reduce idle cpu and disk usage
        prometheus_monitoring['enable'] = false
    ports:
      - '8941:80'
      - '8943:443'
      - '8945:22'
    volumes:
      - '$GITLAB_HOME/config:/etc/gitlab'
      - '$GITLAB_HOME/logs:/var/log/gitlab'
      - '$GITLAB_HOME/data:/var/opt/gitlab'
    # shm_size: '2gb'
```

##### Using apt unofficial method on raspberrypi (Recommended)

```sh
sudo apt install -y curl openssh-server ca-certificates apt-transport-https perl
curl -s https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh | sudo bash
sudo apt-get update
sudo apt-get install debian-archive-keyring
sudo apt-get install curl gnupg apt-transport-https
curl -L https://packages.gitlab.com/gitlab/gitlab-ce/gpgkey | sudo apt-key add -

cat <<EOF > /etc/apt/sources.list.d/gitlab_gitlab-ce.list
deb https://packages.gitlab.com/gitlab/gitlab-ce/debian/ buster main
deb-src https://packages.gitlab.com/gitlab/gitlab-ce/debian/ buster main
EOF


sudo apt-get update
sudo EXTERNAL_URL="http://gitlab.domain.tld" apt-get install gitlab-ce

```

##### Using apt official method for raspberrypi (does not work)
```sh

sudo apt install -y curl openssh-server ca-certificates apt-transport-https perl
curl https://packages.gitlab.com/gpg.key | sudo tee /etc/apt/trusted.gpg.d/gitlab.asc
# sudo apt-get install -y postfix
sudo curl -sS https://packages.gitlab.com/install/repositories/gitlab/raspberry-pi2/script.deb.sh | sudo bash
sudo apt update

sudo EXTERNAL_URL="https://gitlab.domain.tld" LETSENCRYPT="false" apt install gitlab-ce
```

##### LXD 

Ref:-
1. [GItlab on lxd](https://canutethegreat.medium.com/portable-devops-platform-gitlab-in-an-lxd-container-db2850224caf)

If the host system is running Ubuntu with apparmor, we will need to tell apparmor not to restrict the container (you can change it back later after the install if you wish.)

```sh
lxc config set gitlab-server security.privileged=true
# lxc config set gitlab-server raw.lxc "lxc.apparmor.profile=unconfined"
sudo sysctl -a > sysctl.bak
mount -o remount rw /proc/sys
```

```sh
cat sysctl.bak | sudo sysctl -e -p -
lxc config set gitlab-server security.privileged=false
```

##### Telemetry

Disable Telemetry in gitlab install
/etc/gitlab/gitlab.rb or $GITLAB_HOME/config/gitlab.rb
```
### Usage Statistics
# gitlab_rails['usage_ping_enabled'] = true
gitlab_rails['usage_ping_enabled'] = false
```

then as root user
```sh
gitlab-ctl reconfigure
```


### Runner

https://docs.gitlab.com/runner/install/docker.html

Use local system volume mounts to start the Runner container

```sh
docker run -d --name gitlab-runner --restart always \
  -v /srv/gitlab-runner/config:/etc/gitlab-runner \
  -v /var/run/docker.sock:/var/run/docker.sock \
  docker.io/gitlab/gitlab-runner:latest
```


The general rule is that every GitLab Runner command that normally would be executed as:
```sh
gitlab-runner <runner command and options...>
```
can be executed with:
```sh
docker run <chosen docker options...> gitlab/gitlab-runner <runner command and options...>
```

Register interactively
```sh
docker exec -it gitlab-runner gitlab-runner register
```

Register (May not work)
```sh
gitlab-runner register --url https://gitlab.domain.tld --token <token_value>
```

Unregister
```sh
gitlab-runner unregister --all-runners
gitlab-runner unregister runner_id_value
gitlab-runner verify --delete
```

