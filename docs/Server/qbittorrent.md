# qbittorrent

```
---
version: "2.1"
services:
  qbittorrent:
    image: lscr.io/linuxserver/qbittorrent:latest
    container_name: qbittorrent
    environment:
      - PUID=1000
      - PGID=1000
      # - TZ=Etc/UTC
      - TZ=Asia/Kolkata
      - WEBUI_PORT=8084
    volumes:
      - /srv/qbittorrent/config:/config
      - /srv/qbittorrent/downloads:/downloads
    ports:
      - 8084:8084
      - 6881:6881
      - 6881:6881/udp
    restart: unless-stopped
```



https://hub.docker.com/r/linuxserver/qbittorrent
