from django.db import models


class Comodidade(models.Model):
    nome = models.CharField('Nome', max_length=100)
    categoria = models.CharField('Categoria', max_length=100)
    disponivel = models.BooleanField('Disponível', default=True)

    class Meta:
        verbose_name = 'Comodidades'
        verbose_name_plural = 'Comodidades'
        ordering = ['id']

    def __str__(self):
        return f'Comodidade #{self.id}'
