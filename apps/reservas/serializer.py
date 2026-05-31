from .models import Reserva
from rest_framework import serializers

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ["id", "hospedagem", "hospede", "data_checkin", "data_checkout", "quantidade_hospedes", "valor_total", "status", "criada_em",]

    def validate(self, data):
        if data["data_checkout"] <= data["data_checkin"]:
            raise serializers.ValidationError("A data de check-out deve ser posterior à data de check-in.")
        return data
