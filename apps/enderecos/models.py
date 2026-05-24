from django.db import models

class Endereco(models.Model):
    logradouro = models.CharField('Logradouro', max_length=200)
    numero = models.CharField('Número', max_length=10)
    complemento = models.CharField('Complemento', max_length=100, blank=True, null=True)
    bairro = models.CharField('Bairro', max_length=100)
    cidade = models.CharField('Cidade', max_length=100)
    estado = models.CharField('Estado', max_length=2)
    cep = models.CharField('CEP', max_length=9)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        ordering = ['id']

    def __str__(self):
        return f'{self.id} - {self.logradouro}, {self.numero}'
