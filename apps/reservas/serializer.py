from .models import Reserva
from rest_framework import serializers

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ["id", "hospedagem", "hospede", "data_checkin", "data_checkout", "quantidade_hospedes", "valor_total", "status", "criada_em",]
        
