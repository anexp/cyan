# AUR


Add a specific private key (aur_rsa) to the ssh-agent on your local machine
```
ssh-add ~/.ssh/aur_rsa
```

In case of Error,
Could not open a connection to your authentication agent.
```
eval "$(ssh-agent -s)"
```

For creating empty git repo 
```
git clone ssh://aur@aur.archlinux.org/openai-client-git.git

```

For generating .SRCINFO
```
makepkg --printsrcinfo > .SRCINFO
```


