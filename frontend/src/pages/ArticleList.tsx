import React from 'react';
import {ArticleBaseDto} from '../dto/serializer';
import {Container} from 'reactstrap';
import ArticleRow from '../components/ArticleRow';
import {ArticleType} from '../dto/article-types';

const ArticleList = () => {
  const data: ArticleBaseDto[] = JSON.parse(document.getElementById('article_list_data')!.innerText);

  return (
    <Container className="mb-4">
      {
        data.map((article) => (
          <ArticleRow key={article.id} article={article}/>
        ))
      }
    </Container>
  );
};

export default ArticleList;
