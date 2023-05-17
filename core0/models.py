from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    descricao = models.CharField(max_length=255)
    def __str__(self):
        return self.descricao
        # retorna valor de descricao ao invés de classe objeto


class Responsavel(models.Model):
    class Meta:
        verbose_name_plural = "responsaveis"
        # resolve o plural correto 
    nome = models.CharField(max_length=255)
    contato = models.URLField()
    def __str__(self):
        return self.nome
        # retorna valor de descricao ao invés de classe objeto


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    preco = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="produtos")
    responsavel = models.ManyToManyField(Responsavel, related_name="produtos")
        # muitos para muitos

    def __str__(self):
        return "%s (%s)" %(self.nome, self.categoria)
    
class Compra(models.Model):

    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, 'Carrinho'
        REALIZADO = 2, 'Realizado'
        PAGO = 3, 'Pago'
        ENTREGUE = 4, 'Entregue'

    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="compras")
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.CARRINHO)

class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name="+")
    quantidade = models.IntegerField()