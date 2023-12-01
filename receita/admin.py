from django.contrib import admin
from receita.models import Receita, Categoria,Historico,Comentario
# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('img','nome','ingredientes', 'modo_preparo', 'data_cadastro')

@admin.register(Historico)
class HistoricoAdmin(admin.ModelAdmin):
    list_display = ('usuario','receita','data','avaliacao')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario','receita','texto','data_publicacao')

