"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django.urls import path

from . import views

urlpatterns = [
    path("news", views.NewsList.as_view(), name="api_news_list"),
    path("news/create", views.NewNewsView.as_view(), name="api_new_news"),
    path("news/<pk>", views.NewsDetailView.as_view(), name="api_news_detail"),
]
