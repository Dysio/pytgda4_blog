from django import forms

from django.contrib.auth.forms import PasswordChangeForm
from news.forms.horizontalformhelper import HorizontalFormHelper
from django.contrib.auth.models import User


class PasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='stare hasło',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg pr-4 shadow-none'}),
    )

    new_password1 = forms.CharField(
        label='nowe hasło',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg pr-4 shadow-none'}),
    )

    new_password2 = forms.CharField(
        strip=False, label='potwierdź nowe hasło',
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg pr-4 shadow-none'}),
    )

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        self.helper = HorizontalFormHelper()
        super(PasswordForm, self).__init__(*args, **kwargs)

        self.helper.add_submit("zmień hasło")


