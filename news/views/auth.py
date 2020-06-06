"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View


class RegisterView(View):
    templatename = 'auth/register.html'

    def get(self, request):
        return render(request, self.templatename)

    def post(self, request: HttpRequest):
        if request.POST.get('password') != request.POST.get('password_second'):
            messages.error(request, 'Hasła nie są identyczne :P')
            return redirect('register')

        username: str = request.POST.get('username')
        email: str = request.POST.get('email')
        password: str = request.POST.get('password')

        User.objects.create_user(username=username, email=email, password=password)

        messages.success(request, f'Użytkownik {username} został utworzony.')
        return redirect('register')
