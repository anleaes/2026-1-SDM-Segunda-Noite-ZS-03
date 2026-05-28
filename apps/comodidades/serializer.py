from .models import Comodidade
from rest_framework import serializers

class ComodidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comodidade
        fields = '__all__'
