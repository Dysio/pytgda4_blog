"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def UsernameValidator(username: str):
    message = 'Nieprawidłowa nazwa użytkownika'

    if not (5 <= len(username) <= 20):
        raise ValidationError(message)

    if any([not i.isalnum() for i in username]):
        raise ValidationError(message)


# @deconstructible
# class UsernameValidator:
#     message = 'Nieprawidłowa nazwa użytkownika'
#
#     def __call__(self, username: str, *args, **kwargs):
#         if not (5 <= len(username) <= 20):
#             raise ValidationError(self.message)
#
#         # for i in username:
#         #     if not i.isalnum():
#         #         raise ValidationError(self.message)
#         #
#
#         if any([not i.isalnum() for i in username]):
#             raise ValidationError(self.message)
