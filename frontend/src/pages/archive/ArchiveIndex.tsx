import React from 'react';
import ArticleRow from '../../components/ArticleRow';
import {ArticleBaseDto} from '../../dto/serializer';
import {Container} from 'reactstrap';
import {ArticleType} from '../../dto/article-types';


const ArchiveIndex = () => {
  const archives: ArticleBaseDto[] = JSON.parse(window.document.getElementById('archive_list_data')!.innerText);
  return (
    <Container>
      {
        archives.map((archive)=>(
          <ArticleRow key={archive.id} article={archive}/>
        ))
      }
    </Container>
  );
};

export default ArchiveIndex;
