from django.db import models
from django.utils import timezone


class Funcionario(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    equipe = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.nome} {self.sobrenome}'


class Obra(models.Model):
    lugar = models.CharField(max_length=50)
    atividade = models.CharField(max_length=50, default='Reforma')

    def __str__(self) -> str:
        return f'{self.lugar}'


class Chamada(models.Model):
    obra = models.ForeignKey(
        Obra,
        on_delete=models.CASCADE,
    )
    funcionario = models.ForeignKey(
        Funcionario,
        on_delete=models.CASCADE,
    )
    data = models.DateTimeField(default=timezone.now)
    presente = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.funcionario} - {self.obra} - {self.data}'
