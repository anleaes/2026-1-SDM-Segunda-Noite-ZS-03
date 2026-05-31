from django.db import models



class Comodidade(models.Model):
    nome = models.CharField(
        verbose_name="Nome",
        max_length=100,
    )
    descricao = models.TextField(
        verbose_name="Descrição",
    )
    icone = models.CharField(
        verbose_name="Ícone",
        max_length=50,
        blank=True,
        null=True,
    )
    ativo = models.BooleanField(
        verbose_name="Ativo",
        default=True,
    )

    class Meta:
        verbose_name = "Comodidade"
        verbose_name_plural = "Comodidades"
        ordering = ["id"]

    def __str__(self):
        return f"Comodidade #{self.id}: {self.nome}"