from django.db import models

class Mensagem(models.Model):
    hospedagem = models.ForeignKey('hospedagens.Hospedagem', on_delete=models.CASCADE, verbose_name='Hospedagem')
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail')
    telefone = models.CharField('Telefone', max_length=20, blank=True, null=True)
    assunto = models.CharField('Assunto', max_length=200)
    mensagem = models.TextField('Mensagem')
    lida = models.BooleanField('Lida', default=False)
    enviada_em = models.DateTimeField('Enviada em', auto_now_add=True)

    class Meta:
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'
        ordering = ['id']

    def __str__(self):
        return f'{self.id} - {self.assunto} - {self.nome}'
