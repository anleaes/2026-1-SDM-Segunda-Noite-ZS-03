from django.contrib import admin
from .models import Hospedagem

@admin.register(Hospedagem)
class HospedagemAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tipo', 'preco_diaria', 'ativo']
