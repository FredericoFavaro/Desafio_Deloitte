from django.db import models

# Create your models here.
class equipe(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    cargo = models.CharField(max_length=30)
    telefone = models.IntegerField()
    email = models.CharField(max_length=30)

class servicos(models.Model):
    nome_servico = models.CharField(max_length=30)
    descricao = models.TextField(max_length=None)

class posts(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=30)
    data_publi = models.CharField(max_length=30)
    conteudo = models.TextField(max_length=None)