from rest_framework import serializers

from .models import Anfitriao


class AnfitriaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anfitriao
        fields = '__all__'
