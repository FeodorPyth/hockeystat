from django.contrib import admin

from .models import ProfileCart

@admin.register(ProfileCart)
class ProfileCartAdmin(admin.ModelAdmin):
    list_display = (
        'player_name',
        'player_surname',
        'player_age',
        'contract_length'
)
    list_filter = ('player_age', 'contract_length',)
    search_fields = ('player_name', 'player_surname',)
