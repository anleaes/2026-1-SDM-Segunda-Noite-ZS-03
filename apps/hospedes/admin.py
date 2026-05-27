from django.contrib import admin
from .models import Hospede

@admin.register(Hospede)
class HospedeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone']
