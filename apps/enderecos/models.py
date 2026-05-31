from django.db import models


class Endereco(models.Model):
    logradouro = models.CharField(
        verbose_name="Logradouro",
        max_length=200,
    )
    numero = models.CharField(
        verbose_name="Número",
        max_length=10,
    )
    complemento = models.CharField(
        verbose_name="Complemento",
        max_length=100,
        blank=True,
        null=True,
    )
    bairro = models.CharField(
        verbose_name="Bairro",
        max_length=100,
    )
    cidade = models.CharField(
        verbose_name="Cidade",
        max_length=100,
    )
    estado = models.CharField(
        verbose_name="Estado",
        max_length=2,
    )
    cep = models.CharField(
        verbose_name="CEP",
        max_length=9,
    )

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"
        ordering = ["id"]

    def __str__(self):
        return (
            f"Endereço{self.id}: "
            f"{self.logradouro}, {self.numero} - {self.cidade}/{self.estado}"
        )