import React from 'react';
import {ArticleBaseDto} from '../dto/serializer';
import {Container} from 'reactstrap';
import moment from 'moment';


const ArticleRow = ({article}: {article: ArticleBaseDto}) => {
  const m = moment(article.time_published);
  const timeDisplay = m.format('YYYY-MM-DD HH:mm');

  return (
    <div className="my-3 article-row">
      <h1 className="article-title">
        <a className="article-title-anchor" href={`/article/${article.slug}/`}>{article.title}</a>
      </h1>
      <div className="my-2 article-time">更新时间: {timeDisplay}</div>
      <div className="my-2" dangerouslySetInnerHTML={{__html: article.abstract_html}}/>
    </div>
  );
};

const ArticleList = () => {
  const data: ArticleBaseDto[] = JSON.parse(document.getElementById('article_list_data')!.innerText);

  return (
    <Container>
      {
        data.map((article) => (
          <ArticleRow key={article.id} article={article}/>
        ))
      }
    </Container>
  );
};

export default ArticleList;
