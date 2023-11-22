from django.db import models
from datetime import date
from django.db.models.base import Model
from usuarios.models import Usuario

# Create your models here.
class Categoria(models.Model):
    nome= models.CharField(max_length=50)
    descricao=models.TextField()
    usuario =models.ForeignKey(Usuario,on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.nome
    

class Receita(models.Model):
    nome=models.CharField(max_length=100)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_de_preparo = models.CharField(max_length=10)
    rendimento = models.DecimalField(decimal_places=2, max_digits=5)
    data_cadastro=models.DateField(default=date.today)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)#o DO_NOTHING ignora,se apagar o livro não vaia acontecer nada com a categoria
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING) #definindo de quem é a receita

    def __str__(self):
        return self.nome
    

    class Ingrediente(models.Model):
        receita = models.ForeignKey('Receita', on_delete=models.CASCADE)
        quantidade = models.FloatField()
        unidade = models.CharField(max_length=30)
        ingrediente = models.CharField(max_length=100)

    class Meta:
        verbose_name='Receita'

class Historico(models.Model):
    usuario=models.ForeignKey(Usuario,on_delete=models.DO_NOTHING, blank=True, null =True)
    receita=models.ForeignKey(Receita,on_delete=models.DO_NOTHING,blank=True, null =True)
    data=models.DateField()

    
    def __str__(self) -> str:
        return f"{self.usuario} | {self.receita}"