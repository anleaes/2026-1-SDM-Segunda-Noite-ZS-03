from django.db import models


class Endereco(models.Model):
    logradouro = models.CharField('Logradouro', max_length=100)
    rua = models.CharField('Rua', max_length=100)
    numero = models.CharField('Número', max_length=20)
    complemento = models.CharField('Complemento', max_length=100, blank=True, null=True)
    cidade = models.CharField('Cidade', max_length=100)
    estado = models.CharField('Estado', max_length=50)
    cep = models.CharField('CEP', max_length=10)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        ordering = ['id']

    def __str__(self):
        return f'{self.logradouro}, {self.rua}, {self.numero}'
