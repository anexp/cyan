# Nextcloud - All in One


## Initial Setup

Reference :
1. (Github repo)(https://github.com/nextcloud/all-in-one]
2. (Github Reverse Proxy page)(https://github.com/nextcloud/all-in-one/blob/main/reverse-proxy.md]


Behind Reverse proxy
and preferably in VM/LXD container

Create folder for nextcloud mount
```sh
mkdir -pv /mnt/nextcloud_mount
```
```sh
sudo chown -R 33:0 /mnt/nextcloud_mount
sudo chmod -R 750 /mnt/nextcloud_mount
```

```sh
docker run \
--init \
--sig-proxy=false \
--name nextcloud-aio-mastercontainer \
--restart always \
--publish 8928:8080 \
--env APACHE_PORT=11000 \
--env APACHE_IP_BINDING=0.0.0.0 \
--env SKIP_DOMAIN_VALIDATION=true \
--env NEXTCLOUD_MOUNT="/mnt/nextcloud_mount/" \
--volume nextcloud_aio_mastercontainer:/mnt/docker-aio-config \
--volume /var/run/docker.sock:/var/run/docker.sock:ro \
docker.io/nextcloud/all-in-one:latest
```

i changed 8080:8080 to 8928:8080
port 8080 is for iniial setup (admin)
port 11000 is for normal usage



## External Storage
https://docs.nextcloud.com/server/latest/admin_manual/configuration_files/external_storage/local.html

```sh
sudo chown -R www-data:www-data /path/to/localdir
sudo chmod -R 0750 /path/to/localdir
```

Mount something here
```
/var/lib/docker/volumes/nextcloud_aio_nextcloud_data/_data/anirban
```


## OnlyOffice documnent server

```sh
docker run -i -t -d -p 8961:80 --restart=always docker.io/onlyoffice/documentserver
```

https://helpcenter.onlyoffice.com/installation/desktop-connect-nextcloud.aspx

## OnlyOffice full


Ref: https://www.youtube.com/watch?v=zSci6BcB3Q4

```sh
wget https://download.onlyoffice.com/install/workspace-install.sh
```

```sh
sudo bash workspace-install.sh -md "your_domain"
```

```sh
sudo bash workspace-install.sh -ids true -ics false -ims false -skipdc true -md "onlyoffice.hs2.local.kastrone.com"
```


Nginx

https://helpcenter.onlyoffice.com/installation/docs-community-proxy.aspx

https://github.com/ONLYOFFICE/document-server-proxy/blob/master/nginx/proxy-https-to-http.conf
