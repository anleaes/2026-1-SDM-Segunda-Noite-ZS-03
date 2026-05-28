from django.db import models

class Hospedagem(models.Model):
    TIPO_CHOICES = [
        ('casa', 'Casa'),
        ('apartamento', 'Apartamento'),
        ('quarto', 'Quarto'),
        ('hostel', 'Hostel'),
        ('pousada', 'Pousada'),
    ]

    titulo = models.CharField('Título', max_length=200)
    descricao = models.TextField('Descrição')
    tipo = models.CharField('Tipo', max_length=20, choices=TIPO_CHOICES)
    endereco = models.ForeignKey('enderecos.Endereco', on_delete=models.CASCADE, verbose_name='Endereço')
    comodidades = models.ManyToManyField('comodidades.Comodidade', verbose_name='Comodidades', blank=True)
    preco_diaria = models.DecimalField('Preço da Diária', max_digits=10, decimal_places=2)
    capacidade = models.PositiveIntegerField('Capacidade')
    quartos = models.PositiveIntegerField('Quartos')
    banheiros = models.PositiveIntegerField('Banheiros')
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        verbose_name = 'Hospedagem'
        verbose_name_plural = 'Hospedagens'
        ordering = ['id']

    def __str__(self):
        return f'{self.id} - {self.titulo}'
