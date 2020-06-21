"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View


class MainView(View):
    template = 'hello.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('news_list'))
        return render(request, self.template)

    def post(self, request):
        name: str = request.POST.get('name')
        return render(request, self.template, {'name': name})
