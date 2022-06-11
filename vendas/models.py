from pyexpat import model
from django.db import models

class Cliente(models.Model):
    nome_completo = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    cpf = models.IntegerField(null=False)
    telefone = models.IntegerField(null=False)
    cep = models.IntegerField(null=False)
    endereco = models.CharField(max_length=200, null=False)
    cidade = models.CharField(max_length=100, null=False)
    sigla_estado = models.CharField(max_length=2, null=False)

    def __str__(self):
        return self.nome_completo

class Motocicleta(models.Model):
    marca = models.CharField(max_length=100, null=False)
    modelo = models.CharField(max_length=100, null=False)
    cor = models.CharField(max_length=50, null=False)
    placa = models.CharField(max_length=10, null=False)
    ano = models.IntegerField()
    descricao = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.marca + ' ' + self.modelo + ' ' + self.cor

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    motocicleta = models.OneToOneField(Motocicleta, on_delete=models.CASCADE)
    data_compra = models.DateTimeField()