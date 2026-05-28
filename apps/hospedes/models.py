from django.db import models

class Hospede(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail')
    telefone = models.CharField('Telefone', max_length=20)
    documento = models.CharField('Documento', max_length=20)
    nacionalidade = models.CharField('Nacionalidade', max_length=50)
    data_nascimento = models.DateField('Data de Nascimento')

    class Meta:
        verbose_name = 'Hóspede'
        verbose_name_plural = 'Hóspedes'
        ordering = ['id']

    def __str__(self):
        return f'{self.id} - {self.nome}'
