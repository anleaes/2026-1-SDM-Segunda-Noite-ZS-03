from django.db import models

class Reserva(models.Model):
    STATUS_CHOICES = [
        ("pendente", "Pendente"),
        ("confirmada", "Confirmada"),
        ("cancelada", "Cancelada"),
        ("finalizada", "Finalizada"),
    ]

    hospedagem = models.ForeignKey("hospedagens.Hospedagem", on_delete=models.CASCADE, verbose_name="Hospedagem")
    hospede = models.ForeignKey("hospedes.Hospede", on_delete=models.CASCADE, verbose_name="Hóspede")
    data_checkin = models.DateField("Data de Check-in")
    data_checkout = models.DateField("Data de Check-out")
    quantidade_hospedes = models.PositiveIntegerField("Quantidade de Hóspedes")
    valor_total = models.DecimalField("Valor Total", max_digits=10, decimal_places=2)
    status = models.CharField("Status", max_length=20, choices=STATUS_CHOICES, default="pendente")
    criada_em = models.DateTimeField("Criada em", auto_now_add=True)

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ["id"]

    def clean(self):
        super().clean()
        if self.data_checkin and self.data_checkout:
          if self.data_checkout <= self.data_checkin:
            raise ValidationError("A data de check-out deve ser posterior à data de check-in.")
    
    def __str__(self):
        return (
            f"Reserva {self.id}: "
            f"Hospede {self.hospede_id} em Hospedagem {self.hospedagem_id} ({self.status})"
        )