from django.db import models
from usuarios.models import Usuario


class Mensagem(models.Model):
    conteudo = models.TextField('Conteúdo', max_length=1000)
    data_envio = models.DateTimeField('Data de Envio', auto_now_add=True)
    visualizado = models.BooleanField('Visualizado', default=False)
    remetente = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Remetente')

    class Meta:
        verbose_name = 'Mensagens'
        verbose_name_plural = 'Mensagens'
        ordering = ['id']

    def __str__(self):
        return f'Mensagem #{self.id}'
