# Curl

Ref :-

1. [Broken Download](https://www.cyberciti.biz/faq/curl-command-resume-broken-download/)

Continue broken download
Without specifying filename
```sh
 curl -L -O -C - "https://iso.pop-os.org/22.04/amd64/nvidia/34/pop-os_22.04_amd64_nvidia_34.iso"
```

With retry
```sh
curl -L -O --retry 999 --retry-max-time 0 -C - "http://url"
```

If you want to specify filename
```sh
curl -C - -o lfw.tgz "http://vis-www.cs.umass.edu/lfw/lfw.tgz"
```
