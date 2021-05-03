import React from 'react';
import {TweetDto} from '../../dto/serializer';
import {debugMode} from '../../constants';
import moment from 'moment';
import {Container} from 'reactstrap';

const Tweet = ({tweet}: {tweet: TweetDto}) => {
  return (
    <div className="my-3 tweet" style={{display: 'flex'}}>
      <div style={{width: '15%'}}>
        <img src={tweet.user_avatar.url} alt="avatar" style={{width: '100%', borderRadius: '50%'}}/>
      </div>
      <div className="ml-3">
        <div style={{display: 'flex'}}>
          <div>{tweet.username}</div>
          <div className="ml-2">{moment(tweet.create_at).format('YYYY-MM-DD HH:mm:ss')}</div>
        </div>
        <div className="mt-2">
          <div className="tweet-content" dangerouslySetInnerHTML={{__html: tweet.text_html}}/>
        </div>
        <div className="tweet-toolbar"/>
      </div>
    </div>
  );
};

const TweetIndex = () => {
  const data: TweetDto[] = JSON.parse(window.document.getElementById('tweet_list_data')!.innerText);

  return (
    <Container>
      {
        data.map((tweet) => <Tweet key={tweet.id} tweet={tweet}/>)
      }
      {
        debugMode && (
          <pre>
            {JSON.stringify(data, null, 2)}
          </pre>
        )
      }

    </Container>
  );
};

export default TweetIndex;
