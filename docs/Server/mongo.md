# MongoDB


docker installation
https://www.mongodb.com/docs/manual/tutorial/install-mongodb-community-with-docker/

```sh
docker run --name mongo -d mongodb/mongodb-community-server:7.0.1-ubuntu2204
```

### Raspberry pi

https://github.com/themattman/mongodb-raspberrypi-binaries
https://github.com/themattman/mongodb-raspberrypi-docker

Download the tarball via browser or copying the link to a terminal session
```sh
wget https://github.com/themattman/mongodb-raspberrypi-docker/releases/download/r7.0.4-mongodb-raspberrypi-docker-unofficial/mongodb.ce.pi4.r7.0.4-mongodb-raspberrypi-docker-unofficial.tar.gz
```

Load the release
```sh
docker load --input mongodb.ce.pi4.r7.0.4-mongodb-raspberrypi-docker-unofficial.tar.gz
```
```
Loaded image: mongodb-raspberrypi4-unofficial-r7.0.4:latest
```

(Optional) Verify the Docker image has been loaded
```sh
docker images
```

Run the image
```sh
docker run --name mongo -d mongodb-raspberrypi4-unofficial-r7.0.4
```

```docker-compose
version: '3.0'
services:
  mongo1:
    image: 'mongodb-raspberrypi4-unofficial-r7.0.4'
    restart: always
    ports:
    - '21001:27017'
```


Additional commands
```sh
# Using wget assumes network connection. Can also copy with USB.
mkdir ~/mdb-binaries && cd ~/mdb-binaries
wget https://github.com/themattman/mongodb-raspberrypi-binaries/releases/download/r7.0.5-rpi-unofficial/mongodb.ce.pi4.r7.0.5.tar.gz
tar xzvf mongodb.ce.pi4.r7.0.5.tar.gz # Decompress tarball

# Prepare MongoDB data & log directories
mkdir -p /data/db/test_db
touch /data/db/test_db/mongod.log
sudo chown -R ${USER}:${USER} /data

# Run & Configure MongoDB Standalone Local Server
./mongod --dbpath /data/db/test_db --fork --logpath /data/db/test_db/mongod.log --port 28080
./mongo --port 28080 # run queries!
```


### Run

Connect to mongodb deployment using mongosh
```sh
docker exec -it mongo mongosh
```

validate deployment by running `Hello` command
```mongo
db.runCommand(
   {
      hello: 1
   }
)
```
