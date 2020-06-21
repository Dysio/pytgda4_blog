"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django import forms

from news.models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'content', 'category')
