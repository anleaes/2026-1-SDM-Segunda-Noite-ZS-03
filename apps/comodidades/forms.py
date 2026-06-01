from django import forms

from .models import Comodidade


class ComodidadeForm(forms.ModelForm):
    class Meta:
        model = Comodidade
        fields = [
            "nome",
            "descricao",
            "icone",
            "ativo",
        ]
        widgets = {
            "descricao": forms.Textarea(attrs={"rows": 4}),
        }
