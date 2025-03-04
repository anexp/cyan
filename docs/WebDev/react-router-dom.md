# React Router Dom



react-router-dom@6

install 
```js
npm i react-router-dom
```

sample

```js

import {Routes, Route, BrowserRouter} from "react-router-dom"


const App = ()=>{
  return (
    <BrowserRouter>
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/about" element={<About/>} />
      <Route path="/dynamic/a" element={<Dynamic name="a"/>} />
    </Routes>
    </BrowserRouter>

  )
}

export default App

```

dynamic

```js


``
