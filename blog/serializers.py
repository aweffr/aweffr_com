from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Article


class ArticleBaseSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ("id", "title", "slug", "time_published")


class ArticleSerializer(ModelSerializer):
    content_html = serializers.CharField()

    class Meta:
        model = Article
        fields = '__all__'
