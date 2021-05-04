import React from 'react';
import {RelatedLinkDto} from '../dto/serializer';

const RelatedLinkList = ({links}: {links: RelatedLinkDto[]}) => {
  return (
    <ul>
      {
        links.map((link) => (
          <li key={link.id}>
            <a href={link.link}>{link.name}</a>
          </li>
        ))
      }
    </ul>
  );
};

export default RelatedLinkList;
