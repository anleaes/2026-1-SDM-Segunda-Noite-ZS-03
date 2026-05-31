from django.db import models


class Hospedagem(models.Model):
    TIPO_CHOICES = [
        ("casa", "Casa"),
        ("apartamento", "Apartamento"),
        ("quarto", "Quarto"),
        ("hostel", "Hostel"),
        ("pousada", "Pousada"),
    ]

    titulo = models.CharField(
        verbose_name="Título",
        max_length=200,
    )
    descricao = models.TextField(
        verbose_name="Descrição",
    )
    tipo = models.CharField(
        verbose_name="Tipo",
        max_length=20,
        choices=TIPO_CHOICES,
    )
    endereco = models.ForeignKey(
        "enderecos.Endereco",
        verbose_name="Endereço",
        on_delete=models.CASCADE,
    )
    comodidades = models.ManyToManyField(
        "comodidades.Comodidade",
        verbose_name="Comodidades",
        blank=True,
    )
    preco_diaria = models.DecimalField(
        verbose_name="Preço da Diária",
        max_digits=10,
        decimal_places=2,
    )
    capacidade = models.PositiveIntegerField(
        verbose_name="Capacidade",
    )
    quartos = models.PositiveIntegerField(
        verbose_name="Quartos",
    )
    banheiros = models.PositiveIntegerField(
        verbose_name="Banheiros",
    )
    ativo = models.BooleanField(
        verbose_name="Ativo",
        default=True,
    )

    class Meta:
        verbose_name = "Hospedagem"
        verbose_name_plural = "Hospedagens"
        ordering = ["id"]

    def __str__(self):
        return (
            f"Hospedagem #{self.id}: {self.titulo} "
            f"({self.get_tipo_display()}) - R$ {self.preco_diaria}/dia"
        )