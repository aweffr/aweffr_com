import os
import logging
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.static import serve
from django.conf import settings
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Article, UploadedImage, StudySubject, Tweet
from .serializers import ArticleBaseSerializer, ArticleSerializer, StudySubjectSerializer, TweetSerializer

from rest_framework import viewsets, authentication, permissions

logger = logging.getLogger(__name__)


def index(request):
    articles = Article.objects.filter(is_published=True).order_by("-time_published").all()
    tweets = Tweet.objects.order_by("-create_at").all()

    serializer_article_list = ArticleBaseSerializer(articles, many=True)
    serializer_tweet_list = TweetSerializer(tweets, many=True)

    return render(request, "blog/index.html", context={
        "serializer_article_list_data": serializer_article_list.data,
        "serializer_tweet_list_data": serializer_tweet_list.data,
    })


def view_image(request, slug):
    image = get_object_or_404(UploadedImage, pk=slug)

    filepath = image.image.name
    if request.GET.get("size"):
        try:
            size = int(request.GET.get("size"))
            filepath = image.get_with_size(size)
        except:
            logger.exception("处理size参数出错")

    if settings.DEBUG:
        response = serve(request, filepath, document_root=settings.MEDIA_ROOT)
    else:
        response = HttpResponse("")
    response['X-Accel-Redirect'] = os.path.join(settings.MEDIA_URL, filepath)
    response['Content-Type'] = "image/jpeg"

    return response


def view_article_list(request):
    article_list = Article.objects.filter(type=Article.TYPE_ARTICLE).filter(is_published=True).order_by("-time_published").all()
    serializer = ArticleBaseSerializer(article_list, many=True)
    return render(request, "blog/article_list.html", context={
        "article_list_data": serializer.data,
    })


def view_article(request, slug):
    article: Article = get_object_or_404(Article, slug=slug)
    serializer = ArticleSerializer(article)

    return render(request, "blog/article.html", context={
        "article": article,
        "article_data": serializer.data,
    })


def view_study_subject_list(request):
    subject_list = StudySubject.objects.all()
    serializer = StudySubjectSerializer(subject_list, many=True)
    return render(request, "blog/study_subject_list.html", context={
        "subject_list": subject_list,
        "subject_list_data": serializer.data,
    })


def view_study(request, slug):
    return render(request, "blog/study.html")


def view_archive_list(request):
    archive_list = Article.objects.filter(type=Article.TYPE_ARCHIVE).filter(is_published=True).order_by("-time_published").all()
    serializer = ArticleBaseSerializer(archive_list, many=True)

    return render(request, "blog/archive_list.html", {
        "archive_list_data": serializer.data,
    })


def view_archive(request, slug):
    archive = get_object_or_404(Article, type=Article.TYPE_ARCHIVE, slug=slug)
    serializer = ArticleSerializer(archive)

    return render(request, "blog/archive.html", {
        "archive": archive,
        "archive_data": serializer.data,
    })


def view_todo_list(request):
    return render(request, "blog/todo_list.html")


def view_tweet_list(request):
    qs = Tweet.objects.get_queryset().select_related("user__profile")
    if not request.user.is_authenticated:
        qs = qs.filter(is_public=True)
    tweet_list = qs.all()
    serializer = TweetSerializer(tweet_list, many=True)
    return render(request, "blog/tweet_list.html", {
        "tweet_list": tweet_list,
        "tweet_list_data": serializer.data,
    })


def view_tool_list(request):
    return render(request, "blog/tool_list.html")


class ArchiveViewSet(viewsets.ModelViewSet):
    authentication_classes = (authentication.SessionAuthentication, authentication.BasicAuthentication)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Article.objects.filter(type=Article.TYPE_ARCHIVE).all()
    serializer_class = ArticleSerializer

    @action(methods=['POST', ], detail=False)
    def save_zhihu(self, request: Request, **kwargs):
        logger.debug("kwargs=%s", kwargs)
        html = request.data.get("html")
        logger.info("html=%s", html)

        return Response({'msg': 'OK'})
