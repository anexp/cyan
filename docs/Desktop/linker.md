# Linker

Check folders being checked
```sh
ldconfig -v | grep -v "^"$'\t' | sed "s/:$//g"
```

```sh
sudo ldconfig /usr/local/lib
```

Inside /etc/ld.so.conf.d/
Create a file /etc/ld.so.conf.d/usr-local-lib.conf
```
/usr/local/lib
```


Reference :-
1. https://unix.stackexchange.com/questions/67781/use-shared-libraries-in-usr-local-lib
2. [Check paths in ld linker checks](https://unix.stackexchange.com/questions/367600/what-is-the-order-that-linuxs-dynamic-linker-searches-paths-in)
