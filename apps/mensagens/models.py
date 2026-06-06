from django.db import models


class Mensagem(models.Model):
    hospedagem = models.ForeignKey(
        "hospedagens.Hospedagem",
        verbose_name="Hospedagem",
        on_delete=models.CASCADE,
    )
    nome = models.CharField(
        verbose_name="Nome",
        max_length=100,
    )
    email = models.EmailField(
        verbose_name="E-mail",
    )
    telefone = models.CharField(
        verbose_name="Telefone",
        max_length=20,
        blank=True,
        null=True,
    )
    assunto = models.CharField(
        verbose_name="Assunto",
        max_length=200,
    )
    mensagem = models.TextField(
        verbose_name="Mensagem",
    )
    resposta = models.TextField(
        verbose_name="Resposta",
        blank=True,
        null=True,
    )
    lida = models.BooleanField(
        verbose_name="Lida",
        default=False,
    )
    enviada_em = models.DateTimeField(
        verbose_name="Enviada em",
        auto_now_add=True,
    )
    respondida_em = models.DateTimeField(
        verbose_name="Respondida em",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Mensagem"
        verbose_name_plural = "Mensagens"
        ordering = ["id"]

    def __str__(self):
        return f"Mensagem {self.id}: De {self.nome} - Assunto: {self.assunto}"
