# Searxng


```sh
docker run -d \
  --name searxng \
  --restart unless-stopped \
  -p 8910:8080 \
  -v /srv/searxng/etc:/etc/searxng \
  -e BASE_URL=https://searxng.domain.tld \
  -e INSTANCE_NAME="Searxng Local" \
  docker.io/searxng/searxng
```

```docker-compose
version: '3'
services:
  searxng:
    image: docker.io/searxng/searxng
    restart: unless-stopped
    # container_name: searxng-docker
    ports:
      - "8910:8080"
    volumes:
      - /srv/searxng/etc:/etc/searxng
    environment:
      - BASE_URL=https://searxng.domain.tld
      - INSTANCE_NAME=Searxng Local
```
