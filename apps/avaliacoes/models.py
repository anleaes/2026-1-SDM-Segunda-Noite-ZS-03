from django.db import models
from reservas.models import Reserva


class Avaliacao(models.Model):
    nota = models.IntegerField('Nota')
    comentario = models.TextField('Comentário', max_length=500)
    data = models.DateField('Data', auto_now_add=True)
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE, related_name='avaliacao')

    class Meta:
        verbose_name = 'Avaliações'
        verbose_name_plural = 'Avaliações'
        ordering = ['id']

    def __str__(self):
        return f'Avaliacao #{self.id}'
