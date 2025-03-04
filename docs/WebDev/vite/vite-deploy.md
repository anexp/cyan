# Deploying Vite / React App to GitHub Pages


Just follow these simple steps:

1. Install the gh-pages package (ctrl+~ to open the terminal in VS Code)
```
npm install gh-pages --save-dev
```
2. In the package.json file add these lines to scrips
```
"predeploy": "npm run build",
"deploy": "gh-pages -d dist",
```
3. In the vite.config.js file add this line before plugins: [react()],
```
base: "/YOUR_REPOSITORY_NAME",
```
Change YOUR_REPOSITORY_NAME to the name of your GitHub repository.

4. In terminal type
```
npm run deploy
```
🎉 You now have a gh-pages branch in your repository and your app is deployed (you can check it under Settings -> Pages )

P.S. To update your app deployment, just run the **npm run deploy** command again.



### Reference
- [dev.to link](https://dev.to/rashidshamloo/deploying-vite-react-app-to-github-pages-35hf)
