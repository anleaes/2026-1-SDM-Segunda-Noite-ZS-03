from rest_framework import serializers

from .models import Hospedagem


class HospedagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospedagem
        fields = (
            "id",
            "titulo",
            "descricao",
            "tipo",
            "endereco",
            "comodidades",
            "preco_diaria",
            "capacidade",
            "quartos",
            "banheiros",
            "ativo",
        )