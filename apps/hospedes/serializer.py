from .models import Hospede
from rest_framework import serializers

class HospedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospede
        fields = '__all__'
