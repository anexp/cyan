# pdfjs

reference : https://mozilla.github.io/pdf.js/getting_started/

```sh

curl -LJO https://github.com/mozilla/pdf.js/releases/download/v3.9.179/pdfjs-3.9.179-dist.zip

unzip pdfjs-3.9.179-dist.zip -d pdfjs


```

Directory structure would like this

```
.
├── pdfjs
│   ├── LICENSE
│   ├── build
│   │   ├── pdf.js
│   │   ├── pdf.js.map
│   │   ├── pdf.sandbox.js
│   │   ├── pdf.sandbox.js.map
│   │   ├── pdf.worker.js
│   │   └── pdf.worker.js.map
│   └── web
│       ├── cmaps
│       ├── compressed.tracemonkey-pldi-09.pdf
│       ├── debugger.css
│       ├── debugger.js
│       ├── images
│       ├── locale
│       ├── standard_fonts
│       ├── viewer.css
│       ├── viewer.html
│       ├── viewer.js
│       └── viewer.js.map


```

always open **web/viewer.html**

and then pass file=path_to_file

file must be avaialable on the server

use **relative paths**

example url
```
https://domain.tld/pdfjs/web/viewer.html?file=./../../Directory/file.pdf
```
will open a file named file.pdf inside  Directory (which happens to be sibling of pdfjs directory)
