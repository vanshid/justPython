from django.contrib import admin
from .models import Players

# Register your models here.

class PlayersAdmin(admin.ModelAdmin):
    list_display = ('firstName','lastName','dob',)

admin.site.register(Players, PlayersAdmin)
