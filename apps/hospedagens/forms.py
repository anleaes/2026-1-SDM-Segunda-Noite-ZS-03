from django import forms

from .models import Hospedagem


class HospedagemForm(forms.ModelForm):
    class Meta:
        model = Hospedagem
        fields = [
            "titulo",
            "descricao",
            "tipo",
            "endereco",
            "comodidades",
            "preco_diaria",
            "capacidade",
            "quartos",
            "banheiros",
            "ativo",
        ]
        widgets = {
            "descricao": forms.Textarea(attrs={"rows": 4}),
            "comodidades": forms.CheckboxSelectMultiple(),
        }
