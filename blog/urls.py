from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("article/<str:slug>/", views.view_article),
    path("article/", views.view_article_list),
]
