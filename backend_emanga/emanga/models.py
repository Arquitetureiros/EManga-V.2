from django.db import models

# Create your models here.

class manga(models.Model):
  id = models.AutoField(primary_key=True)
  ds_sinopse = models.CharField(max_length=200)
  ds_titulo = models.CharField(max_length=45)
  valor = models.FloatField()
  quantidade = models.IntegerField(default=0)
  fotoCaminho = models.CharField(max_length=700)

class produto(models.Model):
  id = models.AutoField(primary_key = True)
  nm_produto = models.CharField(max_length=45)
  cd_produto = models.CharField(max_length=45)
  qt_produto = models.IntegerField()
  bo_ativo = models.CharField(max_length=45)  
