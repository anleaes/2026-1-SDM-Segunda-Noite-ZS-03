from django.db import models


class Avaliacao(models.Model):
    hospedagem = models.ForeignKey(
        "hospedagens.Hospedagem",
        verbose_name="Hospedagem",
        on_delete=models.CASCADE,
    )
    nome_hospede = models.CharField(
        verbose_name="Nome do Hóspede",
        max_length=100,
    )
    email = models.EmailField(
        verbose_name="E-mail",
    )
    nota = models.PositiveIntegerField(
        verbose_name="Nota",
    )
    comentario = models.TextField(
        verbose_name="Comentário",
        blank=True,
        null=True,
    )
    data_avaliacao = models.DateTimeField(
        verbose_name="Data da Avaliação",
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
        ordering = ["id"]

    def __str__(self):
        return f"Avaliação #{self.id}: Nota {self.nota} para {self.hospedagem}"
