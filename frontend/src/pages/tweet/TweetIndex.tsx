import React from 'react';
import {TweetDto} from '../../dto/serializer';
import {debugMode} from '../../constants';
import moment from 'moment';

const Tweet = ({tweet}: {tweet: TweetDto}) => {
  return (
    <div>
      <div>Avatar</div>
      <div>
        <div>
          <div>aweffr</div>
          <div>{moment(tweet.create_at).format('YYYY-MM-DD HH:mm:ss')}</div>
        </div>
        <div>
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
    <div>
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

    </div>
  );
};

export default TweetIndex;
