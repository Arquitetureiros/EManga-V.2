from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)

class Endereco(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=100)
    num = models.CharField(max_length=10)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
