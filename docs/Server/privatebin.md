# Private Bin


```docker-compose
version: '3'
services:
  privatebin:
    image: docker.io/privatebin/nginx-fpm-alpine
    container_name: privatebin
    restart: unless-stopped
    read_only: true
    ports:
      - "8913:8080"
    volumes:
      - privatebin-data:/srv/data

volumes:
  privatebin-data:
```
