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


class RespostaMensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ["resposta"]
        widgets = {
            "resposta": forms.Textarea(attrs={"rows": 5}),
        }
