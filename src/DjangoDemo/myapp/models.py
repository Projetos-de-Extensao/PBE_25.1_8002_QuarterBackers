from django.db import models

# Morador - Recenseador - Admnistrador
# Trabalhar com herança depois

class Morador(models.Model):
    idusuario = models.TextField(primary_key=True, max_length=10)
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField()
    cpf = models.TextField(max_length=11)
    senha = models.TextField()
    #chave estrangeira para tabela

    def __str__(self):
        return self.nome
    
class Domicilio(models.Model):
    # um caba é dono
    # só tem os numbers
    pass