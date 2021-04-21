from django.shortcuts import render, get_object_or_404

from .models import Article
from .serializers import ArticleBaseSerializer, ArticleSerializer


def index(request):
    return render(request, "blog/index.html", context={})


def view_article_list(request):
    article_list = Article.objects.filter(is_published=True).all()
    serializer = ArticleBaseSerializer(article_list, many=True)
    return render(request, "blog/article_list.html", context={
        "article_list_data": serializer.data,
    })


def view_article(request, slug):
    article: Article = get_object_or_404(Article, slug=slug)
    serializer = ArticleSerializer(article)

    return render(request, "blog/article.html", context={
        'article_data': serializer.data,
    })
