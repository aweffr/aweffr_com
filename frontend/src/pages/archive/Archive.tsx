import React from 'react';
import {ArticleDto} from '../../dto/serializer';
import {Container} from 'reactstrap';
import RelatedLinkList from '../../components/RelatedLinkList';

const Archive = () => {
  const data: ArticleDto = JSON.parse(document.getElementById('archive_data')!.innerText);

  return (
    <Container className="mb-5">
      <main className="my-3" dangerouslySetInnerHTML={{__html: data.content_html}}/>
      {
        data.related_links.length > 0 && (
          <div>
            <h2>参考链接</h2>
            <RelatedLinkList links={data.related_links}/>
          </div>
        )
      }
    </Container>
  );
};

export default Archive;
