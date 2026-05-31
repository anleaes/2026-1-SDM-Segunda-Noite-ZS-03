from django.db import models


class Hospede(models.Model):
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
    nacionalidade = models.CharField(
        verbose_name="Nacionalidade",
        max_length=50,
    )
    data_nascimento = models.DateField(
        verbose_name="Data de Nascimento",
    )

    class Meta:
        verbose_name = "Hóspede"
        verbose_name_plural = "Hóspedes"
        ordering = ["id"]

    def __str__(self):
        return f"Hóspede {self.id}: {self.nome} - Doc: {self.documento}"