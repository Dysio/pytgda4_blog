"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView

from news.forms.loginform import LoginForm
from news.forms.signupform import SignUpForm


class UpdateUserView(UpdateView):
    template_name = 'updateuser.html'
    model = User
    fields = ('username', 'email')

    def get_success_url(self):
        return reverse('users')


class UsersView(ListView):
    template_name = 'users.html'
    model = User

    def get_queryset(self):
        return User.objects.filter(is_superuser=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UsersView, self).get_context_data(object_list=object_list, **kwargs)
        context.update({'bleble': 'cokolwiek'})
        return context


class RegisterView(CreateView):
    template_name: str = 'auth/register.html'
    form_class = SignUpForm

    def get_success_url(self):
        return reverse('index')


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


class ChangePasswordView(View, LoginRequiredMixin):
    login_url = '/login'
    template_name = 'auth/change_password.html'
    form_class = PasswordChangeForm

    def get(self, request):
        context = {'form': self.form_class(user=request.user)}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.user, request.POST)

        if form.is_valid():
            return self.form_valid(form)

        return self.form_invalid(form)

    def form_valid(self, form):
        messages.success(request=self.request, message="Hasło zmienione prawidłowo")
        return redirect(reverse('index'))

    def form_invalid(self, form):
        return render(self.request, self.template_name, {"form": form})


def logout_view(request):
    logout(request)
    return redirect('index')
