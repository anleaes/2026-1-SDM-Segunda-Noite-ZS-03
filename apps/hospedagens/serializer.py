from rest_framework import serializers

from .models import Hospedagem

class HospedagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospedagem
        fields = '__all__'
