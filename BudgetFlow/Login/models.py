from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100,help_text="Digite o nome de usuário",primary_key=True)
    password = models.CharField(max_length=100,help_text="Digite a senha")
    total_depesas = models.FloatField(default=0)
    total_receita = models.FloatField(default=0)
  


    def __str__(self):
        return self.username
    

class Despesa(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.FloatField(default=0)
    decricao = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100)
    data = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.nome
    
class Receita(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.FloatField(default=0)
    decricao = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100)
    data = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.nome