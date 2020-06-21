"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button


class HorizontalFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(HorizontalFormHelper, self).__init__(*args, **kwargs)
        self.form_class = 'form-horizontal animated fadeIn'
        self.label_class = 'col-lg-4 text-lg-right'
        self.field_class = 'col-lg-8'

        # domyślna wartość, którą ustawiłem, żebyście o niej pamiętali ;)
        self.form_tag = True

    def add_submit(self, text='Zapisz', **kwargs):
        self.add_input(
            Submit('submit', text, css_class='btn btn-success', **kwargs)
        )

    def add_cancel(self, text='Cancel', **kwargs):
        self.add_input(
            Button('cancel', text, css_class='btn btn-primary', **kwargs)
        )
