from django.db import models



class Anfitriao(models.Model):
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
    )
    documento = models.CharField(
        verbose_name="Documento",
        max_length=20,
    )
    bio = models.TextField(
        verbose_name="Biografia",
        blank=True,
        null=True,
    )
    avaliacao_media = models.DecimalField(
        verbose_name="Avaliação Média",
        max_digits=3,
        decimal_places=2,
        default=0.0,
    )

    class Meta:
        verbose_name = "Anfitrião"
        verbose_name_plural = "Anfitriões"
        ordering = ["id"]

    def __str__(self):
        return f"Anfitrião: {self.nome} (ID: {self.id})"
