"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from news.forms.horizontalformhelper import HorizontalFormHelper
from news.models import Login

class LoginForm(AuthenticationForm):
    username = UsernameField(
        label='nazwa użytkownika',
        widget=forms.TextInput(
            attrs={'placeholder': 'Username', 'class': 'form-control form-control-lg pr-4 shadow-none'}
        )
    )

    password = forms.CharField(
        label='hasło',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Hasło', 'class': 'form-control form-control-lg pr-4 shadow-none'}
        )
    )

    error_messages = {
        'invalid_login': 'Nieprawidłowe hasło lub login',
        'inactive': 'Konto nieaktywne'
    }

    class Meta:
        model = Login
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        self.helper = HorizontalFormHelper()
        super(LoginForm, self).__init__(*args, **kwargs)

        self.helper.add_submit("zaloguj")
