from django import forms

from .models import Mensagem


class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = [
            "hospedagem",
            "nome",
            "email",
            "telefone",
            "assunto",
            "mensagem",
            "lida",
        ]
        widgets = {
            "mensagem": forms.Textarea(attrs={"rows": 5}),
        }
