import bcrypt
from django.db import models
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_email = models.EmailField(max_length=100, help_text="Digite o e-mail do usuário", unique=True)
    password = models.CharField(max_length=100, help_text="Digite a senha")
    total_depesas = models.FloatField(default=0)
    total_receita = models.FloatField(default=0)

    def __str__(self):
        return self.user_email

    def set_password(self, password):
        """
        Retorna o e-mail do usu rio como string de representao.
        
        A string de representao  usada em v rios locais do Django e 
        facilita a identifica o de um usu rio.
        """
        """
        Função que define o valor da senha do usuário.
        
        A senha é armazenada no banco de dados como um hash criptografado
        usando o algoritmo bcrypt.
        """
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        """
        Função para verificar se a senha digitada corresponde ao hash armazenado.
        """
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
