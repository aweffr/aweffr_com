import React from 'react';
import {ArticleDto} from "../interfaces/article";
import {Container} from "reactstrap";

const Article = () => {
  const data: ArticleDto = JSON.parse(document.getElementById("article_data")!.innerText);

  return (
    <Container fluid>
      <main className="my-3" dangerouslySetInnerHTML={{__html: data.content_html}}/>
    </Container>
  );
};

export default Article;
