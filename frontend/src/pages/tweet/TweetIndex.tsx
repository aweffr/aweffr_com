import React from 'react';
import {TweetDto} from '../../dto/serializer';
import {Container} from 'reactstrap';
import Tweet from '../../components/Tweet';

const TweetIndex = () => {
  const data: TweetDto[] = JSON.parse(window.document.getElementById('tweet_list_data')!.innerText);

  return (
    <Container>
      {
        data.map((tweet) => <Tweet key={tweet.id} tweet={tweet}/>)
      }
    </Container>
  );
};

export default TweetIndex;
