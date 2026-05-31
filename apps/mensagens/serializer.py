from rest_framework import serializers

from .models import Mensagem


class MensagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensagem
        fields = [
            "id",
            "hospedagem",
            "nome",
            "email",
            "telefone",
            "assunto",
            "mensagem",
            "lida",
            "enviada_em",
        ]