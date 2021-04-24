export interface UploadedFileDto {
    id?: number;
    slug: string;
    title?: string;
    file: any;
    create_at?: string;
}

export interface UploadedImageDto {
    id?: string;
    title?: string;
    image: any;
    width?: number | null;
    height?: number | null;
    create_at?: string;
}

export interface RelatedLinkDto {
    id?: number;
    name: string;
    link: string;
}

export interface ArticleBaseDto {
    id?: number;
    title: string;
    slug: string;
    abstract_html: string;
    time_published?: string | null;
    media_img: UploadedImageDto | null;
}

export interface ArticleDto {
    id?: number;
    abstract_html: string;
    content_html: string;
    media_img: UploadedImageDto | null;
    related_links: RelatedLinkDto[];
    related_files: UploadedFileDto[];
    title: string;
    slug: string;
    video_iframe?: string;
    type?: any;
    source?: any;
    is_published?: boolean;
    time_published?: string | null;
    time_modified?: string;
    abstract_markdown?: string;
    content_markdown: string;
}

