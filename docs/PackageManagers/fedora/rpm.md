# rpm


Set up environment

```sh
sudo dnf install fedora-packager fedora-reviewer @development-tools
sudo dnf install rpmdevtools


echo "%_topdir  $HOME/rpmbuild" > ~/.rpmmacros

rpmdev-setuptree
```


Package the source code as tarball and store it in SOURCES
Say, the source code is only hello.c then 

```sh
mkdir hello-0.0.1
cat <<EOF > hello-0.0.1/hello.c
#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}
EOF

tar -czvf hello-0.0.1.tar.gz hello-0.0.1
cp hello-0.0.1.tar.gz ~/rpmbuild/SOURCES
```

Make sure hello-0.0.1.tar.gz is in ~/rpmbuild/SOURCES

Put the spec file in the SPECS directory 

then run 

```sh
cd ~/rpmbuild/SPECS
rpmbuild -ba hello.spec
```


### References

- [CentOS youtube channel]https://youtu.be/CTTbu_q2xiQ
- [Debug error](https://superuser.com/questions/1091529/rpm-build-error-empty-files-file-debugfiles-list)

