from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)

class Endereco(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cep = models.CharField(max_length=9, default=None, blank=True, null=True)
    logradouro = models.CharField(max_length=100, default=None, blank=True, null=True)
    num = models.CharField(max_length=10, default=None, blank=True, null=True)
    cidade = models.CharField(max_length=100, default=None, blank=True, null=True)
    uf = models.CharField(max_length=2, default=None, blank=True, null=True)

class FormaPagamento(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=20, default=None, blank=True, null=False)

class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    endereco_entrega = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True)
    dh_pedido = models.DateTimeField(auto_now_add=True)
    vl_total = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    class Meta:
        ordering = ['-dh_pedido']

class Cobranca(models.Model):
    id = models.AutoField(primary_key=True)
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True)
    dh_criacao = models.DateTimeField(auto_now_add=True)
    dh_vencimento = models.DateTimeField(auto_now_add=False)
    vl_total = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    nr_parcelas = models.CharField(max_length=2, null=False)

class Pagamento(models.Model):
    id = models.AutoField(primary_key=True)
    cobranca = models.ForeignKey(Cobranca, on_delete=models.CASCADE)
    nr_parcela = models.IntegerField(null=False)
    dh_pagamento = models.DateTimeField(null=True)
    vl_fatura =  models.DecimalField(max_digits=10, decimal_places=2, null=False)
    vl_pago = models.DecimalField(max_digits=10, decimal_places=2, null=True)

class Manga(models.Model):
    id = models.AutoField(primary_key=True)
    ds_titulo = models.CharField(max_length=45)
    ds_sinopse = models.CharField(max_length=200)
    cidade = models.CharField(max_length=50,default='')
    estado = models.CharField(max_length=5,default='')
    valor = models.FloatField()
    quantidade = models.IntegerField(default=0)
    fotoCaminho = models.CharField(max_length=700)
    disponivel = models.BooleanField(default=True)

class ItemPedido(models.Model):
    id = models.AutoField(primary_key=True)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    qt_pedido = models.CharField(max_length=2, null=False)
    vl_unitario = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    vl_total = models.DecimalField(max_digits=10, decimal_places=2, null=False)