# tar 


To create compressed archive
```
tar czpf binaries.tar.gz --preserve-permissions binaries/
```

To extract the contents of the archive
```
tar xzf binaries.tar.gz -C "$srcdir/binaries"
```

#### Permissions

By default, when you create a tar archive using the czf options, the permissions and ownership of the files and directories are preserved, including the executable permission. When you extract the archive using the xzf options, the permissions and ownership of the files and directories are also preserved.

So, if a file is executable before it is compressed using tar, it will retain its executable permission when it is extracted from the archive.

However, if you want to ensure that the permissions and ownership of the files and directories are preserved when you create the archive, you can use the -p or --preserve-permissions option with tar czf command. This will preserve the permissions, ownership, and timestamps of the files and directories in the archive.

