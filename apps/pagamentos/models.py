from django.db import models


class Pagamento(models.Model):
    STATUS_PENDENTE = "pendente"
    STATUS_PAGO = "pago"

    METODO_CHOICES = [
        ("cartao_credito", "Cartão de Crédito"),
        ("cartao_debito", "Cartão de Débito"),
        ("pix", "PIX"),
        ("boleto", "Boleto"),
        ("dinheiro", "Dinheiro"),
    ]

    STATUS_CHOICES = [
        (STATUS_PENDENTE, "Pendente"),
        (STATUS_PAGO, "Pago"),
        ("cancelado", "Cancelado"),
        ("reembolsado", "Reembolsado"),
    ]

    reserva = models.ForeignKey(
        "reservas.Reserva",
        verbose_name="Reserva",
        on_delete=models.CASCADE,
    )
    valor = models.DecimalField(
        verbose_name="Valor",
        max_digits=10,
        decimal_places=2,
    )
    metodo = models.CharField(
        verbose_name="Método",
        max_length=20,
        choices=METODO_CHOICES,
    )
    status = models.CharField(
        verbose_name="Status",
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PENDENTE,
    )
    data_pagamento = models.DateTimeField(
        verbose_name="Data do Pagamento",
        blank=True,
        null=True,
    )
    criado_em = models.DateTimeField(
        verbose_name="Criado em",
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "Pagamento"
        verbose_name_plural = "Pagamentos"
        ordering = ["id"]

    def __str__(self):
        return (
            f"Pagamento {self.id}: "
            f"Reserva {self.reserva_id} - R$ {self.valor} ({self.status})"
        )