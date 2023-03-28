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
    user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, null = True)
    nome = models.CharField(max_length=100)
    numero = models.CharField(max_length=16)
    validade = models.CharField(max_length=5)
    cvc = models.CharField(max_length=3)

class Manga(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, null = True)
    ds_titulo = models.CharField(max_length=45)
    ds_sinopse = models.CharField(max_length=200)
    valor = models.FloatField()
    fotoCaminho = models.CharField(max_length=700)
    disponivel = models.BooleanField(default=True)

class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    dh_pedido = models.DateTimeField(auto_now_add=True)
    vl_total = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    entregue = models.BooleanField(default = False)

class ItemPedido(models.Model):
    id = models.AutoField(primary_key=True)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    qt_pedido = models.CharField(max_length=2, null=False)
    vl_total = models.DecimalField(max_digits=10, decimal_places=2, null=False)