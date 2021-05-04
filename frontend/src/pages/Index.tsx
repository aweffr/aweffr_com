import React from 'react';
import {ArticleBaseDto, TweetDto} from '../dto/serializer';
import {ArticleType} from '../dto/article-types';
import _ from 'lodash';
import ArticleRow from '../components/ArticleRow';
import Tweet from '../components/Tweet';
import {Container} from 'reactstrap';

const Index = () => {
  const articles: ArticleBaseDto[] = JSON.parse(document.getElementById('serializer_article_list_data')!.innerText);
  const tweets: TweetDto[] = JSON.parse(document.getElementById('serializer_tweet_list_data')!.innerText);
  let items: {type: 'article' | 'archive' | 'tweet', item: ArticleBaseDto | TweetDto, time: string}[] = [];
  articles.forEach((a) => {
    if (a.type === ArticleType.ARTICLE) {
      items.push({
        type: 'article',
        item: a,
        time: a.time_published as string,
      });
    } else if (a.type === ArticleType.ARCHIVE) {
      items.push({
        type: 'archive',
        item: a,
        time: a.time_published as string,
      });
    }
  });
  tweets.forEach((t) => {
    items.push({
      type: 'tweet',
      item: t,
      time: t.create_at as string,
    });
  });

  items = _.sortBy(items, 'time');
  items.reverse();

  return (
    <Container>
      {
        items.map((item) => {
          if (item.type === 'article') {
            return (
              <ArticleRow article={item.item as ArticleBaseDto}/>
            );
          } else if (item.type === 'archive') {
            return (
              <ArticleRow article={item.item as ArticleBaseDto}/>
            );
          } else {
            return <Tweet tweet={item.item as TweetDto}/>;
          }
        })
      }
    </Container>
  );
};

export default Index;
