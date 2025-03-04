# PIP 

Virtual Environment


```
python -m venv .venv
mkdir app
cd app
source ../.venv/bin/activate
```

Check packages
```
pip freeze
pip freeze > requirements.txt
```

### Remove all packages in virtual environment
```
pip freeze | xargs pip uninstall -y
```

Deactivate
```
deactivate
```


### Local Packages 
local packages are stored in
```
~/.local/bin/
```


### $PYTHONPATH
## Pylint and Coc-Pyright do not need $PYTHONPATH PYTHONPATH
## can safely ignore this

PYTHONPATH is an environment variable which you can set to add additional directories
where python will look for modules and packages. e.g.:

# make python look in the foo subdirectory of your home directory for
# modules and packages 
```
export PYTHONPATH=${PYTHONPATH}:${HOME}/foo
```
