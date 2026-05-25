from django.db import models
from reservas.models import Reserva


class Pagamento(models.Model):
    metodo = models.CharField('Método', max_length=20, choices=[
        ('Cartao', 'Cartão de Crédito'),
        ('Pix', 'Pix'),
        ('Boleto', 'Boleto'),
        ('Dinheiro', 'Dinheiro'),
    ])
    status = models.CharField('Status', max_length=20, choices=[
        ('Pendente', 'Pendente'),
        ('Pago', 'Pago'),
        ('Cancelado', 'Cancelado'),
    ])
    data_pagamento = models.DateTimeField('Data do Pagamento', auto_now_add=True)
    quantidade_parcelas = models.IntegerField('Quantidade de Parcelas', default=1)
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE, related_name='pagamento')

    class Meta:
        verbose_name = 'Pagamentos'
        verbose_name_plural = 'Pagamentos'
        ordering = ['id']

    def __str__(self):
        return f'Pagamento #{self.id}'
