from django.db import models

class Comodidade(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição')
    icone = models.CharField('Ícone', max_length=50, blank=True, null=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        verbose_name = 'Comodidade'
        verbose_name_plural = 'Comodidades'
        ordering = ['id']

    def __str__(self):
        return f'{self.id} - {self.nome}'
