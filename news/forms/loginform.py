"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class LoginForm(AuthenticationForm):
    username = UsernameField(
        label=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Username', 'class': 'form-control form-control-lg pr-4 shadow-none'}
        )
    )

    password = forms.CharField(
        label=False,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Hasło', 'class': 'form-control form-control-lg pr-4 shadow-none'}
        )
    )

    error_messages = {
        'invalid_login': 'Nieprawidłowe hasło lub login',
        'inactive': 'Konto nieaktywne'
    }
