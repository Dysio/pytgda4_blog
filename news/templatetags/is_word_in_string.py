"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""

from django import template

register = template.Library()


@register.filter
def is_word_in_string(value: str, words_list: str) -> bool:
    return any([word in value for word in words_list.split(',')])
