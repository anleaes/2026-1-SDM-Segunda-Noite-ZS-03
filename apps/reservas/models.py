from django.db import models
from hospedes.models import Hospede
from hospedagens.models import Hospedagem


class Reserva(models.Model):
    data_entrada = models.DateField('Data de Entrada')
    data_saida = models.DateField('Data de Saída')
    status = models.CharField('Status', max_length=20, choices=[
        ('Pendente', 'Pendente'),
        ('Confirmada', 'Confirmada'),
        ('Cancelada', 'Cancelada'),
        ('Concluída', 'Concluída'),
    ], default='Pendente')
    valor_total = models.DecimalField('Valor Total', max_digits=10, decimal_places=2)
    hospede = models.ForeignKey(Hospede, on_delete=models.CASCADE)
    hospedagem = models.ForeignKey(Hospedagem, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Reservas'
        verbose_name_plural = 'Reservas'
        ordering = ['id']

    def __str__(self):
        return f'Reserva #{self.id}'
