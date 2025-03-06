# Rsync

Ref :-
1. [stackoverflow Copy files with particular extension](https://stackoverflow.com/questions/11111562/rsync-copy-over-only-certain-types-of-files-using-include-option#11111793)
2. [Man page](https://linux.die.net/man/1/rsync)


### Copy files with  a particular extension

--include is used to include a subset of files that are otherwise excluded by --exclude, rather than including only those files. In other words: you have to think about include meaning don't exclude.

```sh
rsync -zarv  --include "*/" --exclude="*" --include="*.sh" "$from" "$to"
```
For rsync version 3.0.6 or higher, the order needs to be modified as follows (see comments):
```sh
rsync -zarv --include="*/" --include="*.sh" --exclude="*" "$from" "$to"
```
Adding the **-m flag** will avoid creating empty directory structures in the destination. Tested in version 3.1.2.

So if we only want *.sh files we have to exclude all files --exclude="*", include all directories --include="*/" and include all *.sh files --include="*.sh".

### Broken download/ large files

use parital and append flags
```sh
rsynv -av --delete --partial --append  "path_from" "path_to"
```
