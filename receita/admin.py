from django.contrib import admin
from receita.models import Receita, Categoria,Historico
# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('nome','ingredientes', 'modo_preparo','tempo_de_preparo','rendimento', 'data_cadastro')

@admin.register(Historico)
class HistoricoAdmin(admin.ModelAdmin):
    list_display = ('usuario','receita','data')

