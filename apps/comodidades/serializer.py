from rest_framework import serializers

from .models import Comodidade


class ComodidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comodidade
        fields = (
            "id",
            "nome",
            "descricao",
            "icone",
            "ativo",
        )
