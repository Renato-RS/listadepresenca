from django.contrib import admin
from presenca.models import *

# Register your models here.


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = 'nome', 'sobrenome', 'equipe', 'cargo',


@admin.register(Obra)
class ObraAdmin(admin.ModelAdmin):
    list_display = 'lugar', 'atividade',


@admin.register(Chamada)
class ChamadaAdmin(admin.ModelAdmin):
    list_display = 'funcionario', 'obra', 'data', 'presente',
