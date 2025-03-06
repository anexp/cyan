# heimdall

```docker-compose
version: '3'
services:
  heimdall:
    image: docker.io/linuxserver/heimdall
    restart: unless-stopped
    # container_name: heimdall
    environment:
      - PUID=1000
      - PGID=1000
      # - TZ=america/new_york
      - TZ=asia/kolkata
      - APP_URL=https://heimdall.domain.tld
    ports:
      - "8908:80"
      - "8909:443"
    volumes:
      - /srv/heimdall/config:/config
      # - heimdall:/config
volumes:
  heimdall:
```

docker cli
```sh
docker run -d \
  --name heimdall \
  --restart unless-stopped \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=asia/kolkata \
  -e APP_URL=https://heimdall.domain.tld \
  -p 8908:80 \
  -p 8909:443 \
  -v heimdall:/config \
  docker.io/linuxserver/heimdall
```
