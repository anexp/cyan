To list global npm packages
```
npm -g list
```
To install a package globally say create-react-app
```
sudo npm i -g create-react-app
```
To uninstall a global package 
```
sudo npm uninstall -g create-react-app
```

Generally, not using **sudo** leads to errors as without it **npm** does not have enought permissions to perform installation

To use npm packages without installing them use **npx**, where the **x** stands for **execute**
for example
```
npx create-react-app my-app
```
