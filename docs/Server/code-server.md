# Vs Code Server

Ref:-
1. [linuxserver.io](https://github.com/linuxserver/docker-code-server)

My
```docker-compose
---
version: "2.1"
services:
  code-server:
    image: lscr.io/linuxserver/code-server:latest
    container_name: code-server
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Asia/Kolkata
      - PASSWORD=password #optional
      # - HASHED_PASSWORD= #optional
      - SUDO_PASSWORD=password #optional
      # - SUDO_PASSWORD_HASH= #optional
      - PROXY_DOMAIN=code-server.domain.tld #optional
      # - DEFAULT_WORKSPACE=/config/workspace #optional
    volumes:
      - /srv/code-server/config:/config
    ports:
      - 8443:8443
    restart: unless-stopped
```



Default
```docker-compose
---
version: "2.1"
services:
  code-server:
    image: lscr.io/linuxserver/code-server:latest
    container_name: code-server
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
      - PASSWORD=password #optional
      - HASHED_PASSWORD= #optional
      - SUDO_PASSWORD=password #optional
      - SUDO_PASSWORD_HASH= #optional
      - PROXY_DOMAIN=code-server.my.domain #optional
      - DEFAULT_WORKSPACE=/config/workspace #optional
    volumes:
      - /path/to/appdata/config:/config
    ports:
      - 8443:8443
    restart: unless-stopped
```

