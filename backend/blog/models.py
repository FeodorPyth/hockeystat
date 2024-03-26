from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class ProfileCart(models.Model):
    player_name = models.CharField(
        max_length=15,
        verbose_name='Player first name',
    )
    player_surname = models.CharField(
        max_length=20,
        verbose_name='Player last name',
    )
    player_age = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(
                16,
                message="Player's age must be greater than 16"
            ),
            MaxValueValidator(
                45,
                message="Player's age must be less than 45"
            )
        ],
        verbose_name="Player's age",
    )
    contract_length = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(
                0,
                message='Contract length must be greater than 0 years'
            )
        ],
        verbose_name='Contract length',
    )
    photo = models.ImageField(
        upload_to='media/profile_pics/',
        verbose_name="Hocker player's photo",
    )

    class Meta:
        ordering = ['player_surname', 'player_name']
        verbose_name = 'Profile cart'
        verbose_name_plural = 'Profile carts'
        constraints = [
            models.UniqueConstraint(
                fields=['player_name', 'player_surname'],
                name='unique_hockey_player_name_player_surname'
            )
        ]

    def __str__(self):
        return f'{self.player_name} {self.player_surname}.'
