from django.contrib import admin
from .models import Anfitriao

@admin.register(Anfitriao)
class AnfitriaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'avaliacao_media']
