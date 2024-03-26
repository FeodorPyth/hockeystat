from django.core.exceptions import ValidationError

from hockeystat.constants import URL_PATH_NAME


def validate_username_me(value):
    """
    Валидация поля username.
    Значение не должно быть равно 'me'.
    """
    if value == URL_PATH_NAME:
        raise ValidationError(f'Can not use {URL_PATH_NAME} as username')
    return value
