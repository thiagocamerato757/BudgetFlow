from django.db import models
from django.contrib.auth.models import User

class Despesa(models.Model):
    CATEGORIAS_DESPESAS = [
        ('alimentacao', 'Alimentação'),
        ('transporte', 'Transporte'),
        ('educacao', 'Educação'),
        ('moradia', 'Moradia'),
        ('saude', 'Saúde'),
        ('lazer', 'Lazer'),
        ('roupas', 'Roupas'),
        ('servicos', 'Serviços'),
        ('outros', 'Outros'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits = 10, decimal_places=2)
    data = models.DateField()
    categoria = models.CharField(max_length=20, choices=CATEGORIAS_DESPESAS,default='Outros')                                                                                                                                                                                                                                                                                                                                                                       

    def __str__(self):
        return f'{self.descricao} - {self.valor} ({self.categoria})'

class Receita(models.Model):
    CATEGORIAS_RECEITAS = [
        ('salario', 'Salário'),
        ('freelancer', 'Freelancer'),
        ('investimentos', 'Investimentos'),
        ('presentes', 'Presentes'),
        ('aluguel', 'Aluguel'),
        ('venda_bens', 'Venda de Bens'),
        ('outros', 'Outros'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    categoria = models.CharField(max_length=20, choices=CATEGORIAS_RECEITAS,default='Outros')

    def __str__(self):
        return f'{self.descricao} - {self.valor} ({self.categoria})'
