from django import forms

from .models import Pagamento


class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = [
            "reserva",
            "valor",
            "metodo",
            "status",
            "data_pagamento",
        ]
        widgets = {
            "data_pagamento": forms.DateTimeInput(
                attrs={"type": "datetime-local"},
                format="%Y-%m-%dT%H:%M",
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["data_pagamento"].input_formats = ["%Y-%m-%dT%H:%M"]

    def clean_valor(self):
        valor = self.cleaned_data["valor"]

        if valor <= 0:
            raise forms.ValidationError("O valor do pagamento deve ser maior que zero.")

        return valor
