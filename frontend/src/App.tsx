import React from 'react';
import MyNavbar from './components/MyNavbar';
import ArticleList from './pages/ArticleList';
import Article from './pages/Article';
import StudyIndex from './pages/study/StudyIndex';
import TweetIndex from './pages/tweet/TweetIndex';
import ArchiveIndex from './pages/archive/ArchiveIndex';
import Archive from './pages/archive/Archive';
import Index from './pages/Index';

function App() {
  let Component: any = () => null;
  if (window.location.pathname.includes('/archive/')) {
    if (window.location.pathname.endsWith('/archive/')) {
      Component = ArchiveIndex;
    } else {
      Component = Archive;
    }
  } else if (window.location.pathname.endsWith('/article/')) {
    Component = ArticleList;
  } else if (window.location.pathname.includes('/article/')) {
    Component = Article;
  } else if (window.location.pathname.endsWith('/study/')) {
    Component = StudyIndex;
  } else if (window.location.pathname.endsWith('/tweet/')) {
    Component = TweetIndex;
  } else {
    Component = Index;
  }
  return (
    <div className="App">
      <MyNavbar/>
      <Component/>
    </div>
  );
}

export default App;
