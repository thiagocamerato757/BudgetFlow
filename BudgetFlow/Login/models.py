from django.db import models
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #Gera automaticamente um novo UUID para cada novo registro usando a função uuid.uuid4(), que cria um UUID aleatório.
    user_email = models.EmailField(max_length=100,help_text="Digite o e-mail do usuário",unique=True)                                                                     
    password = models.CharField(max_length=100,help_text="Digite a senha")
    total_depesas = models.FloatField(default=0)
    total_receita = models.FloatField(default=0)
  


    def __str__(self):
        return self.user_email
    

