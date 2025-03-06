

### Create database

Docker Run
```sh
docker run -d -p 3401:3306 -e MYSQL_ROOT_PASSWORD=password  --name db1 --restart=always mysql:latest
```

### Connection

Error : Public Key retrieval is not allowed

https://stackoverflow.com/questions/50379839/connection-java-mysql-public-key-retrieval-is-not-allowed

For DBeaver users:

Right-click your connection, choose "Edit Connection"
On the "Connection settings" screen (main screen), click on "Edit Driver Settings"
Click on "Driver properties"

Set property: "allowPublicKeyRetrieval" to true


