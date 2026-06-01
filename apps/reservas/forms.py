from django import forms

from .models import Reserva


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = [
            "hospedagem",
            "hospede",
            "data_checkin",
            "data_checkout",
            "quantidade_hospedes",
            "valor_total",
            "status",
        ]
        widgets = {
            "data_checkin": forms.DateInput(attrs={"type": "date"}),
            "data_checkout": forms.DateInput(attrs={"type": "date"}),
        }

    def clean(self):
        dados = super().clean()
        data_checkin = dados.get("data_checkin")
        data_checkout = dados.get("data_checkout")

        if data_checkin and data_checkout and data_checkout <= data_checkin:
            raise forms.ValidationError(
                "A data de check-out deve ser posterior a data de check-in."
            )

        return dados
