export interface ArticleBaseDto {
  id: number;
  title: string;
  slug: string;
  time_published: string;
}

export interface ArticleDto {
  id: number;
  title: string;
  slug: string;
  is_published: boolean;
  time_published: string;
  time_modified: string;

  content_markdown: string;
  content_html: string;
}
