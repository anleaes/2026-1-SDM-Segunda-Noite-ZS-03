from django.contrib import admin
from .models import Comodidade

@admin.register(Comodidade)
class ComodidadeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ativo']
