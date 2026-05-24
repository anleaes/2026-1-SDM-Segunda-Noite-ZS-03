from django.db import models

class Reserva(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('finalizada', 'Finalizada'),
    ]

    hospedagem = models.ForeignKey('hospedagens.Hospedagem', on_delete=models.CASCADE, verbose_name='Hospedagem')
    hospede = models.ForeignKey('hospedes.Hospede', on_delete=models.CASCADE, verbose_name='Hóspede')
    data_checkin = models.DateField('Data de Check-in')
    data_checkout = models.DateField('Data de Check-out')
    quantidade_hospedes = models.PositiveIntegerField('Quantidade de Hóspedes')
    valor_total = models.DecimalField('Valor Total', max_digits=10, decimal_places=2)
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='pendente')
    criada_em = models.DateTimeField('Criada em', auto_now_add=True)

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['id']

    def __str__(self):
        return f'{self.id} - {self.hospedagem}'
