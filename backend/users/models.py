from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

from hockeystat.constants import LENGTH_FOR_EMAIL, LENGTH_FOR_USERNAME
from .validators import validate_username_me


class User(AbstractUser):
    """Кастомная модель пользователей."""
    username_validator = UnicodeUsernameValidator()

    email = models.EmailField(
        max_length=LENGTH_FOR_EMAIL,
        unique=True,
        verbose_name='E-mail address'
    )
    username = models.CharField(
        max_length=LENGTH_FOR_USERNAME,
        blank=True,
        unique=True,
        help_text=(
            'Required field. 150 characters or less.'
            'Only letters, numbers and @/./+/-/_.'
        ),
        validators=[username_validator, validate_username_me],
        verbose_name='Username',
    )
    avatar = models.ImageField(
        upload_to='media/avatars/',
        blank=True,
        verbose_name='Photo',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
        'first_name',
        'last_name',
        'password'
    ]

    class Meta:
        ordering = ('username',)
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        constraints = [
            models.UniqueConstraint(
                fields=['email', 'username'],
                name='unique_email_and_username'
            )
        ]

    def __str__(self):
        return self.username
