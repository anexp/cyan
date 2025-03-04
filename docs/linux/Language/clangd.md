# clangd setup

```
sudo apt install clang
clang -v
```
To check the version of clangd compiler

You will find a version of g++ , gcc
say version 12

install that version of gcc/g++

```
sudo apt install g++-n
```
where 'n' is the version of g++ to be installed

https://gatowololo.github.io/blog/clangmissingheaders/

https://stackoverflow.com/questions/26333823/clang-doesnt-see-basic-headers


To set code formatting

To reset defaults 
```
cp ~/.clang-format ~/.clang-format-backup
rm ~/.clang-format
```

To get the current clang-format being used
```
# specify file 
# clang-format -dump-config <filename.cpp>

# or just use 
clang-format -dump-conf 
```

To copy defaults to ~/.clang-format
```
# specify file
# clang-format -dump-config <filename.cpp>  > ~/.clang-format

# or just use
clang-format -dump-config > ~/.clang-format
```

In my Arch 
I just set 
to get desired indentation
```
IndentWidth:     4
ObjCBlockIndentWidth: 4
```


### compile_commands

Inside CMakeLists.txt
```cmake
# For clangd lsp
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
```

Create .clangd at the root of the project
```
CompileFlags:
  CompilationDatabase: "../build-projectname-Desktop_Qt_6_5_3_GCC_64bit-Debug"
```


Reference
1. [generate compile_commands.json](https://gist.github.com/Strus/042a92a00070a943053006bf46912ae9)
1. [generate compile_commands.json reddit]https://www.reddit.com/r/neovim/comments/17rhvtl/guide_how_to_use_clangd_cc_lsp_in_any_project/)
