import React from 'react';
import MyNavbar from './components/MyNavbar';
import ArticleList from './pages/ArticleList';
import Article from './pages/Article';

function App() {
  let Component: any = () => null;
  if (window.location.pathname.endsWith('/article/')) {
    Component = ArticleList;
  } else if (window.location.pathname.includes('/article/')) {
    Component = Article;
  }
  return (
    <div className="App">
      <MyNavbar/>
      <Component/>
    </div>
  );
}

export default App;
