"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from news.views import MainView, RegisterView, LoginView, logout_view, UsersView, UpdateUserView, ChangePasswordView
from news.views.news_view import NewsListView, ShowNewsView, AddNewsView, SearchNewsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='index'),
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', logout_view, name='logout'),
    path('users', UsersView.as_view(), name='users'),
    path('users/<pk>/edit', UpdateUserView.as_view(), name='update_user'),
    path('change_password', ChangePasswordView.as_view(), name='change_password'),
    path('news', NewsListView.as_view(), name='news_list'),
    path('news/add', AddNewsView.as_view(), name='add_news'),
    path('news/search', SearchNewsView.as_view(), name='find_news'),
    path('news/<pk>', ShowNewsView.as_view(), name='show_news'),
]
