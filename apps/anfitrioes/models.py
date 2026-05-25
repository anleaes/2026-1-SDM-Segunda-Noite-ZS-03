from django.db import models

class Anfitriao(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail')
    telefone = models.CharField('Telefone', max_length=20)
    documento = models.CharField('Documento', max_length=20)
    bio = models.TextField('Biografia', blank=True, null=True)
    avaliacao_media = models.DecimalField('Avaliação Média', max_digits=3, decimal_places=2, default=0.0)

    class Meta:
        verbose_name = 'Anfitrião'
        verbose_name_plural = 'Anfitriões'
        ordering = ['id']

    def __str__(self):
        return f'{self.id} - {self.nome}'
