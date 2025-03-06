# Github CLI (gh)

```sh
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

Just add Github fingerprint to known hosts this way:
```sh
mkdir -p ~/.ssh
ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts
```


Change visibility to private, public, internal
```sh
gh repo edit --visibility <visibility-string>
```
Where visibility-string = private,public or internal



### Delete all releases from github

```sh
gh release list | sed 's/|/ /' | awk '{print $1, $8}' | while read -r line; do gh release delete -y "$line"; done
```
- gh release list gets a list of releases as a table.
- sed 's/|/ /' | awk '{print $1, $8}' singles out the first column provided by the table.
- while read -r line; do gh release delete -y "$line"; done ran the delete command for each result.

After deleting all of the releases I had to also get rid of all the tags. This command did that for me.

```sh
git fetch
git tag -l | xargs -n 1 git push --delete origin
```

Reference :
1. https://dev.to/dakdevs/delete-all-releases-from-github-repo-13ad
