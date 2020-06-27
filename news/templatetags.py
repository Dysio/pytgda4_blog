"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""

from django import template

register = template.Library()


@register.filter
def is_word_in_string(value: str, words_list: str) -> bool:
    # todo - zrobić z tego jednolinijkowca :P
    for word in words_list.split(','):
        if word in value:
            return True
    return False
