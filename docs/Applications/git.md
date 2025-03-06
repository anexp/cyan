# Git


To make changes in .gitignore take effect
```
git rm -rf --cached .
```
and then add and commit changes


To set nvim as the editor to write commit messages for git
```
git config --global core.editor nvim
```

To see user.name and user.email
```
git config --global user.name
git config --global user.email
```

To set user.name and user.email
```
git config --global user.name "yourUserName"
git config --global user.email "you@example.com"
```


If you want to list all the files currently being tracked under the branch master, you could use this command:
```
git ls-tree -r master --name-only
```
If you want a list of files that ever existed (i.e. including deleted files):
```
git log --pretty=format: --name-only --diff-filter=A | sort - | sed '/^$/d'
```

Set upstream branch
```
$ git push
fatal: The current branch master has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin master
```


## Branch

### Rename
 If you want to rename a branch while pointed to any branch, do:
```sh
git branch -m <oldname> <newname>
```
If you want to rename the current branch, you can do:
```sh
git branch -m <newname>
```

### Pull all branches from remote repository

```sh
git fetch --all
```
### Merge

Merge branch B (dev) into branch A (main)
```sh
git merge dev main
```

or, if you are already have main branch checked out
```sh
git merge dev
```



## Rebase

[StacKOverflow](https://stackoverflow.com/questions/750172/how-do-i-change-the-author-and-committer-name-email-for-multiple-commits#1320317)


Rebase entire project

```sh
git rebase -r --root --exec "git commit --amend --no-edit --reset-author"
```

Rebse upto a sepecific commit
```sh
git rebase -r commit_hash --exec "git commit --amend --no-edit --reset-author"
```

Most recent commit
```sh
git commit --amend --no-edit --reset-author
```

## Tags

List tags
```sh
git tag
```

Details of Specific tag
```sh
git show v1.0.0
```

Create
```sh
git tag v1.0.1
```

Delete tag
```sh
git tag -d v1.0.1
```

Pushing to remote
```sh
git push origin v1.0.2
```

Delete remote tag
```sh
git push origin -d v1.0.2
```


## Submodule

#### ref
- [stackoverflow](https://stackoverflow.com/questions/1030169/pull-latest-changes-for-all-git-submodules#1032653)
- https://stackoverflow.com/questions/1777854/how-can-i-specify-a-branch-tag-when-adding-a-git-submodule
- https://stackoverflow.com/questions/10914022/how-do-i-check-out-a-specific-version-of-a-submodule-using-git-submodule

If it's the first time you check-out a repo you need to use --init first:
```sh
git submodule update --init --recursive
```
For git 1.8.2 or above, the option --remote was added to support updating to latest tips of remote branches:
```sh
git submodule update --recursive --remote
```
This has the added benefit of respecting any "non default" branches specified in the .gitmodules or .git/config files (if you happen to have any, default is origin/master, in which case some of the other answers here would work as well).

For git 1.7.3 or above you can use (but the below gotchas around what update does still apply):
```sh
git submodule update --recursive
```
or:
```sh
git pull --recurse-submodules
```
if you want to pull your submodules to latest commits instead of the current commit the repo points to.


##### Submodule add fail

https://stackoverflow.com/questions/20929336/git-submodule-add-a-git-directory-is-found-locally-issue



I came to this SO post trying to add a submodule with the same path as a submodule that I recently deleted.

This is what ultimately worked for me (this article helped out a lot):

If you haven't already run
git rm --cached path_to_submodule (no trailing slash) as well as
rm -rf path_to_submodule

Then:

    Delete the relevant lines from the .gitmodules file. e.g. delete these:

[submodule "path_to_submodule"]
        path = path_to_submodule
        url = https://github.com/path_to_submodule

    Delete the relevant section from .git/config. e.g. delete these:

[submodule "path_to_submodule"]
        url = https://github.com/path_to_submodule

    rm -rf .git/modules/path_to_submodule

Then, you can finally:

git submodule add https://github.com/path_to_submodule



## Tricks

Remove a particular file from githistory
```sh
git filter-branch --index-filter "git rm -rf --cached --ignore-unmatch path_to_file" <branch_name>
```
Found it here https://myopswork.com/how-remove-files-completely-from-git-repository-history-47ed3e0c4c35



### Change email id and name
```sh
git filter-branch --env-filter '
OLD_EMAIL="old_email@example.com"
CORRECT_NAME="Your Correct Name"
CORRECT_EMAIL="correct_email@example.com"
if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]; then
    export GIT_COMMITTER_NAME="$CORRECT_NAME"
    export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]; then
    export GIT_AUTHOR_NAME="$CORRECT_NAME"
    export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
fi
' --tag-name-filter cat -- --branches --tags
```


Set all commiters
```sh
git filter-branch --env-filter '
CORRECT_NAME="$(git config --global user.name)"
CORRECT_EMAIL="$(git config --global user.email)"
export GIT_COMMITTER_NAME="$CORRECT_NAME"
export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
export GIT_AUTHOR_NAME="$CORRECT_NAME"
export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
' --tag-name-filter cat -- --branches --tags

```


### Clone

```sh
git clone --depth 1 https://url.git
git fetch --unshallow
```


### Reset

Undoing a commit is a little scary if you don't know how it works. But it's actually amazingly easy if you do understand. I'll show you the 4 different ways you can undo a commit.

Say you have this, where C is your HEAD and (F) is the state of your files.
```
   (F)
A-B-C
    ↑
  master
```
##### Option 1:
```sh
git reset --hard
```
You want to destroy commit C and also throw away any uncommitted changes. You do this:
```sh
git reset --hard HEAD~1
```
The result is:
```
 (F)
A-B
  ↑
master
```
Now B is the HEAD. Because you used --hard, your files are reset to their state at commit B.
##### Option 2:
```sh
git reset
```
Maybe commit C wasn't a disaster, but just a bit off. You want to undo the commit but keep your changes for a bit of editing before you do a better commit. Starting again from here, with C as your HEAD:
```
   (F)
A-B-C
    ↑
  master
```
Do this, leaving off the --hard:
```sh
git reset HEAD~1
```
In this case the result is:
```
   (F)
A-B-C
  ↑
master
```
In both cases, HEAD is just a pointer to the latest commit. When you do a git reset HEAD~1, you tell Git to move the HEAD pointer back one commit. But (unless you use --hard) you leave your files as they were. So now git status shows the changes you had checked into C. You haven't lost a thing!
##### Option 3:
```sh
git reset --soft
```
For the lightest touch, you can even undo your commit but leave your files and your index:
```sh
git reset --soft HEAD~1
```
This not only leaves your files alone, it even leaves your index alone. When you do git status, you'll see that the same files are in the index as before. In fact, right after this command, you could do git commit and you'd be redoing the same commit you just had.
Option 4: you did git reset --hard and need to get that code back

One more thing: Suppose you destroy a commit as in the first example, but then discover you needed it after all? Tough luck, right?

Nope, there's still a way to get it back. Type this
```sh
git reflog
```
and you'll see a list of (partial) commit SHAs (that is, hashes) that you've moved around in. Find the commit you destroyed, and do this:
```sh
git checkout -b someNewBranchName shaYouDestroyed
```
You've now resurrected that commit. Commits don't actually get destroyed in Git for some 90 days, so you can usually go back and rescue one you didn't mean to get rid of.

In short
```sh
git reset --soft HEAD^     # Use --soft if you want to keep your changes
git reset --hard HEAD^     # Use --hard if you don't care about keeping the changes you made
```


Reference :
1. https://stackoverflow.com/questions/927358/how-do-i-undo-the-most-recent-local-commits-in-git
