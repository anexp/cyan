# Ports

Which application is running at port 8080
```sh
ss -lptn 'sport = :8080'
```


Get active ports and process names
```sh
sudo ss -plunt
```
