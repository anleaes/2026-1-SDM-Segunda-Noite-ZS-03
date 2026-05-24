from django.db import models

class Usuario(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', unique=True)
    telefone = models.CharField('Telefone', max_length=20)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    data_nascimento = models.DateField('Data de Nascimento')
    ativo = models.BooleanField('Ativo', default=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['id']

    def __str__(self):
        return f'{self.id} - {self.nome}'
