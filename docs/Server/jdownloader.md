# jdownloader

```docker
version: '2'
services:
  jdownloader-2:
    image: docker.io/jlesage/jdownloader-2
    restart: always
    ports:
      - "5800:5800"
    volumes:
      - "/srv/jdownloader-2/config:/config:rw"
      - "/srv/jdownloader-2/output:/output:rw"

```

https://github.com/jlesage/docker-jdownloader-2
