"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django import forms

from news.form_widgets import ListTextWidget
from news.forms.horizontalformhelper import HorizontalFormHelper
from news.models import News, Category


class NewsForm(forms.ModelForm):
    title = forms.CharField(
        label='Tytuł newsa',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg pr-4 shadow-none',
                'placeholder': 'Tytuł'
            }
        )
    )

    content = forms.CharField(
        label='Treść newsa',
        widget=forms.Textarea(
            attrs={'class': 'form-control form-control-lg pr-4 shadow-none', }
        )
    )

    category = forms.CharField(
        label='Kategoria',
        widget=ListTextWidget(
            name="category",
            data_list=Category.objects.all(),
            attrs={'class': 'form-control form-control-lg pr-4 shadow-none', }
        )
    )

    def clean_category(self):
        return Category.objects.get_or_create(
            name=self.cleaned_data.get('category')
        )[0]

    class Meta:
        model = News
        fields = ('title', 'content', 'category')

    def __init__(self, *args, **kwargs):
        self.helper = HorizontalFormHelper()
        super(NewsForm, self).__init__(*args, **kwargs)

        self.helper.add_submit("Dodaj post")
        self.helper.add_cancel("Anuluj")
