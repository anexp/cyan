# Pyinstaller


#### Correct Method  works both in dev and production environment (Recommended)
```py
    def resource_path(self,relative_path:str)->str:
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
            # base_path = sys._MEIPASS2
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

```



#### Alternate Method : does not work properly in dev environment (Not Recommended)


All of the other answers use the current working directory in the case where the application is not PyInstalled (i.e. sys._MEIPASS is not set).
That is wrong, as it prevents you from running your application from a directory other than the one where your script is.


```py
    def resource_path(self,relative_path:str)->str:
        """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

```

####  Explore directory structure inside _MEIPASS



The most common complaint/question I've seen wrt PyInstaller is "my code can't find a data file which I definitely included in the bundle, where is it?", and it isn't easy to see what/where your code is searching because the extracted code is in a temp location and is removed when it exits. Add this bit of code to see what's included in your onefile and where it is, using @Jonathon Reinhart's resource_path()

```py
for root, dirs, files in os.walk(resource_path("")):
    print(root)
    for file in files:
        print( "  ",file)

```


Reference:
1. [Stack Overflow bundling-data-files-with-pyinstaller-onefile](https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile)
