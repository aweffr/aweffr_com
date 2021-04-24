import React from 'react';
import {ArticleDto} from "../dto/serializer";
import {Container} from "reactstrap";


const Article = () => {
  const data: ArticleDto = JSON.parse(document.getElementById("article_data")!.innerText);

  return (
    <Container>
      <main className="my-3" dangerouslySetInnerHTML={{__html: data.content_html}}/>
      {
        data.related_links.length > 0 && (
          <div>
            <h2>参考链接</h2>
            <ul>
              {
                data.related_links.map(link => (
                  <li key={link.id}><a href={link.link}>{link.name}</a></li>
                ))
              }
            </ul>
          </div>
        )
      }
    </Container>
  );
};

export default Article;
