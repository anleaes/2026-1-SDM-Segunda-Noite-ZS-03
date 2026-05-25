from django.db import models
from usuarios.models import Usuario


class Hospede(Usuario):
    cpf = models.CharField('CPF', max_length=14)
    data_nascimento = models.DateField('Data de Nascimento')
    telefone = models.CharField('Telefone', max_length=20)

    class Meta:
        verbose_name = 'Hóspedes'
        verbose_name_plural = 'Hóspedes'
        ordering = ['id']

    def __str__(self):
        return f'Hospede #{self.id}'
