from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("archives", views.ArchiveViewSet)

urlpatterns = [
    path("", views.index),

    path("article/<str:slug>/", views.view_article),
    path("article/", views.view_article_list),

    path("study/<str:slug>/", views.view_study),
    path("study/", views.view_study_subject_list),

    path("archive/<str:slug>/", views.view_archive),
    path("archive/", views.view_archive_list),

    path("todo/", views.view_todo_list),
    path("tweet/", views.view_tweet_list),
    path("tool/", views.view_tool_list),

    path("image/<str:slug>/", views.view_image, name="view_image"),

    path("api/", include(router.urls))
]
