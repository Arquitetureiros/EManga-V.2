from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)

class Endereco(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cep = models.CharField(max_length=9, default=None, blank=True, null=True)
    logradouro = models.CharField(max_length=100, default=None, blank=True, null=True)
    num = models.CharField(max_length=10, default=None, blank=True, null=True)
    cidade = models.CharField(max_length=100, default=None, blank=True, null=True)
    uf = models.CharField(max_length=2, default=None, blank=True, null=True)

class Cartao(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, default= 'null')
    nome = models.CharField(max_length=100)
    numero = models.CharField(max_length=16)
    validade = models.CharField(max_length=5)
    cvc = models.CharField(max_length=3)