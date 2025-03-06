# Conda


```sh
conda config --set auto_activate_base false
```

```sh
conda init --reverse $SHELL
```

if $SHELL is not specified then bash is selected by default
```sh
CONDA_PREFIX=$HOME/anaconda3 $HOME/anaconda3/bin/conda init $SHELL
```

Do not activate conda base environment
```sh
conda config --set auto_activate_base false
```

~/.condarc
```
auto_activate_base: false
```


Update conda

```sh
conda update -n base conda
```


Qt in conda
```sh
conda install qt-main qt-webengine
```

Disable telemetry

https://github.com/anaconda/anaconda-anon-usage
```sh
conda config --set anaconda_anon_usage off
```

~/.condarc
```
anaconda_anon_usage: false
```
