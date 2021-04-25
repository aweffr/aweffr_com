from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Article, RelatedLink, UploadedFile, UploadedImage, StudySubject
from django_typomatic import ts_interface


@ts_interface()
class UploadedFileSerializer(ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = "__all__"


@ts_interface()
class UploadedImageSerializer(ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = "__all__"


@ts_interface()
class RelatedLinkSerializer(ModelSerializer):
    class Meta:
        model = RelatedLink
        fields = "__all__"


@ts_interface()
class ArticleBaseSerializer(ModelSerializer):
    abstract_html = serializers.CharField()
    media_img = UploadedImageSerializer(allow_null=True)

    class Meta:
        model = Article
        fields = ("id", "title", "slug", "abstract_html", "time_published", "media_img")


@ts_interface()
class ArticleSerializer(ModelSerializer):
    abstract_html = serializers.CharField()
    content_html = serializers.CharField()
    media_img = UploadedImageSerializer(allow_null=True)

    related_links = RelatedLinkSerializer(many=True)
    related_files = UploadedFileSerializer(many=True)

    class Meta:
        model = Article
        fields = '__all__'


@ts_interface()
class StudySubjectSerializer(ModelSerializer):
    image = UploadedImageSerializer(allow_null=True)

    related_links = RelatedLinkSerializer(many=True)
    related_files = UploadedFileSerializer(many=True)

    detail_html = serializers.CharField(read_only=True)
    review_html = serializers.CharField(read_only=True)

    class Meta:
        model = StudySubject
        fields = '__all__'
