import React from 'react';
import {StudySubjectDto} from '../../dto/serializer';
import {Container, Progress} from 'reactstrap';


const StudyIndex = () => {
  const subjects: StudySubjectDto[] = JSON.parse(window.document.getElementById('subject_list_data')!.innerText);
  return (
    <Container className="mb-4">
      {
        subjects.map((subject) => (
          <div className="study-subject-row" key={subject.id}>
            <h1>
              {subject.title}
            </h1>
            <div dangerouslySetInnerHTML={{__html: subject.detail_html!}}/>
            <div className="related-links">
              <h2 className="text-secondary">相关链接</h2>
              <ul>
                {
                  subject.related_links.map((link) => (
                    <li key={link.id}><a href={link.link}>{link.name || link.link}</a></li>
                  ))
                }
              </ul>
            </div>
            {
              subject.cnt_current > 0 && (
                <Progress value={Math.floor(100 * subject.cnt_current / subject.cnt_total)}/>
              )
            }
          </div>
        ))
      }
    </Container>
  );
};

export default StudyIndex;
