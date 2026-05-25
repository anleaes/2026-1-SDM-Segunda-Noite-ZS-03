from .models import Hospedagem
from rest_framework import serializers

class HospedagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospedagem
        fields = '__all__'
