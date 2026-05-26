from django.db import models

class Avaliacao(models.Model):
    hospedagem = models.ForeignKey('hospedagens.Hospedagem', on_delete=models.CASCADE, verbose_name='Hospedagem')
    nome_hospede = models.CharField('Nome do Hóspede', max_length=100)
    email = models.EmailField('E-mail')
    nota = models.PositiveIntegerField('Nota')
    comentario = models.TextField('Comentário', blank=True, null=True)
    data_avaliacao = models.DateTimeField('Data da Avaliação', auto_now_add=True)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        ordering = ['id']

    def __str__(self):
        return f'{self.id} - {self.nota} - {self.hospedagem}'
