from django.db import models

# Create your models here.

class Contacto(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    mensagem = models.TextField()



    def __str__(self):
        return self.nome