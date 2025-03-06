# GNU C Compiler (gcc)


### Static vs Dynamic binding
Ref : 
1. https://stackoverflow.com/questions/6578484/telling-gcc-directly-to-link-a-library-statically


To link your program with lib1, lib3 dynamically and lib2 statically, use such gcc call:
```sh
gcc program.o -llib1 -Wl,-Bstatic -llib2 -Wl,-Bdynamic -llib3
```
Assuming that default setting of ld is to use dynamic libraries (it is on Linux).
