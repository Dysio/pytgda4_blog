"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from typing import List

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View

from news.forms.loginform import LoginForm
from news.forms.signupform import SignUpForm


class RegisterView(View):
    template_name: str = 'auth/register.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')

        return render(request, self.template_name, {'form': SignUpForm()})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Użytkownik {request.POST.get("username")} został utworzony.')

        return redirect('register')


class LoginView(View):
    template_name = 'auth/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')

        return render(request, self.template_name, {'form': LoginForm()})

    def post(self, request):
        username: str = request.POST.get('username')
        password: str = request.POST.get('password')

        user: User or None = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('index')

        messages.error(request, 'Nie znam takiego usera :P')
        return redirect('login')


def logout_view(request):
    logout(request)
    return redirect('index')