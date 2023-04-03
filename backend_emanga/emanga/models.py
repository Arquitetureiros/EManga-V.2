from django.db import models

# Create your models here.

class manga(models.Model):
  id = models.AutoField(primary_key=True)
  ds_titulo = models.CharField(max_length=45)
  ds_sinopse = models.CharField(max_length=200)
  cidade = models.CharField(max_length=50, default='')
  estado = models.CharField(max_length=5, default='')
  valor = models.FloatField()
  quantidade = models.IntegerField(default=0)
  fotoCaminho = models.CharField(max_length=700)
