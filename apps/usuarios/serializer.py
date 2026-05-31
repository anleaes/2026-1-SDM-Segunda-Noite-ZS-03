from .models import Usuario
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["id", "nome", "email", "telefone", "cpf", "data_nascimento", "ativo", "criado_em",]
        
