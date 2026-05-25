from django.db import models

class Pagamento(models.Model):
    METODO_CHOICES = [
        ('cartao_credito', 'Cartão de Crédito'),
        ('cartao_debito', 'Cartão de Débito'),
        ('pix', 'PIX'),
        ('boleto', 'Boleto'),
        ('dinheiro', 'Dinheiro'),
    ]

    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('pago', 'Pago'),
        ('cancelado', 'Cancelado'),
        ('reembolsado', 'Reembolsado'),
    ]

    reserva = models.ForeignKey('reservas.Reserva', on_delete=models.CASCADE, verbose_name='Reserva')
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2)
    metodo = models.CharField('Método', max_length=20, choices=METODO_CHOICES)
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='pendente')
    data_pagamento = models.DateTimeField('Data do Pagamento', blank=True, null=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering = ['id']

    def __str__(self):
        return f'{self.id} - {self.reserva}'
