# Nginx


Use nginx as a file server
```
    root /var/www/html;

         location /tr {

                 alias /var/lib/transmission-daemon/downloads;

                 # download
                 autoindex on;               # enable directory listing output
                 autoindex_exact_size off;   # output file sizes rounded to kilobytes, megabytes, and gigabytes
                 autoindex_localtime on;     # output local times in the directory
         }
```
