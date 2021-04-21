import React from 'react';
import {ArticleBaseDto} from "../interfaces/article";
import {Container, Card} from "reactstrap";


const Article = ({article}: {article: ArticleBaseDto}) => {
  return (
    <div className="my-3">
      <h1 className="article-title">
        <a className="article-title-anchor" href={`/article/${article.slug}/`}>{article.title}</a>
      </h1>
    </div>
  )
}

const ArticleList = () => {
  const data: ArticleBaseDto[] = JSON.parse(document.getElementById("article_list_data")!.innerText);

  return (
    <Container fluid>
      {
        data.map(article => (
          <Article key={article.id} article={article}/>
        ))
      }
    </Container>
  );
};

export default ArticleList;
