from .models import Pagamento
from rest_framework import serializers

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = ["id", "reserva", "valor", "metodo", "status", "data_pagamento", "criado_em",] 
