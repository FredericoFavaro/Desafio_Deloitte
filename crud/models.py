from django.db import models

# Create your models here.
class equipe(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    cargo = models.CharField(max_length=30)
    telefone = models.IntegerField()
    email = models.CharField(max_length=30)