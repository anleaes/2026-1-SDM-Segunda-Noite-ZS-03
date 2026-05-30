from rest_framework import serializers

from .models import Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ("id", "hospedagem", "nome_hospede", "email", "nota", "comentario", "data_avaliacao")
