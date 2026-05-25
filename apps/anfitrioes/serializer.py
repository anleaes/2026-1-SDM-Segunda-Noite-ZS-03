from .models import Anfitriao
from rest_framework import serializers

class AnfitriaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anfitriao
        fields = '__all__'
