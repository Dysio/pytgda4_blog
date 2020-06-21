"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""

from django import forms


class ListTextWidget(forms.TextInput):
    def __init__(self, name, data_list, model_object=None,  *args, **kwargs):
        super(ListTextWidget, self).__init__(*args, **kwargs)
        self._name = name
        self._list = data_list
        self._model_object = model_object

        self.attrs.update({'list': 'list_%s' % self._name})

    def render(self, name, value, attrs=None, renderer=None):
        # Przyda się do edycji (w naszym przypadku newsa)
        if self._model_object:
            try:
                value = self._model_object.objects.get(id=value)
            except self._model_object.DoesNotExist:
                pass

        # tu jest generowane pole input typu text z klasy TextInput
        text_html = super(ListTextWidget, self).render(name, value, attrs=attrs, renderer=renderer)

        text_html += '<datalist id="list_%s">' % self._name

        for item in self._list:
            text_html += f'<option value="{item}">'

        text_html += '</datalist>'

        return text_html

        # return text_html + '<datalist id="list_%s">' % self._name + ''.join(
        #     ['<option value="%s">' % item for item in self._list]) + '</datalist>'
