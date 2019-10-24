from django.db import models
from django.utils.datetime_safe import datetime

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField()
    telefone = models.CharField(max_length=15)
    saldo_bancario = models.DecimalField(max_digits=15, decimal_places=2)
    dt_cadastro = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.nome
