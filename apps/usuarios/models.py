from django.db import models


class Usuario(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', null=False, blank=False)
    senha = models.CharField('Senha', max_length=100)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['id']

    def __str__(self):
        return f'{self.nome}'
