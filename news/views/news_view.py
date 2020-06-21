"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from news.forms.newsform import NewsForm
from news.models import News


class NewsListView(LoginRequiredMixin, ListView):
    login_url = '/login'
    template_name = 'news/index.html'
    model = News

    def get_queryset(self):
        return self.model.objects.all()[:10]


class ShowNewsView(LoginRequiredMixin, DetailView):
    login_url = '/login'
    template_name = 'news/news.html'
    model = News

    def get_context_data(self, **kwargs):
        context = super(ShowNewsView, self).get_context_data(**kwargs)
        context.update({"tags": ", ".join([str(tag) for tag in self.get_object().tags.iterator()])})
        return context


class AddNewsView(LoginRequiredMixin, CreateView):
    login_url = '/login'
    template_name = 'news/add_news.html'
    form_class = NewsForm

    def get_success_url(self):
        return reverse('news_list')


class SearchNewsView(LoginRequiredMixin, View):
    login_url = '/login'
    template_name = 'news/index.html'

    def post(self, request):
        search_param: str = request.POST.get('search_param')

        if not search_param:
            messages.error(request, 'Podaj czego szukasz a nie się bawisz przyciskiem :P')
            return redirect(reverse('news_list'))

        news_list = News.objects.filter(
            title__contains=search_param,
            category__name__contains=search_param
        )

        return render(request, self.template_name, {"object_list": news_list})
