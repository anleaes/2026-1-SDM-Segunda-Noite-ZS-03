from django.db import models
from anfitrioes.models import Anfitriao
from enderecos.models import Endereco
from comodidades.models import Comodidade


class Hospedagem(models.Model):
    titulo = models.CharField('Título', max_length=200)
    descricao = models.TextField('Descrição', max_length=500)
    preco_noite = models.DecimalField('Preço por Noite', max_digits=10, decimal_places=2)
    capacidade = models.IntegerField('Capacidade', default=1)
    status = models.BooleanField('Ativo', default=True)
    anfitriao = models.ForeignKey(Anfitriao, on_delete=models.CASCADE, verbose_name='Anfitrião')
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, related_name='hospedagem')
    comodidades = models.ManyToManyField(Comodidade, verbose_name='Comodidades')

    class Meta:
        verbose_name = 'Hospedagens'
        verbose_name_plural = 'Hospedagens'
        ordering = ['id']

    def __str__(self):
        return f'Hospedagem #{self.id}'
