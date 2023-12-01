from django import forms
from .models import Receita, Categoria,Comentario
from datetime import date
from usuarios.models import Usuario

       
class CadastroReceita(forms.ModelForm):
    class Meta:
        model = Receita
        fields = "__all__"

    
    
    def __init__(self, *args, **kwargs):  #sempre que ouver uma instancia,to sobreescrevendo, to usando para tirar o campo do usuario no cadastro
        super().__init__(*args, **kwargs)
        self.fields['usuario'].widget = forms.HiddenInput()


         # Personalize o widget para o campo 'nome'
        self.fields['nome'].widget.attrs.update({'placeholder': 'Digite o nome','class': 'form-control'})

        # Personalize o widget para o campo 'ingredientes'
        self.fields['ingredientes'].widget.attrs.update({'placeholder': 'Adicione os ingredientes','class': 'form-control'})

        # Personalize o widget para o campo 'modo_preparo'
        self.fields['modo_preparo'].widget.attrs.update({'placeholder': 'Adicione o modo de preparo','class': 'form-control'})
        

        # Personalize o widget para o campo 'data_cadastro'
        self.fields['data_cadastro'].widget.attrs.update({'class': 'form-control'})

        # Personalize o widget para o campo 'categoria' (chave estrangeira)
        self.fields['categoria'].widget = forms.Select(attrs={ 'placeholder': 'Adicione a categoria','class': 'form-control'})

    
       
class CategoriaReceita(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome','descricao']

    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalize o widget para o campo 'nome'
        self.fields['nome'].widget.attrs.update({'placeholder': 'Digite o nome', 'class': 'form-control'})

        # Personalize o widget para o campo 'descricao'
        self.fields['descricao'].widget.attrs.update({'placeholder': 'Digite a descrição', 'class': 'form-control'})

        # Personalize o widget para o campo 'usuario'
       


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']

    def __init__(self, *args, user=None, receita=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.receita = receita

    def save(self, commit=True):
        comentario = super().save(commit=False)
        comentario.usuario = self.user if self.user and self.user.is_authenticated else None
        comentario.receita = self.receita
        if commit:
            comentario.save()
        return comentario







        
    
