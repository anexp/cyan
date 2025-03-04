# Pylint


Install pylint
```
python -m pip install --user --upgrade pylint
```

warning shown during installation
```
WARNING: The scripts epylint, pylint, pylint-config, pyreverse and symilar are installed in '/home/darklord/.local/bin' which is not on PATH.
Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed pylint-2.15.10
```

if pylint is not in path
then  following error wil be shown on nvim startup
```
uncaught exception spawn pylint ENOENT
```

to add pylint to path do
```
export PATH=$PATH:/home/darklord/.local/bin/pylint
```

or more generally
```
export PATH=$PATH:/path/to/pylint/executable
```

to make changes permanent add this to **.bashrc**


### PYLINTRC  .pylinrc

```
python -m pylint --generate-rcfile > /home/darklord/.pylintrc
```
or more generally

```
python -m pylint --generate-rcfile > ${HOME}/.pylintrc
```



