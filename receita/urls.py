from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.home, name="home"),
    path('DetalheReceita/<int:id>',views.detalhe, name="detalhe"),
    path('Cadastrar_Receita',views.Cadastrar_Receita, name="Cadastrar_Receita"),
    path('Excluir_Receita/<int:id>',views.Excluir_Receita, name="Excluir_Receita"),
    path('cadastrar_categoria/', views.cadastrar_categoria, name='cadastrar_categoria'),
]