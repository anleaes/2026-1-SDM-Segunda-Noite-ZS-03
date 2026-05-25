from django.db import models
from usuarios.models import Usuario


class Anfitriao(Usuario):
    cpf = models.CharField('CPF', max_length=14, blank=True, null=True)
    cnpj = models.CharField('CNPJ', max_length=18, blank=True, null=True)
    conta_bancaria = models.CharField('Conta Bancária', max_length=50)
    data_cadastro = models.DateField('Data de Cadastro', auto_now_add=True)
    avaliacao_media = models.FloatField('Avaliação Média', default=0.0)
    experiencia_desde = models.DateField('Experiência Desde')
    verificado_em = models.DateTimeField('Verificado Em', null=True, blank=True)

    class Meta:
        verbose_name = 'Anfitriões'
        verbose_name_plural = 'Anfitriões'
        ordering = ['id']

    def __str__(self):
        return f'Anfitriao #{self.id}'
