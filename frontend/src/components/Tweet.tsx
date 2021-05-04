import React from 'react';
import {TweetDto} from '../dto/serializer';
import moment from 'moment';
import {debugMode} from '../constants';
// import _ from 'lodash';


const Tweet = ({tweet}: {tweet: TweetDto}) => {
  return (
    <div className="tweet">
      <div className="tweet-avatar-container">
        <img src={tweet.user_avatar.url} alt="avatar"/>
      </div>
      <div className="tweet-content-container">
        <div style={{display: 'flex'}}>
          <div>{tweet.username}</div>
          <div className="ml-2">{moment(tweet.create_at).format('YYYY-MM-DD HH:mm:ss')}</div>
        </div>
        <div className="mt-2">
          <div className="tweet-content" dangerouslySetInnerHTML={{__html: tweet.text_html}}/>
        </div>
        {
          tweet.image && (
            <div className="tweet-image">
              <img src={tweet.image.url} alt={tweet.image.title}/>
            </div>
          )
        }
        <div className="tweet-toolbar"/>
        {
          debugMode && (
            <div style={{display: 'none'}}>
              <pre>
                {JSON.stringify(tweet, null, 2)}
              </pre>
            </div>
          )
        }
      </div>
    </div>
  );
};

export default Tweet;
