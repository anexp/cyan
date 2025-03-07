# Jellyfin

```docker-compose
version: '3'
services:
  jellyfin:
    image: docker.io/jellyfin/jellyfin:latest
    restart: unless-stopped
    # container_name: myjellyfin
    # detach: true
    labels:
      io.containers.autoupdate: registry
    # user: '{{UID}}:{{GID}}'
    # userns: keep-id
    ports:
      - '8934:8096/tcp'
    volumes:
      - '$JELLYFIN_HOME/cache:/cache:Z'
      - '$JELLYFIN_HOME/config:/config:Z'
      - '/var/lib/transmission-daemon/downloads:/media/Transmission-Downloads:ro'
      - '/mnt/briggs/briggs/Media/Videos/Movies:/media/Videos/Movies:ro'
      - '/mnt/briggs/briggs/Media/Videos/Courses:/media/Videos/Courses:ro'
      - '/mnt/briggs/briggs/Media/Music:/media/Music:ro'
      - '/mnt/briggs/briggs/Media/Family:/media/Family:ro'
# volumes:
#   jellyfin-cache:
#   jellyfin-config:

```
