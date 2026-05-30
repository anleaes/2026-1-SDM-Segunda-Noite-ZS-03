from rest_framework import serializers

from .models import Anfitriao


class AnfitriaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anfitriao
        fields = (
            "id",
            "nome",
            "email",
            "telefone",
            "documento",
            "bio",
            "avaliacao_media",
        )
