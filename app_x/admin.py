from django.contrib import admin

from .models import Game
# Register your models here.


class CustomSnackAdmin(admin.ModelAdmin):
    model = Game
    fieldsets = (
        ('Owner', {
            'fields' : ('purchaser',)
        }),
        ('Game Info', {
            'fields':(
                'name',
                'desc'
            )
        })
    )

    list_display = ('name', 'purchaser')
    list_filter = ('name', 'desc')
    search_fields = ('name', 'desc')


admin.site.register(Game, CustomSnackAdmin)
