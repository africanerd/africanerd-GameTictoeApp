from django.contrib import admin
from .models import Game, Move


class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_player', 'second_player', 'status')
    list_editable = ('status',)
    list_filter = ['start_time', 'last_active']


admin.site.register(Game, GameAdmin)
admin.site.register(Move)
