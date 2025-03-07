# Overleaf

:exclamation: Overleaf is not supported on ARM

Ref :
1. [Flexivola blog Overleaf Self host](https://blog.felixviola.de/overleaf-ce-self-host-your-own-latex-server-tutorial/)
2. Nginx reverse proxy : [https://github.com/overleaf/overleaf/wiki/HTTPS-reverse-proxy-using-Nginx](https://github.com/overleaf/overleaf/wiki/HTTPS-reverse-proxy-using-Nginx)

The nginx reverse proxy file specified helps traffic passing through wss:// web sockets, otherewise there is a large delay in loading projects and uploading of zip files don't work.

Clone
```sh
git clone https://github.com/overleaf/toolkit.git
cd toolkit
./bin/init
```

Edit ./config/overleaf.rc

Change
```
SHARELATEX_LISTEN_IP=127.0.0.1
SHARELATEX_PORT=80
```

to 
```
SHARELATEX_LISTEN_IP=0.0.0.0
SHARELATEX_PORT=8931
```

port can be whatever you like


You could also change ./config/variables.env
inside ./config/variables.env

Set the site url
```
SHARELATEX_SITE_URL=http://overleaf.example.com
```



Then build everything
```sh
./bin/up
```

If things have to started again
```sh
./bin/start
```

To create admin account go to  `overleaf_url/launchpad`


### Update TexLive (Installing extra packages)

Up front: The Update will take a lot of time! Once you entered the commands (which takes less than 5 mins) the update will take more than an hour – on my hardware it took about 1.5 hours. So make sure you got time for that!

First up, go into your Overleaf-docker-container. You must there for be in the overleaf-toolkit-folder we created in Step 2. From here you can execute the following command:
Make sure the containers are running
```sh
./bin/shell
```
Now that you are in the docker-container, you can download the tex-live update-script:

```sh
wget https://mirror.clientvps.com/CTAN/systems/texlive/tlnet/install-tl-unx.tar.gz
```

Next up: extract the folder and cd into it:
```sh
tar -xf install-tl-unx.tar.gz
cd install-tl-*
```

Now you can start the perl-installscript with:
```sh
perl install-tl
```

It might ask you, if you want to use previous configs, I just denied that. Next start the installation with i when it gives you the opportunity:
Use 'i' as command
```
Enter command: i
```
Now it will work and work and work, you will see that it is going to install over 4000 packages, so be patient.
