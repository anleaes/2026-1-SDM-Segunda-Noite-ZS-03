from django import forms

from .models import Avaliacao


class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = [
            "hospedagem",
            "nome_hospede",
            "email",
            "nota",
            "comentario",
        ]
        widgets = {
            "comentario": forms.Textarea(attrs={"rows": 4}),
            "nota": forms.NumberInput(attrs={"min": 1, "max": 5}),
        }

    def clean_nota(self):
        nota = self.cleaned_data["nota"]

        if nota < 1 or nota > 5:
            raise forms.ValidationError("A nota deve estar entre 1 e 5.")

        return nota
