import {ArticleBaseDto} from '../dto/serializer';
import moment from 'moment';
import React from 'react';
import {ArticleType} from '../dto/article-types';

const ArticleRow = ({article}: {article: ArticleBaseDto}) => {
  const m = moment(article.time_published);
  const timeDisplay = m.format('YYYY-MM-DD HH:mm');
  const type = article.type as ArticleType;

  let href: string;
  let timeDesc: string;
  if (type === ArticleType.ARTICLE) {
    timeDesc = '更新时间';
    href = `/article/${article.slug}/`;
  } else if (type === ArticleType.ARCHIVE) {
    timeDesc = '转载时间';
    href = `/archive/${article.slug}/`;
  } else {
    throw new Error('not supported');
  }


  return (
    <div className="my-3 article-row">
      <h1 className="article-title">
        <a className="article-title-anchor" href={href}>{article.title}</a>
      </h1>
      <div className="my-3 article-time">{timeDesc}: {timeDisplay}</div>
      <div className="my-2" dangerouslySetInnerHTML={{__html: article.abstract_html}}/>
    </div>
  );
};

export default ArticleRow;
