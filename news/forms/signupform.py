"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from news.forms.horizontalformhelper import HorizontalFormHelper


class SignUpForm(UserCreationForm):
    username = UsernameField(
        label='Nazwa użytkownika',
        widget=forms.TextInput(
            attrs={'autofocus': True, 'class': 'form-control form-control-lg pr-4 shadow-none',
                   'placeholder': 'Nazwa użytkownika'},
        )
    )
    email = forms.EmailField(
        max_length=254, label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg pr-4 shadow-none'})
    )
    password1 = forms.CharField(
        label='Hasło',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg pr-4 shadow-none'}),
    )
    password2 = forms.CharField(
        strip=False, label='Hasło 2',
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg pr-4 shadow-none'}),
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Hasła nie są identyczne', code='password_mismatch')

        return password2

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        self.helper = HorizontalFormHelper()
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.helper.add_submit("zarejestruj")

