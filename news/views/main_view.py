"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django.shortcuts import render
from django.views import View


class MainView(View):
    template = 'hello.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        name: str = request.POST.get('name')
        return render(request, self.template, {'name': name})
